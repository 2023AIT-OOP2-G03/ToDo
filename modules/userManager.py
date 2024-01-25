import json
import hashlib
import os

USERS_DIR = './data/users/'

LOGIN_TOKEN_FILE_PATH = './data/login_tokens.json'

# 作成
def create(id, pw):
    """ユーザーを作成する
    
    args:
        id (str): ユーザーID
        pw (str): パスワード
    returns:
        bool: True(ユーザー作成成功時)
        int: 0(ユーザー作成失敗時)
    """
    if check(id):
        return "既にユーザーが存在します"
    else:
        # ユーザーを作成
        # パスワードをハッシュ化
        hashed_pw = get_digest(pw)
        
        user = {
            "pw": hashed_pw,
            "tasks": {}
        }
        
        # ユーザーのタスクファイルを作成
        tasks_file_path = USERS_DIR + id + '.json'
        json.dump(user, open(tasks_file_path, 'w'), indent = 4)

        return True

# ユーザーの存在を確認
def check(id):
    """ユーザーの存在を確認する
    
    args:
        id (str): ユーザーID
    returns:
        bool: ユーザーの存在(True: 存在する, False: 存在しない)
    """
    # タスクファイルの存在を確認
    flag_tasks = os.path.exists(USERS_DIR + id + '.json')
    
    # ユーザーの存在を確認
    if flag_tasks:
        return True
    else:
        return False
    
def get_digest(pw):
    """文字列をハッシュ化する
    
    args:
        pw (str): ハッシュ化したい文字列
    returns:
        str: ハッシュ化された文字列
    """
    # SHA256でハッシュ化
    hashed_pw = hashlib.sha256(pw.encode("utf-8")).hexdigest()
    return hashed_pw

def delete(id):
    """ユーザーを削除する
    
    args:
        id (str): ユーザーID
    """
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
    """ユーザーのハッシュ化されたパスワードを取得する
    
    args:
        id (str): ユーザーID
    returns:
        str: ハッシュ化されたパスワード
    """
    if check(id):
        # ユーザーのタスクファイルを読み込み
        tasks_file_path = USERS_DIR + id + '.json'
        user = json.load(open(tasks_file_path, 'r'))
        return user['pw']
    else:
        return None
    
def set_loginToken(id, loginToken):
    """ユーザーのログイントークンを設定する
    
    args:
        id (str): ユーザーID
        loginToken (str): ログイントークン
    """
    if check(id):
        # ログイントークンを設定
        loginToken_file_path = LOGIN_TOKEN_FILE_PATH
        loginTokens = json.load(open(loginToken_file_path, 'r'))
        loginTokens[id] = loginToken
        json.dump(loginTokens, open(loginToken_file_path, 'w'), indent = 4)
    else:
        print("ユーザーが存在しません")

def get_loginToken(id):
    """ユーザーのログイントークンを取得する
    
    args:
        id (str): ユーザーID
    returns:
        str: ログイントークン
    """
    if check(id):
        # ログイントークンを取得
        loginToken_file_path = LOGIN_TOKEN_FILE_PATH
        loginTokens = json.load(open(loginToken_file_path, 'r'))
        return loginTokens[id]
    else:
        return None

if __name__ == '__main__':
    # test
    # print(create('test', 'test'))
    # print(check('test'))
    # # print(delete('test'))
    # print(check('test'))
    # set_loginToken('test', 'hypertest')
    # print(get_loginToken('test'))
    pass