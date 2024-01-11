import json
import hashlib

import userManager

USERS_FILE_PATH = './data/users.json'

# 認証
def login(id, pw):
    # users.jsonを読み込み
    users = json.load(open(USERS_FILE_PATH, 'r'))
    # ユーザーの存在を確認
    if userManager.check(id):
        # パスワードの確認
        if users[id]['pw'] == pw:
            return True
        else:
            return "ログインに失敗しました。パスワードが違います。"
    else:
        return "ログインに失敗しました。ユーザーが存在しません。"

if __name__ == '__main__':
    # test
    print(login('test', 'test'))
    print(login('test', 'test2'))
    print(login('test2', 'test'))
    
    pass