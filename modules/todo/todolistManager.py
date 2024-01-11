import taskManager
import uuid
import json

USERS_DIR = './data/users/'

def add_task(userid, task: taskManager.task):
    # idの生成
    id = uuid.uuid4()
    set_task(userid, str(id), task)
    
    
def delete_task(userid, taskid):
    if check_task(taskid):
        tasks = get_tasks(userid)
        tasks.pop(taskid)
        set_tasks(userid, tasks)
    else:
        print("タスクが存在しません")
    

def set_task(userid, taskid, task: taskManager.task):
    tasks = get_tasks(userid)
    
    # タスクの生成
    tasks[taskid] = task.to_dict()
    
    set_tasks(userid, tasks)

def get_tasks(userid):
    # jsonファイルの読み込み
    user_data = json.load(open(USERS_DIR + userid + ".json", "r"))
    return user_data["tasks"]

def set_tasks(userid, tasks):
    user_data = json.load(open(USERS_DIR + userid + ".json", "r"))
    user_data["tasks"] = tasks
    json.dump(user_data, open(USERS_DIR + userid + ".json", "w"), indent = 4)

def check_task(userid, taskid):
    tasks = get_tasks(userid)
    if taskid in tasks:
        return True
    else:
        return False

if __name__ == '__main__':
    # add_task("test", taskManager.task("test", "test", taskManager.task_status.NOT_READY))
    
    tasks = get_tasks("test")
    for i in tasks:
        print(i)
        print(tasks[i])
    
    pass