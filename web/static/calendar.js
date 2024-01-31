let calendarEl = document.getElementById('calendar');
const date = new Date();
const currentYear = date.getFullYear();
const currentMonth = date.getMonth();

let currentDisplayedMonth = currentMonth;
let currentDisplayedYear = currentYear;

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
function openModal(date) {
    const modalContent = document.getElementById('modalContent');
    modalContent.innerText = 'ここに予定の内容を入れる';
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



function createTaskListItem(data) {
    let YYYYMMnow = currentDisplayedYear.toString() + (currentDisplayedMonth + 1).toString().padStart(2, '0');
    keys = Object.keys(data)

    // loop for each task
    for (i = 0; i < keys.length; i++) {
        let datas = Object.values(data)[i]  // from JSON
        let limitDate = parseDateWithReplace(datas.timeLimit);
        let getId = 'd' + limitDate;
        let dateId = document.getElementById(getId);
        
        console.log("--------------------");
        console.log("key : " + keys[i]);
        console.log(datas.name);
        console.log(datas.description);
        console.log(datas.status);
        console.log(datas.timeLimit);

        console.log("YYYYMMnow : " + YYYYMMnow);
        console.log("limitDate : " + limitDate);
        console.log("limitDate.substring(0, 6) : " + limitDate.substring(0, 6));
        console.log("getId : " + getId);
        console.log("dateId : " + dateId);

        // Loop through each element with the specified class
        Array.from(dateId).forEach(dateId => {
            dateId.innerHTML = limitDate;

        if (YYYYMMnow == limitDate.substring(0, 6)) {
            let listHTML = '<p>'   // 文字列連結先
            //listItem.className = 'taskItem';
            listHTML += `${datas.name}</p></br>`;    // タスク名

            // ラベルたぶんいらない
            // // タスクラベル
            // taskLabel = document.createElement('label');
            // taskLabel.textContent = 'タスク:';
            // taskLabel.setAttribute('class', 'taskLabel_js');
            // listItem.appendChild(taskLabel);
            // タスク名
            /* taskText = document.createElement('span');
            taskText.textContent = datas.name;
            taskText.setAttribute('class', 'task_js')
            listItem.appendChild(taskText);
            // 見た目を整える用
            taskBreak = document.createElement('br');
            listItem.appendChild(taskBreak);

            console.log("listItem : " + listItem); */

           /*  // タスク内容ラベル
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
            listItem.appendChild(taskBreak); */

            //dateId.appendChild(listItem);

            //dateId.innerHTML += listHTML;
            console.log("listHTML : " + listHTML);
        }
    });

    // document.getElementById('displayedYYYYMM').innerHTML + 'aaaaa';
    }
}

// "/"と空白と時刻部分を削除する
function parseDateWithReplace(inputDate) {
    const formattedDate = inputDate.replace(/[\/\s:]/g, '').substring(0, 8);

    return formattedDate;
}
