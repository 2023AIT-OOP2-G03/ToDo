# Task Flower

## 概要
アカウントごとに管理されたカレンダーで確認できるToDoリスト

主な機能は2つあり
- ToDoリストに追加されたタスクに役職をつけることで、今やらなくていいタスクはカレンダーに非表示にすることで見やすくなっている。
- アカウント処理されていることで、大人数でも使用することができる。

## Initial Setting

```zsh
$ git clone https://github.com/2023AIT-OOP2-G03/ToDo.git
$ cd ToDo
$ python -m venv .env
$ source .env/bin/activate
(.env) $ pip install -r requirements.txt
```

## Require

- Python version : 3.10 or higher

## Usage

```zsh
$ source .env/bin/activate
(.env) $ python main.py
```