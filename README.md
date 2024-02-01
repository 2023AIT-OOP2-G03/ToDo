# Task Flower

## 概要
アカウントごとに管理されたカレンダーで確認できるToDoリスト

主な機能は2つあり
- ToDoリストに追加されたタスクに状態をつけることで、今やらなくていいタスクはカレンダーで見やすくなっている。
- アカウント処理されていることで、複数人でも使用することができる。

## Initial Setting

```zsh
$ git clone https://github.com/2023AIT-OOP2-G03/ToDo.git
$ cd ToDo
$ pip install -r requirements.txt
```

## Require

- Python version : 3.10 or higher

## Usage

```zsh
$ python main.py
```

## ディレクトリ構造

```
TODO
│
├── data
│     ├── users
│     │      └── {users}.json (ユーザーを管理するjson)
│     └──login_tokens.json (ユーザーごとに振られたトークン)
│
├── modules 
│     ├── todo
│     │      ├── taskManager.py (タスクの管理)
│     │      └── todolistManager.py (タスクの動き)
│     ├── login.py (ログインの動き)
│     └── userManager.py (ユーザー管理)
│   
├── web
│     ├── static
│     │      ├── calendar.css
│     │      ├── calendar.js
│     │      ├── todo.css
│     │      └── todo.js
│     └── templates
│             ├── admin.html
│             ├── calender.html
│             ├── create.html
│             ├── login.html
│             └── todo.html
│           
├── README.md
├── requirements.txt
└── main.py

```