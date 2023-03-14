from datetime import datetime

class Task:
    def __init__(self, name, desc, deadline) -> None:
        self.name = name
        self.desc = desc
        self.deadline = deadline
        self.next = None
        self.prev = None

class TaskManager:
    def __init__(self) -> None:
        self.today = datetime.today().date().strftime("%d/%m/%y")
        self.first = None
        self.last = None
        self.size = 0
        self.__load_tasks()

    def append_task(self, name, desc, deadline):
        new_task = Task(name, desc, deadline)
        if self.is_empty():
            self.first = new_task
            self.last = new_task
            self.size += 1
            return
        
        new_task.prev = self.last
        self.last.next = new_task
        self.last = new_task
        self.size += 1

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
Descrição: {cur_task.desc}
Prazo: {cur_task.deadline}
Você tem {days_left} dia(s) restante(s)
'''
                else:
                    s = f'''-------Tarefa encontrada-------
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
            print(f"Nome: {cur_task.name}\nDescrição: {cur_task.desc}\nPrazo: {cur_task.deadline}")
            print("-------------------------------")
            cur_task = cur_task.next

    def edit_task(self, index):
        if index >= len(self) or index < 0:
            raise IndexError("Index out of range")
        
        elif index == 0:
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
                file.write(f"{current.name}\n{current.desc}\n{current.deadline}")
                file.write("\n")
                current = current.next
    
    def __load_tasks(self):
        try:
            with open("tasks.txt", "r") as file:
                lines = file.readlines()
                for i in range(0, len(lines), 3):
                    self.append_task(lines[i].strip(), lines[i+1].strip(), lines[i+2].strip())

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

                if name == "" or desc == "" or deadline == "":
                    return print("Você não pode deixar nenhum campo em branco!")
                
                taskman.append_task(name, desc, deadline)
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

# TODO: Add a way to store tasks in a file