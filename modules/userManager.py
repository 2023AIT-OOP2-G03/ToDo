import json
import hashlib
import os

USERS_FILE_PATH = './data/users.json'

TASKS_FILE_DIR = './data/tasks/'

# 作成
def create(id, pw):
    if check(id):
        return "ユーザーが存在します"
    else:
        # users.jsonを読み込み
        users = json.load(open(USERS_FILE_PATH, 'r'))
        # ユーザーを作成
        # パスワードをハッシュ化
        hashed_pw = get_digest(pw)
        users[id] = {"pw": hashed_pw}
        
        # ユーザーのタスクファイルを作成
        tasks_file = open(TASKS_FILE_DIR + id + '.json', 'w')
        # 空のjsonファイルを作成
        tasks_file.write('{}')
        tasks_file.close()
        
        # users.jsonを書き込み
        json.dump(users, open(USERS_FILE_PATH, 'w'))
        # TODO: なぜか「0」を返している、main.pyを編集してTrueにすべき
        # return True
        return 0

# ユーザーの存在を確認
def check(id):
    # users.jsonを読み込み
    users = json.load(open(USERS_FILE_PATH, 'r'))
    flag_users = id in users
    
    # タスクファイルの存在を確認
    flag_tasks = os.path.exists(TASKS_FILE_DIR + id + '.json')
    
    # ユーザーの存在を確認
    if flag_users and flag_tasks:
        return True
    elif flag_users or flag_tasks:
        print("!!!ユーザーの存在に矛盾があります!!!")
        print(f"\tusers.json: {flag_users}")
        print(f"\t{id}.json: {flag_tasks}")
        print("整合性解決のため、ユーザーを削除します")
        __force_delete(id)
        return False
    else:
        return False
    
def get_digest(pw):
    # SHA256でハッシュ化
    hashed_pw = hashlib.sha256(pw.encode("utf-8")).hexdigest()
    return hashed_pw

def delete(id):
    if check(id):
        __force_delete(id)
    else:
        return "ユーザーが存在しません"

def __force_delete(id):
    # users.jsonを読み込み
    users = json.load(open(USERS_FILE_PATH, 'r'))
    if id in users:
        users.pop(id)
    else:
        print("\tusers.jsonにユーザーが存在しなかったため、削除できませんでした")
    
    if os.path.exists(TASKS_FILE_DIR + id + '.json'):
        json.dump(users, open(USERS_FILE_PATH, 'w'))
        # タスクファイルを削除
        os.remove(TASKS_FILE_DIR + id + '.json')
    else:
        print(f"\t{TASKS_FILE_DIR + id + '.json'}が存在しなかったため、削除できませんでした")
    

if __name__ == '__main__':
    # test
    print(create('test', 'test'))
    print(check('test'))
    print(delete('test'))
    print(check('test'))
    
    pass
    