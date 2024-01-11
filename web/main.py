from flask import Flask, render_template, request
from modules import userManager

app = Flask(__name__)


#登録ページ
@app.route('/registration', methods=["GET"])
def registration_show(message=None):
    return render_template("test/test.html", message=message)
#登録ページ
@app.route('/registration', methods=["POST"])
def registration():
    username = request.form.get('user', None)
    password = request.form.get('pw', None)
    # username = "usr"
    # password = "pass"
    result = userManager.create(username, password)
    if result: index("登録完了")
    else: registration_show(result)

#ログインページ
@app.route('/')
def index(message=None):
    return render_template("test.html", message=message)

if __name__ == '__main__':
    app.run(debug=True)