import taskManager
import uuid
import json

USERS_DIR = './data/users/'

def add_task(userid, name, description, status):
    # idの生成
    id = uuid.uuid4()
    # jsonファイルの読み込み
    user_data = json.load(open(USERS_DIR + userid + ".json", "r"))
    tasks = user_data["tasks"]
    
    # タスクの生成
    task = taskManager.task(name, description, status)
    tasks[str(id)] = task.to_dict()
    
    user_data["tasks"] = tasks
    json.dump(user_data, open(USERS_DIR + userid + ".json", "w"))
    
    
def delete_task(id):
    tasks.pop(id)

def set_task():
    pass

def get_task():
    pass

if __name__ == '__main__':
    # test
    tasks = {}
    add_task("test", "test", "test", taskManager.task_status.NOT_READY)
    for i in tasks:
        print(i)
    
    pass