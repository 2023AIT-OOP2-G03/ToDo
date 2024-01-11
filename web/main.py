from flask import Flask, render_template, request
#関数名は仮
from modules import temp as regi

app = Flask(__name__)


#登録ページ
@app.route('/registration', methods=["GET"])
def registration_show(error=None):
    return render_template("test/test.html", error=error)
#登録ページ
@app.route('/registration', methods=["POST"])
def registration():
    username = request.form.get('user', None)
    password = request.form.get('pw', None)
    #関数名は仮
    result = regi.registration(username, password)
    if result: index("登録完了")
    else: registration_show(result)

#ログインページ
@app.route('/')
def index(message=None):
    return render_template("test.html", message=message)

if __name__ == '__main__':
    app.run(debug=True)