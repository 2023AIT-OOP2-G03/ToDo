from flask import Flask, render_template, request
from modules import login, userManager

app = Flask(__name__, static_folder='web/static', template_folder='web/templates')

#ログインページ
@app.route('/', methods=["GET"])
def index():
    return render_template("login.html")

if __name__ == '__main__':
    app.run(debug=True)