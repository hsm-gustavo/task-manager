from datetime import datetime

class Task:
    def __init__(self, name, desc, deadline, priority: int) -> None:
        self.name = name
        self.desc = desc
        self.deadline = deadline
        self.priority = priority
        self.next = None
        self.prev = None

class TaskManager:
    def __init__(self) -> None:
        self.today = datetime.today().date().strftime("%d/%m/%y")
        self.first = None
        self.last = None
        self.size = 0
        self.__load_tasks()

    def append_task(self, new_task: Task):
        new_task.prev = self.last
        self.last.next = new_task
        self.last = new_task
        self.size += 1

    def add_sorted(self, name, desc, deadline, priority: int = 0):
        new_task = Task(name, desc, deadline, priority)

        if self.is_empty():
            self.first = new_task
            self.last = new_task
            self.size += 1
            return
        
        elif new_task.priority < self.first.priority:
            new_task.next = self.first
            self.first.prev = new_task
            self.first = new_task
            self.size += 1
            return
        
        elif new_task.priority >= self.last.priority:
            self.append_task(new_task)
            return
        
        current = self.first.next
        while current is not None:
            if new_task.priority < current.priority:
                new_task.next = current
                new_task.prev = current.prev
                if current.prev is not None:
                    current.prev.next = new_task
                current.prev = new_task
                self.size += 1
                return
            elif new_task.priority == current.priority:
                new_task.next = current.next
                new_task.prev = current
                if current.next is not None:
                    current.next.prev = new_task
                current.next = new_task
                self.size += 1
                return
            current = current.next

    def sort(self):
        if self.size < 2:
            return

        for i in range(self.size):
            node = self.first
            for j in range(self.size - 1 - i):
                if node.priority > node.next.priority:
                    next_node = node.next
                    node.next = next_node.next
                    if next_node.next is not None:
                        next_node.next.prev = node
                    next_node.prev = node.prev
                    if node.prev is not None:
                        node.prev.next = next_node
                    else:
                        self.first = next_node
                    node.prev = next_node
                    next_node.next = node
                else:
                    node = node.next


    def search_task(self, name):
        cur_task = self.first
        while cur_task is not None:
            if cur_task.name == name:

                conversion_type = "%d/%m/%y" if len(cur_task.deadline)<9 else "%d/%m/%Y"

                days_left =  datetime.strptime(cur_task.deadline, conversion_type) - datetime.strptime(self.today, "%d/%m/%y")
                days_left = days_left.days

                s = str()
                if days_left >= 0:
                    s = f'''-------Tarefa encontrada-------
Prioridade: {cur_task.priority}
Descrição: {cur_task.desc}
Prazo: {cur_task.deadline}
Você tem {days_left} dia(s) restante(s)
'''
                else:
                    s = f'''-------Tarefa encontrada-------
Prioridade: {cur_task.priority}
Descrição: {cur_task.desc}
Prazo: {cur_task.deadline}
Você está {abs(days_left)} dia(s) atrasado
'''

                return print(s)
            
            cur_task = cur_task.next

        print("Tarefa não encontrada")

    def remove_task(self, index):
        if index >= len(self) or index < 0:
            raise IndexError("Index out of range")
        
        elif index == 0:
            self.first = self.first.next
            if self.first is not None:
                self.first.prev = None
            self.size -= 1
            return print("\n--------Tarefa removida--------\n")
        
        elif index == len(self)-1:
            self.last = self.last.prev
            if self.last is not None:
                self.last.next = None
            self.size -= 1
            return print("\n--------Tarefa removida--------\n")
        
        current = self.first.next
        cur_index = 1

        while cur_index != index:
            current = current.next
            cur_index += 1

        current.prev.next = current.next
        current.next.prev = current.prev
        self.size -= 1

        return print("\n--------Tarefa removida--------\n")
    
    def show_tasks(self):
        cur_task = self.first
        self.length()
        while cur_task is not None:
            print(f"Prioridade: {cur_task.priority}\nNome: {cur_task.name}\nDescrição: {cur_task.desc}\nPrazo: {cur_task.deadline}")
            print("-------------------------------")
            cur_task = cur_task.next

    def edit_task(self, index):
        if index >= len(self) or index < 0:
            raise IndexError("Index out of range")
        
        elif index == 0:
            priority = input("Digite a nova prioridade da tarefa:\n")
            if priority != "":
                self.first.priority = int(priority)
            name = input("Digite o novo nome da tarefa:\n")
            if name != "":
                self.first.name = name
            desc = input("Digite a nova descrição da tarefa:\n")
            if desc != "":
                self.first.desc = desc
            deadline = input("Digite o novo prazo da tarefa (no estilo DD/MM/AA ou DD/MM/AAAA):\n")
            if deadline != "":
                self.first.deadline = deadline
            return
        
        elif index == len(self)-1:
            priority = input("Digite a nova prioridade da tarefa:\n")
            if priority != "":
                self.last.priority = int(priority)
            name = input("Digite o novo nome da tarefa:\n")
            if name != "":
                self.last.name = name
            desc = input("Digite a nova descrição da tarefa:\n")
            if desc != "":
                self.last.desc = desc
            deadline = input("Digite o novo prazo da tarefa (no estilo DD/MM/AA ou DD/MM/AAAA):\n")
            if deadline != "":
                self.last.deadline = deadline
            return

        current = self.first.next
        cur_index = 1

        while cur_index != index:
            current = current.next
            cur_index += 1
        
        priority = input("Digite a nova prioridade da tarefa:\n")
        if priority != "":
            current.priority = int(priority)
        name = input("Digite o novo nome da tarefa:\n")
        if name != "":
            current.name = name
        desc = input("Digite a nova descrição da tarefa:\n")
        if desc != "":
            current.desc = desc
        deadline = input("Digite o novo prazo da tarefa (no estilo DD/MM/AA ou DD/MM/AAAA):\n")
        if deadline != "":
            current.deadline = deadline

    def is_empty(self) -> bool:
        return self.first == None
    
    def length(self):
        print(f"\nVocê tem {len(self)} tarefa(s)\n")
    
    def __len__(self) -> int:
        return self.size
    
    def save_tasks(self):
        with open("tasks.txt", "w") as file:
            current = self.first
            while current is not None:
                file.write(f"{current.priority}\n{current.name}\n{current.desc}\n{current.deadline}")
                file.write("\n")
                current = current.next
    
    def __load_tasks(self):
        try:
            with open("tasks.txt", "r") as file:
                lines = file.readlines()
                for i in range(0, len(lines), 4):
                    priority = int(lines[i].strip())
                    name = lines[i+1].strip()
                    desc = lines[i+2].strip()
                    deadline = lines[i+3].strip()
                    self.add_sorted(name, desc, deadline, priority)
        except FileNotFoundError:
            pass   
    
