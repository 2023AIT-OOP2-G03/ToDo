import json
import hashlib
import os

USERS_DIR = './data/users/'

# 作成
def create(id, pw):
    if check(id):
        return "ユーザーが存在します"
    else:
        # ユーザーを作成
        # パスワードをハッシュ化
        hashed_pw = get_digest(pw)
        
        user = {
            "pw": hashed_pw,
            "tasks": []
        }
        
        # ユーザーのタスクファイルを作成
        tasks_file_path = USERS_DIR + id + '.json'
        json.dump(user, open(tasks_file_path, 'w'))
        
        # TODO: なぜか「0」を返している、main.pyを編集してTrueにすべき
        # return True
        return 0

# ユーザーの存在を確認
def check(id):
    # タスクファイルの存在を確認
    flag_tasks = os.path.exists(USERS_DIR + id + '.json')
    
    # ユーザーの存在を確認
    if flag_tasks:
        return True
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
        print("ユーザーが存在しません")

def __force_delete(id):
    if os.path.exists(USERS_DIR + id + '.json'):
        # タスクファイルを削除
        os.remove(USERS_DIR + id + '.json')
    else:
        print(f"\t{USERS_DIR + id + '.json'}が存在しなかったため、削除できませんでした")

def get_pw(id):
    if check(id):
        # ユーザーのタスクファイルを読み込み
        tasks_file_path = USERS_DIR + id + '.json'
        user = json.load(open(tasks_file_path, 'r'))
        return user['pw']
    else:
        return None
    

if __name__ == '__main__':
    # test
    print(create('test', 'test'))
    print(check('test'))
    # print(delete('test'))
    print(check('test'))