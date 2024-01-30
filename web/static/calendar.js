let user = document.querySelector('#username').textContent
//let tasklist = document.querySelector('#taskList')
let formdata = new FormData()
formdata.append("user", user)

// request json data from server
fetch("/calender", {
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

function parseDateWithReplace(inputDate) {
    // "/"と空白と時刻部分を削除
    const formattedDate = inputDate.replace(/[\/\s:]/g, '').substring(0, 8);

    return formattedDate;
}

function createTaskListItem(data) {
    keys = Object.keys(data)
    limitDate = parseDateWithReplace(datas.timeLimit);
    let dateId = document.getElementById(limitDate);
    
    // loop for each task
    for (i = 0; i < keys.length; i++) {
        let datas = Object.values(data)[i]  // from JSON
        // console.log("--------------------")
        // console.log("key : " + keys[i])
        // console.log(datas.name)
        // console.log(datas.description)
        // console.log(datas.status)
        // console.log(datas.timeLimit)
        listItem = document.createElement('li');
        listItem.className = 'taskItem';

        // ラベルたぶんいらない
        // // タスクラベル
        // taskLabel = document.createElement('label');
        // taskLabel.textContent = 'タスク:';
        // taskLabel.setAttribute('class', 'taskLabel_js');
        // listItem.appendChild(taskLabel);
        // タスク名
        taskText = document.createElement('span');
        taskText.textContent = datas.name;
        taskText.setAttribute('class', 'task_js')
        listItem.appendChild(taskText);
        // 見た目を整える用
        taskBreak = document.createElement('br');
        listItem.appendChild(taskBreak);

        // タスク内容ラベル
        taskLabel = document.createElement('label');
        taskLabel.textContent = '内容:';
        taskLabel.setAttribute('class', 'contentLabel_js');
        listItem.appendChild(taskLabel);
        // タスク内容
        contentText = document.createElement('span');
        contentText.textContent = datas.description;
        contentText.setAttribute('class', 'content_js')
        listItem.appendChild(contentText);
        // 見た目を整える用
        taskBreak = document.createElement('br');
        listItem.appendChild(taskBreak);

        // 期限ラベル
        taskLabel = document.createElement('label');
        taskLabel.textContent = '期限:';
        taskLabel.setAttribute('class', 'deadlineLabel_js');
        listItem.appendChild(taskLabel);
        // 期限
        deadlineText = document.createElement('span');
        deadlineText.textContent = datas.timeLimit;
        deadlineText.setAttribute('class', 'deadline_js')
        listItem.appendChild(deadlineText);

        // 状態
        statusSelect = document.createElement('select');
        statusSelect.setAttribute('id', keys[i]);
        statusSelect.setAttribute('class', 'status_js');

        for (j = 0; j < 4; j++) {
            statusText = document.createElement('option');
            statusText.textContent = changeTaskStatus(j);
            statusText.setAttribute('value', j);
            if (j == changeTaskStatus(datas.status)) statusText.setAttribute('selected', '');
            statusSelect.appendChild(statusText);
        }

        listItem.appendChild(statusSelect);

        // 見た目を整える用
        taskBreak = document.createElement('br');
        listItem.appendChild(taskBreak);

        tasklist.appendChild(listItem);
        // tmp[i].setAttribute("id", str + i)
    }
}
