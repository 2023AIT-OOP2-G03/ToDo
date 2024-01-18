from enum import Enum
import json
import datetime

class task_status(str, Enum):
    NOT_READY = "not ready"
    READY = "ready"
    DOING = "doing"
    DONE = "done"

class task:
    def __init__(self, name = "", description = "", status = task_status.NOT_READY, timeLimit = datetime.datetime.now()):
        self.name = name
        self.description = description
        self.status = status
        self.timeLimit = timeLimit

    def __str__(self):
        return f"{self.name}\n desc: {self.description}\n status: {self.status}"

    
    def get_name(self):
        """タスク名を取得する
        
        returns:
            str: タスク名
        """
        return self.name

    def get_description(self):
        """タスクの説明を取得する
        
        returns:
            str: タスクの説明
        """
        return self.description
    
    def get_status(self):
        """タスクのステータスを取得する
        
        returns:
            str: タスクのステータス
        """
        return self.status

    def get_timeLimit(self):
        """タスクの期限を取得する
        
        returns:
            datetime.datetime: タスクの期限
        """
        return self.timeLimit
    
    def set_name(self, name):
        """タスク名を設定する
        
        args:
            name (str): タスク名
        returns:
            str: タスク名
        """
        self.name = name
    
    def set_description(self, description):
        """タスクの説明を設定する
        
        args:
            description (str): タスクの説明
        returns:
            str: タスクの説明
        """
        self.description = description
        
    def set_status(self, status):
        """タスクのステータスを設定する
        
        args:
            status (str): タスクのステータス
        returns:
            str: タスクのステータス
        """
        self.status = status
    
    def set_timeLimit(self, timeLimit):
        """タスクの期限を設定する
        
        args:
            timeLimit (datetime.datetime): タスクの期限
        returns:
            datetime.datetime: タスクの期限
        """
        self.timeLimit = timeLimit

    def to_dict(self):
        """タスクを辞書型に変換する
        
        returns:
            dict: タスクの辞書型
        """
        return {
            "name": self.name,
            "description": self.description,
            "status": self.status,
            "timeLimit": self.timeLimit.strftime("%Y/%m/%d %H:%M:%S")
        } 