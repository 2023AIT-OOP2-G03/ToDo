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
                let cellId = `${year}${(month + 1).toString().padStart(2, '0')}${i.toString().padStart(2, '0')}`;
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

        window.onload = function() {
            updateCalendar(currentDisplayedYear, currentDisplayedMonth);
            updateDisplayedYYYYMM(currentDisplayedYear, currentDisplayedMonth);
        };