def menu(taskman: TaskManager):
    try:
        command = int(input("1) Adicionar Tarefa\n2) Procurar tarefa (requer nome)\n3) Remover Tarefa (requer índice)\n4) Quantidade de tarefas\n5) Listar tarefas\n6) Editar tarefa (requer índice)\n7) Sair do programa\nDigite o que deseja fazer: "))

        if command>7 or command<1:
            raise ValueError
        
        match command:
            case 1:
                name = input("Digite o nome da tarefa:\n")
                desc = input("Digite a descrição da tarefa:\n")
                deadline = input("Digite o prazo da tarefa (no estilo DD/MM/AA ou DD/MM/AAAA):\n")
                priority = input("Digite a prioridade da tarefa (1 é a mais alta, 5 é a mais baixa):\n")

                if name == "" or desc == "" or deadline == "" or priority == "":
                    return print("Você não pode deixar nenhum campo em branco!")
                
                elif int(priority) > 5 or int(priority) < 1:
                    return print("A prioridade deve ser um número entre 1 e 5!")
                
                taskman.add_sorted(name, desc, deadline, int(priority))
            case 2:
                name = input("Digite o nome da tarefa:\n")
                taskman.search_task(name)
            case 3:
                idx = int(input("Digite o índice da tarefa (a primeira tarefa tem índice zero):\n"))
                taskman.remove_task(idx)
            case 4:
                taskman.length()
            case 5:
                taskman.show_tasks()
            case 6:
                idx = int(input("Digite o índice da tarefa (a primeira tarefa tem índice zero):\n"))
                taskman.edit_task(idx)
                taskman.sort()
            case 7:
                taskman.save_tasks()
                raise KeyboardInterrupt
            
    except ValueError:
        print("Digite um número válido!")

    except IndexError:
        print("Este índice não existe nas tarefas ou não foi digitado um índice válido")

if __name__=="__main__":
    taskman = TaskManager()
    
    try:
        while True:
            menu(taskman)
    except KeyboardInterrupt:
        taskman.save_tasks()
        print("\nSaindo do programa...")