let calendarEl = document.getElementById('calendar');
const date = new Date();
const currentYear = date.getFullYear();
const currentMonth = date.getMonth();

let currentDisplayedMonth = currentMonth;
let currentDisplayedYear = currentYear;

let user = document.querySelector('#username').textContent
let tasklist = document.querySelector('#taskList')
let formdata = new FormData()
formdata.append("user", user)

// 指定された年と月に基づいてカレンダーグリッドを更新する関数
function updateCalendar(year, month) {
    let daysInMonth = new Date(year, month + 1, 0).getDate();
    let calendarHtml = '<table><thead><tr>';
    for (let i = 0; i < 7; i++) {
        calendarHtml += `<th>${['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'][i]}</th>`;
    }
    calendarHtml += '</tr></thead><tbody><tr>';

    for (let i = 1; i <= daysInMonth; i++) {
        const dayOfWeek = new Date(year, month, i).getDay();
        if (i === 1) {
            calendarHtml += '<tr>';
            for (let j = 0; j < dayOfWeek; j++) {
                calendarHtml += '<td></td>';
            }
        }
        let cellId = `d${year}${(month + 1).toString().padStart(2, '0')}${i.toString().padStart(2, '0')}`;
        //TODO: ここにif文を追加して予定があった時のみボタンが出るように書き換える。
        //予定がない時はelse文を用いてその下にコメントアウトしてあるcalendarHtmlに飛ぶようにする。
        calendarHtml += `<td><button class="day-button" onclick="openModal('${cellId}')"><span>${i}</span></button><div id="${cellId}" class="taskTitleCell"></div></td>`;
        //calendarHtml += `<td><span class="font ${i <= daysInMonth ? '' : 'hidden'}">${i}</span><div id="${cellId}" class="taskTitleCell"></div></td>`;                
        if (dayOfWeek === 6) {
            calendarHtml += '</tr>';
            if (i < daysInMonth) {
                calendarHtml += '<tr>';
            }
        } else if (i === daysInMonth) {
            for (let j = dayOfWeek + 1; j <= 6; j++) {
                calendarHtml += '<td></td>';
            }
            calendarHtml += '</tr>';
        }
    }
    calendarHtml += '</tbody></table>';
    calendarEl.innerHTML = calendarHtml;
}

// ヘッダーに表示されている月と年を更新する関数
function updateDisplayedYYYYMM(year, month) {
    document.getElementById('currentDisplayedYYYYMM').innerHTML = `${year}/${(month + 1).toString().padStart(2, '0')}`;
}

// モーダルウィンドウを開く関数
function openModal(cellId) {
    const dateCell = document.getElementById(cellId);
    const tasksData = dateCell.getAttribute('data-tasks');

    const modalContent = document.getElementById('modalContent');
    modalContent.innerHTML = ''; // コンテンツをクリア

    if (tasksData) {
        const tasks = JSON.parse(tasksData);
        tasks.forEach(task => {
            // 各タスクの詳細を追加
            const taskDiv = document.createElement('div');
            taskDiv.innerHTML = `<h3>${task.name}</h3><p>${task.description}</p><p>${task.status}</p>`;
            modalContent.appendChild(taskDiv);
        });
    } else {
        modalContent.innerText = 'この日にはタスクがありません。';
    }

    const modalOverlay = document.getElementById('modalOverlay');
    const modal = document.getElementById('myModal');
    modalOverlay.style.display = 'block';
    modal.style.display = 'block';
}

// モーダルウィンドウを閉じる関数
function closeModal() {
    const modalOverlay = document.getElementById('modalOverlay');
    const modal = document.getElementById('myModal');
    modalOverlay.style.display = 'none';
    modal.style.display = 'none';
}

//前月
function prevClick() {
    currentDisplayedMonth--;
    if (currentDisplayedMonth < 0) {
        currentDisplayedMonth = 11;
        currentDisplayedYear--;
    }
    updateCalendar(currentDisplayedYear, currentDisplayedMonth);
    updateDisplayedYYYYMM(currentDisplayedYear, currentDisplayedMonth);
    fetch("/calender", {
        method: "post",
        body: formdata
    }).then(response => response.json())
        .then(data => {
            // サーバーからの応答を処理
            createTaskListItem(data)
        })
        .catch(error => {
            console.error('エラー:', error);
        });
}

//翌月
function nextClick() {
    currentDisplayedMonth++;
    if (currentDisplayedMonth > 11) {
        currentDisplayedMonth = 0;
        currentDisplayedYear++;
    }
    updateCalendar(currentDisplayedYear, currentDisplayedMonth);
    updateDisplayedYYYYMM(currentDisplayedYear, currentDisplayedMonth);
    fetch("/calender", {
        method: "post",
        body: formdata
    }).then(response => response.json())
        .then(data => {
            // サーバーからの応答を処理
            createTaskListItem(data)
        })
        .catch(error => {
            console.error('エラー:', error);
        });
}

function createTaskListItem(data) {
    const tasksByDate = {};

    // タスクを日付ごとにグループ化
    Object.values(data).forEach(task => {
        const taskDate = new Date(task.timeLimit);
        const cellId = `d${taskDate.getFullYear()}${(taskDate.getMonth() + 1).toString().padStart(2, '0')}${taskDate.getDate().toString().padStart(2, '0')}`;

        if (!tasksByDate[cellId]) {
            tasksByDate[cellId] = [];
        }
        tasksByDate[cellId].push(task);
    });

    // 各日付のセルにタスクのタイトルを追加
    for (const cellId in tasksByDate) {
        const dateCell = document.getElementById(cellId);
        if (dateCell) {
            const tasksDiv = document.createElement('div');
            tasksDiv.className = 'task-list';

            tasksByDate[cellId].forEach(task => {
                const taskTitle = document.createElement('div');
                taskTitle.textContent = task.name;
                taskTitle.className = 'task-title';
                tasksDiv.appendChild(taskTitle);
            });

            dateCell.appendChild(tasksDiv);
            // タスクの詳細情報をセルの属性として格納
            dateCell.setAttribute('data-tasks', JSON.stringify(tasksByDate[cellId]));
        }
    }
}


//ページ読み込み時にカレンダーを表示する
window.onload = function () {
    updateCalendar(currentDisplayedYear, currentDisplayedMonth);
    updateDisplayedYYYYMM(currentDisplayedYear, currentDisplayedMonth);
    let user = document.querySelector('#username').textContent
    //let tasklist = document.querySelector('#taskList')
    let formdata = new FormData()
    formdata.append("user", user)
    
    // request json data from server
    fetch("/calender", {
        method: "post",
        body: formdata
    }).then(response => response.json())
        .then(data => {
            // サーバーからの応答を処理
            createTaskListItem(data)
        })
        .catch(error => {
            console.error('エラー:', error);
        });
};


// "/"と空白と時刻部分を削除する
function parseDateWithReplace(inputDate) {
    const formattedDate = inputDate.replace(/[\/\s:]/g, '').substring(0, 8);

    return formattedDate;
}
