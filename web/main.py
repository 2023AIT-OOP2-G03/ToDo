from flask import Flask, render_template, request
from modules import user

app = Flask(__name__)


#登録ページ
@app.route('/registration')
def index():
    return render_template("addressbook.html")

#ログインページ
@app.route('/')
def index():
    return render_template("test.html")

if __name__ == '__main__':
    app.run(debug=True)