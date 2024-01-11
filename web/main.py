from flask import Flask, render_template, request
#関数名は仮
from modules import temp as regi

app = Flask(__name__)


#登録ページ
@app.route('/registration', methods=["GET"])
def registration_show():
    return render_template("test/test.html")
#登録ページ
@app.route('/registration', methods=["POST"])
def registration():
    username = request.form.get('user', None)
    password = request.form.get('pw', None)
    #関数名は仮
    result = regi.registration(username, password)
    if result: index()
    else: return render_template("registration_failure.html")

#ログインページ
@app.route('/')
def index():
    return render_template("test.html")

if __name__ == '__main__':
    app.run(debug=True)