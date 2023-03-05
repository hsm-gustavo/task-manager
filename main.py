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

    def append_task(self, name, desc, deadline):
        new_task = Task(name, desc, deadline)
        if self.is_empty():
            self.first = new_task
            self.last = new_task
            return
        
        new_task.prev = self.last
        self.last.next = new_task
        self.last = new_task

    def search_task(self, name):
        cur_task = self.first
        while cur_task is not None:
            if cur_task.name == name:

                conversion_type = "%d/%m/%y" if len(cur_task.deadline)<9 else "%d/%m/%Y"

                days_left =  datetime.strptime(cur_task.deadline, conversion_type) - datetime.strptime(self.today, "%d/%m/%y")

                return print(f"-------Tarefa encontrada-------\nDescrição: {cur_task.desc}\nPrazo: {cur_task.deadline}\nVocê tem {days_left.days} dia(s) restante(s)") \
                if days_left.days>=0 else print(f"-------Tarefa encontrada-------\nDescrição: {cur_task.desc}\nPrazo: {cur_task.deadline}\nVocê está {abs(days_left.days)} dia(s) atrasado")
            
            cur_task = cur_task.next
            
        print("Tarefa não encontrada")

    def remove_task(self, index):
        if len(self) == 0:
            return print("\nVocê ainda não adicionou nenhuma tarefa\n")

        elif index >= len(self) or index < 0:
            raise IndexError("Index out of range")
        
        if index == 0:
            self.first = self.first.next
            if self.first is not None:
                self.first.prev = None
            return print("\n--------Tarefa removida--------\n")
        
        elif index == len(self)-1:
            self.last = self.last.prev
            if self.last is not None:
                self.last.next = None
            return print("\n--------Tarefa removida--------\n")
        
        current = self.first
        cur_index = 0

        while cur_index != index:
            current = current.next
            cur_index += 1

        current.prev.next = current.next
        current.next.prev = current.prev

        return print("\n--------Tarefa removida--------\n")
    
    def show_tasks(self):
        cur_task = self.first
        print(f"Você tem {len(self)} tarefa(s)\n")
        while cur_task is not None:
            print(f"Nome: {cur_task.name}\nDescrição: {cur_task.desc}\nPrazo: {cur_task.deadline}")
            print("-------------------------------")
            cur_task = cur_task.next

    def is_empty(self) -> bool:
        return self.first == None
    
    def length(self):
        return print(f"Você tem {len(self)} tarefa(s)")
    
    def __len__(self) -> int:
        current = self.first
        size = 0
        while current is not None:
            size += 1
            current = current.next
        return size

def menu(taskman: TaskManager):
    try:
        command = int(input("1) Adicionar Tarefa\n2) Procurar tarefa (requer nome)\n3) Remover Tarefa (requer índice)\n4) Quantidade de tarefas\n5) Mostrar tarefas\n6) Sair do programa\nDigite o que deseja fazer: "))

        if command>6 or command<1:
            raise ValueError
        
        match command:
            case 1:
                name = input("Digite o nome da tarefa:\n")
                desc = input("Digite a descrição da tarefa:\n")
                deadline = input("Digite o prazo da tarefa (no estilo DD/MM/AA ou DD/MM/AAAA):\n")
                
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
                raise KeyboardInterrupt
            
    except ValueError:
        print("Digite um número válido!")

    except IndexError:
        print("Este índice não existe nas tarefas")

if __name__=="__main__":
    taskman = TaskManager()
    
    try:
        while True:
            menu(taskman)
    except KeyboardInterrupt:
        print("\nSaindo do programa...")