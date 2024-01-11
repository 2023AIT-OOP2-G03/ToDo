import json

# 作成
def create(id, pw):
    if check(id):
        print('ユーザーが存在します')
        return False
    else:
        # users.jsonを読み込み
        users = json.load(open('users.json', 'r'))
        # ユーザーを作成
        users[id]["pass"] = pw
        # users.jsonを書き込み
        json.dump(users, open('users.json', 'w'))
        return True

# ユーザーの存在を確認
def check(id):
    # users.jsonを読み込み
    users = json.load(open('users.json', 'r'))
    # ユーザーの存在を確認
    if id in users:
        return True
    else:
        return False

if __name__ == '__main__':
    # ユーザーの存在を確認
    print(check('test'))