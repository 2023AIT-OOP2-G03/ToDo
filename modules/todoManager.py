from enum import Enum

class task_status(Enum):
    NOT_READY = 1
    READY = 2
    DOING = 3
    DONE = 4

class task:
    name = "買い物に行く"
    description = "卵と牛乳を買う"
    status = task_status.NOT_READY
    
    def get_name(self):
        return self.name

    def get_description(self):
        return self.description
    
    def get_status(self):
        return self.status
    
    def create():
        pass
    
    def delete():
        pass
