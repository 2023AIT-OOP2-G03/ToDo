from flask import Flask, render_template, request
from modules import login, userManager

app = Flask(__name__, static_folder='web/static', template_folder='web/templates')

#登録ページ
@app.route('/registration', methods=["GET"])
def registration_show():
    return render_template("create.html", message="waegrhtjyfu")
#登録ページ
@app.route('/registration', methods=["POST"])
def registration():
    username = request.form.get('user', None)
    password = request.form.get('pw', None)
    result = userManager.create(username, password)
    if (result==True):
        return render_template("login.html", message="登録完了しました")
    else:
        return render_template("create.html", message=result)

#ログインページ
@app.route('/', methods=["GET"])
def index(message=None):
    return render_template("login.html", message=message)
@app.route('/', methods=["POST"])
def login_():
    username = request.form.get('user', None)
    password = request.form.get('pw', None)
    # if (username==None and password==None):
    #     print("username or password is None")
        # return index()
    result = login.login(username, password)
    if (result==True):
        return index(message="ログイン完了")
    else:
        return index(message=result)

if __name__ == '__main__':
    app.run(debug=True)