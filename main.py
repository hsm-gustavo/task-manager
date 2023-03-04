class Task:
    def __init__(self, name, desc, deadline) -> None:
        self.name = name
        self.desc = desc
        self.deadline = deadline
        self.next = None
        self.prev = None

class TaskManager:
    def __init__(self) -> None:
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
                return print(f"-------Tarefa encontrada-------\nDescrição: {cur_task.desc}\nPrazo: {cur_task.deadline}")
            cur_task = cur_task.next
        print("Tarefa não encontrada")
    
    def show_tasks(self):
        cur_task = self.first
        print(f"Você tem {len(self)} tarefa(s)\n")
        while cur_task is not None:
            print(f"Nome: {cur_task.name}\nDescrição: {cur_task.desc}\nPrazo: {cur_task.deadline}")
            print("------------------------------")
            cur_task = cur_task.next

    def is_empty(self) -> bool:
        return self.first == None
    
    def length(self) -> int:
        current = self.first
        size = 0
        while current is not None:
            size += 1
            current = current.next
        return size
    
    def __len__(self) -> int:
        return self.length()


taskman = TaskManager()

taskman.append_task("Atividade de CSD", "Fazer a atividade de CSD", "11/03/23")
taskman.append_task("Trabalho de ACE2", "Enviar o Trabalho de ACE2 no AVA", "04/03/23")
taskman.append_task("Reunião", "Reunião com o Prof. Adriano", "09/03/23")

taskman.show_tasks()

taskman.search_task("Atividade de CSD")