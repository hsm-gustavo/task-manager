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

    def append_task(self):
        pass

    def search_task(self):
        pass
    
    def show_tasks(self):
        pass

    def is_empty(self):
        return self.first == None
