import json
import hashlib

USERS_FILE_PATH = './data/users.json'

# 作成
def create(id, pw):
    if check(id):
        return "ユーザーが存在します"
    else:
        # users.jsonを読み込み
        users = json.load(open(USERS_FILE_PATH, 'r'))
        # ユーザーを作成
        # SHA-256でハッシュ化
        hashed_pw = get_digest(pw)
        users[id] = {"pw": hashed_pw}
        
        # users.jsonを書き込み
        json.dump(users, open(USERS_FILE_PATH, 'w'))
        # TODO なぜか「0」を返している、main.pyを編集してTrueにすべき
        # return True
        return 0

# ユーザーの存在を確認
def check(id):
    # users.jsonを読み込み
    users = json.load(open(USERS_FILE_PATH, 'r'))
    # ユーザーの存在を確認
    if id in users:
        return True
    else:
        return False
    
def get_digest(pw):
    hashed_pw = hashlib.sha256(pw.encode("utf-8")).hexdigest()
    # print(hashed_pw)
    return hashed_pw

if __name__ == '__main__':
    # test
    print(create('test', 'test'))
    print(check('test'))
    
    pass
    