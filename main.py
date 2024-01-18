from flask import Flask, render_template, request, jsonify
from modules import login, userManager
import random

app = Flask(__name__, static_folder='web/static', template_folder='web/templates')

#登録ページ
@app.route('/registration', methods=["GET"])
def registration_show(message=None):
    return render_template("create.html", message=message)
@app.route('/registration', methods=["POST"])
def registration():
    username = request.form.get('user', None)
    password = request.form.get('pw', None)
    result = userManager.create(username, password)
    if (result==True):
        return render_template("login.html", message="登録完了しました")
    else:
        return registration_show(result)

#ログインページ
@app.route('/', methods=["GET"])
def index(message=None):
    return render_template("login.html", message=message)
@app.route('/', methods=["POST"])
def login_():
    username = request.form.get('user', None)
    password = request.form.get('pw', None)
    if (username==None and password==None): return index()

    result = login.login(username, password)

    if (result==True): return render_template("todo.html", message=username)
    else: return index(message=result)

#ToDoListページ
@app.route('/todo', methods=["POST"])
def get_todo():
    username = request.form.get('user', None)

    data = "{""}"
    return jsonify(data)
@app.route('/add', methods=["POST"])
def add_todo():
    username = request.form.get('user', None)
    task_name = request.form.get('task_name', None)
    task = request.form.get('task', None)
    task_date = request.form.get('task_date', None)
    task_id = str(int(random.random()*10000))

    data = "{""}"
    return jsonify(data)
@app.route('/delete', methods=["POST"])
def delete_todo():
    username = request.form.get('user', None)
    task_id = request.form.get('task_id', None)

    data = "{""}"
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
