from enum import Enum

class task_status(Enum):
    NOT_READY = 1
    READY = 2
    DOING = 3
    DONE = 4

class task:
    def __init__(self, name = "", description = "", status = task_status.NOT_READY):
        self.name = name
        self.description = description
        self.status = status

    def __str__(self):
        return f"{self.name}\n {self.description}\n {self.status}"
    
    def get_name(self):
        return self.name

    def get_description(self):
        return self.description
    
    def get_status(self):
        return self.status
    
    def set_name(self, name):
        self.name = name
    
    def set_description(self, description):
        self.description = description
        
    def set_status(self, status):
        self.status = status
