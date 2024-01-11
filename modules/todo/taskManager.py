from enum import Enum
import json

class task_status(str, Enum):
    NOT_READY = "not ready"
    READY = "ready"
    DOING = "doing"
    DONE = "done"

class task:
    def __init__(self, name = "", description = "", status = task_status.NOT_READY):
        self.name = name
        self.description = description
        self.status = status

    def __str__(self):
        return f"{self.name}\n desc: {self.description}\n status: {self.status}"

    
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

    def to_dict(self):
        return {
            "name": self.name,
            "description": self.description,
            "status": self.status
        } 