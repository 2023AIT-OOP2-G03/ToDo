const formdata = new FormData()
fn = document.querySelector('#user').textContent
formdata.append("user", fn)
console.log(fn)

fetch("/todo", {
    method: "POST",
    body: formdata
}).then(response => response.json())
.then(data => {
    // サーバーからの応答を処理
    console.log(typeof(data))
})
.catch(error => {
    console.error('エラー:', error);
});

function addTask() {
    var taskInput = document.getElementById('taskInput');
    var taskContent = document.getElementById('taskContent');
    var taskDeadline = document.getElementById('taskDeadline');

    if (taskInput.value.trim() !== '' && taskDeadline.value !== '') {
        // タスクオブジェクトを作成
        var taskData = {
            taskName: taskInput.value,
            taskContent: taskContent.value,
            taskDeadline: taskDeadline.value
        };

        // タスクの追加をサーバーに送信
        fetch('/add_task', {
            
            body: JSON.stringify(taskData),
        })
        .then(response => response.json())
        .then(data => {
            // サーバーからの応答を処理
            console.log('サーバーからの応答:', data);

            // タスクを表示する処理を追加
            var taskList = document.getElementById('taskList');
            var listItem = createTaskListItem(data);
            insertTaskInOrder(listItem, taskList);

            // 入力フィールドをクリア
            taskInput.value = '';
            taskContent.value = '';
            taskDeadline.value = '';
        })
        .catch(error => {
            console.error('エラー:', error);
        });
    }
}

function createTaskListItem(taskData) {
    var listItem = document.createElement('li');
    listItem.className = 'taskItem';

    // タスク名
    var taskText = document.createElement('span');
    taskText.textContent = taskData.taskName;
    listItem.appendChild(taskText);

    // タスク内容
    var contentText = document.createElement('span');
    contentText.textContent = taskData.taskContent;
    listItem.appendChild(contentText);

    // 期限
    var deadlineText = document.createElement('span');
    deadlineText.textContent = taskData.taskDeadline;
    listItem.appendChild(deadlineText);

    // 削除ボタン
    var deleteButton = document.createElement('button');
    deleteButton.textContent = '削除';
    deleteButton.className = 'deleteButton';
    deleteButton.addEventListener('click', function () {
        listItem.parentNode.removeChild(listItem);
    });
    listItem.appendChild(deleteButton);

    return listItem;
}

function insertTaskInOrder(newTask, taskList) {
    var taskDate = new Date(newTask.querySelector('span:nth-child(3)').textContent);
    var existingItems = taskList.querySelectorAll('.taskItem');
    var inserted = false;

    existingItems.forEach(function (existingItem) {
        var existingDate = new Date(existingItem.querySelector('span:nth-child(3)').textContent);
        if (taskDate < existingDate) {
            taskList.insertBefore(newTask, existingItem);
            inserted = true;
            return;
        }
    });

    if (!inserted) {
        // 最後に追加
        taskList.appendChild(newTask);
    }
}

