import task

def add_task(tasks, name, description, status):
    tasks.append(task.task(name, description, status))
    

def delete_task():
    pass

if __name__ == '__main__':
    # test
    tasks = []
    add_task(tasks, "test", "test", task.task_status.NOT_READY)
    for i in tasks:
        print(i)
    
    pass