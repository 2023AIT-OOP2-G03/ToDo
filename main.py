from flask import Flask, render_template, request
from modules import userManager

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
def index():
    return render_template("login.html")
@app.route('/', methods=["POST"])
def login():
    username = request.form.get('user', None)
    password = request.form.get('pw', None)
    print(username, password)
    return render_template("login.html", message="ロ了")

if __name__ == '__main__':
    app.run(debug=True)