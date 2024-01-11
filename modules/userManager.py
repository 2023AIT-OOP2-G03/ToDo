import json

USERS_FILE_PATH = './data/users.json'

# 作成
def create(id, pw):
    if check(id):
        print('ユーザーが存在します')
        return False
    else:
        # users.jsonを読み込み
        users = json.load(open(USERS_FILE_PATH, 'r'))
        # ユーザーを作成
        users[id] = {"pw": pw}
        # users.jsonを書き込み
        json.dump(users, open(USERS_FILE_PATH, 'w'))
        return True

# ユーザーの存在を確認
def check(id):
    # users.jsonを読み込み
    users = json.load(open(USERS_FILE_PATH, 'r'))
    # ユーザーの存在を確認
    if id in users:
        return True
    else:
        return False

if __name__ == '__main__':
    # test
    print(create('test', 'test'))
    print(check('test'))
    