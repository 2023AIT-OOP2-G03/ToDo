// request json data from server
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