from flask import Flask, render_template, request,jsonify
from modules import login, userManager
import json

app = Flask(__name__, static_folder='web/static', template_folder='web/templates')
app = Flask(__name__)

#登録ページ
@app.route('/registration', methods=["GET"])
def registration_show(message=None):
    return render_template("create.html", message=message)
#登録ページ
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

    if (result==True): return render_template("todo.html")
    else: return index(message=result)

@app.route('/')
def index():
    return render_template('todo.html')

# タスクの追加時 POST でタスク名、タスク内容、期限を送信する。
@app.route('/add_task', methods=["POST"])
def add_task():
    # リクエストデータをJSON形式で受け取る
    task_data = request.get_json()
    print(task_data)

    with open('todo.json', 'r') as f:
        json_data = json.load(f)

    new_task = {
        "taskId": len(json_data) + 1,  # 新しいタスクIDを生成
        "taskName": task_data["taskName"],
        "taskContent": task_data["taskContent"],
        "taskDeadline": task_data["taskDeadline"]
    }

    json_data.append(new_task)

    with open('todo.json', 'w') as f:
        json.dump(json_data, f, indent=2)

    return jsonify(new_task)


if __name__ == '__main__':
    app.run(debug=True)