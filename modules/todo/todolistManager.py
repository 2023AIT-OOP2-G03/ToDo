if __name__ == '__main__': import taskManager
else: from modules.todo import taskManager
from datetime import datetime as dt
import uuid
import json
import datetime

USERS_DIR = './data/users/'

def add_task(userid, task: taskManager.task):
    """タスクを追加する
    
    args:
        userid (str): ユーザーID
        task (taskManager.task): タスク
    """
    # idの生成
    id = uuid.uuid4()
    set_task(userid, str(id), task)
    
    
def delete_task(userid, taskid):
    """タスクを削除する
    
    args:
        userid (str): ユーザーID
        taskid (str): タスクID
    """
    if check_task(userid, taskid):
        tasks = get_tasks(userid)
        tasks.pop(taskid)
        set_tasks(userid, tasks)
    else:
        print("タスクが存在しません")
    

def set_task(userid, taskid, task: taskManager.task):
    """タスクを設定する
    
    args:
        userid (str): ユーザーID
        taskid (str): タスクID
        task (taskManager.task): タスク"""
    tasks = get_tasks(userid)
    
    # タスクの生成
    tasks[taskid] = task.to_dict()
    
    set_tasks(userid, tasks)

def set_task_status(userid, taskid, status: taskManager.task_status):
    """タスクのステータスを設定する
    
    args:
        userid (str): ユーザーID
        taskid (str): タスクID
        status (str): タスクのステータス
    """
    tasks = get_tasks(userid)
    tasks[taskid]["status"] = status
    set_tasks(userid, tasks)

def get_tasks(userid):
    """タスクを取得する
    
    args:
        userid (str): ユーザーID
    returns:
        dict: タスク
    """
    # jsonファイルの読み込み
    user_data = json.load(open(USERS_DIR + userid + ".json", "r"))
    return user_data["tasks"]

def set_tasks(userid, tasks):
    """タスクを設定する
    
    args:
        userid (str): ユーザーID
        tasks (dict): タスク
    """
    user_data = json.load(open(USERS_DIR + userid + ".json", "r"))
    user_data["tasks"] = tasks
    json.dump(user_data, open(USERS_DIR + userid + ".json", "w"), indent = 4)

def check_task(userid, taskid):
    """タスクの存在を確認する
    
    args:
        userid (str): ユーザーID
        taskid (str): タスクID
    returns:
        bool: タスクの存在(True: 存在する, False: 存在しない)
    """
    tasks = get_tasks(userid)
    if taskid in tasks:
        return True
    else:
        return False

if __name__ == '__main__':
    # task_date = dt.strptime("[2024-1-9]", "[%Y-%m-%d]")
    # add_task("test", taskManager.task("ni", "nikome", taskManager.task_status.NOT_READY, task_date))
    
    # tasks = get_tasks("test")
    # for i in tasks:
    #     print(i)
    #     print(tasks[i])
    #     delete_task("test", i)
    
    # print(type(tasks))
    set_task_status("test", "f55b810b-b462-49d4-9656-abc59b833850", taskManager.task_status.DOING)
    pass