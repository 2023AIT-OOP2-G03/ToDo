import json

import userManager

# 認証
def login(id, pw):
    """ログイン機能
    
    ログインの成功・失敗を判定する。
    失敗時はエラーメッセージを返す
    
    Args:
        id (str): ユーザーID
        pw (str): パスワード
    Returns:
        bool: True(ログイン成功時)
        str: エラーメッセージ(ログイン失敗時)
    """
    # ユーザーの存在を確認
    if userManager.check(id):
        # パスワードの確認
        if userManager.get_pw(id) == userManager.get_digest(pw):
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