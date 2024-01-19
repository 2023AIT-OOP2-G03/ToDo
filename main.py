from flask import Flask, render_template, request, jsonify
from modules import login, userManager
from modules.todo import todolistManager, taskManager
from datetime import datetime as dt

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
        return index("登録完了しました")
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
    todo_data = todolistManager.get_tasks(username)

    return jsonify(todo_data)

@app.route('/add', methods=["POST"])
def add_todo():
    username = request.form.get('user', None)
    task_name = request.form.get('task_name', None)
    task = request.form.get('task', None)
    task_date = request.form.get('task_date', None)
    todolistManager.add_task(username, taskManager.task(task_name, task, taskManager.task_status.NOT_READY, dt.strptime(task_date, "%Y-%m-%d")))
    todo_data = todolistManager.get_tasks(username)

    return jsonify(todo_data)

@app.route('/delete', methods=["POST"])
def delete_todo():
    username = request.form.get('user', None)
    task_id = request.form.get('task_id', None)
    todolistManager.delete_task(username, task_id)
    todo_data = todolistManager.get_tasks(username)

    return jsonify(todo_data)


#管理者ページ
@app.route('/admin', methods=["GET"])
def admin(message=None):
    return render_template("login.html", message=message, admin=True)

@app.route('/admin', methods=["POST"])
def login_admin(message=None):
    username = request.form.get('user', None)
    password = request.form.get('pw', None)
    if (username=="admin" and password=="admin"): return render_template("admin.html")
    return admin(message="ログインエラー")

@app.route('/del-admin', methods=["POST"])
def delete_user():
    username = request.form.get('user', None)
    if (userManager.check(username)):
        userManager.delete(username)
        return render_template("admin.html", message="削除完了しました")
    return render_template("admin.html", message="ユーザーが存在しません")

if __name__ == '__main__':
    # app.run(debug=True)
    app.run(debug=False, host='0.0.0.0', port=80)