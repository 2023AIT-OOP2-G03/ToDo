from flask import Flask, render_template, request
from modules import userManager

app = Flask(__name__, static_folder='web/static', template_folder='web/templates')

#登録ページ
@app.route('/registration', methods=["GET"])
def registration_show():
    return render_template("touroku.html", message="waegrhtjyfu")
#登録ページ
@app.route('/registration', methods=["POST"])
def registration():
    username = request.form.get('user', None)
    password = request.form.get('pw', None)
    result = userManager.create(username, password)
    print ("--------")
    print (result)
    print ("--------")
    if (result==0):
        return render_template("temp.html", message="登録完了")
    else:
        return render_template("touroku.html", message=result)

#ログインページ
@app.route('/', methods=["GET"])
def index():
    return render_template("temp.html")
@app.route('/', methods=["POST"])
def login():
    return render_template("temp.html", message="ロ了")

if __name__ == '__main__':
    app.run(debug=False)