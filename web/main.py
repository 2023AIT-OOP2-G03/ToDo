from flask import Flask, render_template, request
from modules import user

app = Flask(__name__)


#ログインページ
@app.route('/')
def index():
    return render_template("addressbook.html")

#ログインページ
@app.route('/')
def index():
    return render_template("addressbook.html")

if __name__ == '__main__':
    app.run(debug=True)