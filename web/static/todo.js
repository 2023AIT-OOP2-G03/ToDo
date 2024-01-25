let user = document.querySelector('#username').textContent
let tasklist = document.querySelector('#taskList')
let formdata = new FormData()
formdata.append("user", user)

fetch("/todo", {
    method: "POST",
    body: formdata
}).then(response => response.json())
    .then(data => {
        // サーバーからの応答を処理
        createTaskListItem(data)
    })
    .catch(error => {
        console.error('エラー:', error);
    });

function addTask() {
    taskInput = document.getElementById('taskInput'); //タスクの名前
    taskContent = document.getElementById('taskContent');  //タスクの内容
    taskDeadline = document.getElementById('taskDeadline'); //タスクの期限
    taskStatus = document.getElementById('taskStatus'); //タスクの状態

    if (taskInput.value.trim() !== '' && taskDeadline.value !== '') {
        formdata = new FormData()
        formdata.append("user", user) //ユーザーネーム
        formdata.append("task_name", taskInput.value) //タスクの名前
        formdata.append("task", taskContent.value) //タスクの内容
        formdata.append("task_date", taskDeadline.value) //タスクの期限
        formdata.append("task_status", taskStatus.value) //タスクの状態

        // タスクの追加をサーバーに送信
        fetch('/add', {
            method: "POST",
            body: formdata
        }).then(response => response.json())
            .then(data => {
                // サーバーからの応答を処理
                console.log('サーバーからの応答:', data);

                createTaskListItem(data)

                // 入力欄を空にする
                taskInput.value = '';
                taskContent.value = '';
                taskDeadline.value = '';
            })
            .catch(error => {
                console.error('エラー:', error);
            });
    }
}

function delTask(taskID) {
    result = window.confirm("削除しますか？")
    if (result == false) return;
    formdata = new FormData()
    formdata.append("user", user) //ユーザーネーム
    formdata.append("task_id", taskID) //タスクのID

    // タスクの追加をサーバーに送信
    fetch('/delete', {
        method: "POST",
        body: formdata
    }).then(response => response.json())
        .then(data => {
            // サーバーからの応答を処理
            console.log('サーバーからの応答:', data);

            createTaskListItem(data)
        })
        .catch(error => {
            console.error('エラー:', error);
        });
}

function changeStatus(taskID) {
    taskStatus = document.getElementById(taskID); //タスクの状態
    formdata = new FormData()
    formdata.append("user", user) //ユーザーネーム
    formdata.append("task_id", taskID) //タスクのID
    formdata.append("task_status", taskStatus.value) //タスクの状態

    // タスクの変更をサーバーに送信
    fetch('/change', {
        method: "POST",
        body: formdata
    }).then(response => response.json())
        .then(data => {
            // サーバーからの応答を処理
            console.log('サーバーからの応答:', data);

            createTaskListItem(data)
        })
        .catch(error => {
            console.error('エラー:', error);
        });
}

function changeTaskStatus(Status) {
    if (typeof(Status) == "string") {
        if (Status == "not ready") return 0;
        else if (Status == "ready") return 1;
        else if (Status == "doing") return 2;
        else if (Status == "done") return 3;
    }
    else {
        if (Status == 0) return "準備中";
        else if (Status == 1) return "準備完了";
        else if (Status == 2) return "実行中";
        else if (Status == 3) return "完了";
    }
}

function createTaskListItem(data) {
    // 子要素を全削除
    while (tasklist.firstChild) {
        tasklist.removeChild(tasklist.firstChild)
    }

    // const str = "strID"
    // const tmp = document.getElementById('span').innerHTML
    keys = Object.keys(data)
    for (i = 0; i < keys.length; i++) {
        datas = Object.values(data)[i]
        // console.log("--------------------")
        // console.log("key : " + keys[i])
        // console.log(datas.name)
        // console.log(datas.description)
        // console.log(datas.status)
        // console.log(datas.timeLimit)
        listItem = document.createElement('li');
        listItem.className = 'taskItem';
        // タスク名
        taskText = document.createElement('span');
        taskText.textContent = datas.name;
        listItem.appendChild(taskText);

        // タスク内容
        contentText = document.createElement('span');
        contentText.textContent = datas.description;
        listItem.appendChild(contentText);

        // 期限
        deadlineText = document.createElement('span');
        deadlineText.textContent = datas.timeLimit;
        listItem.appendChild(deadlineText);

        // 状態
        statusSelect = document.createElement('select');
        statusSelect.setAttribute('id', keys[i]);
        statusSelect.setAttribute('class', 'taskStatus');

        for (j = 0; j < 4; j++) {
            statusText = document.createElement('option');
            statusText.textContent = changeTaskStatus(j);
            statusText.setAttribute('value', j);
            if (j == changeTaskStatus(datas.status)) statusText.setAttribute('selected','');
            statusSelect.appendChild(statusText);
        }

        listItem.appendChild(statusSelect);

        // 変更ボタン
        changeButton = document.createElement('button');
        changeButton.textContent = '変更';
        changeButton.className = 'changeButton';
        changeButton.setAttribute('onclick', 'changeStatus("' + keys[i] + '")')
        listItem.appendChild(changeButton);

        // 削除ボタン
        deleteButton = document.createElement('button');
        deleteButton.textContent = '削除';
        deleteButton.className = 'deleteButton';
        deleteButton.setAttribute('onclick', 'delTask("' + keys[i] + '")')
        listItem.appendChild(deleteButton);

        tasklist.appendChild(listItem);
        // tmp[i].setAttribute("id", str + i)
    }
}