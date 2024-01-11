// Add your JavaScript code here
function addTask() {
    var taskInput = document.getElementById('taskInput');
    var taskList = document.getElementById('taskList');

    if (taskInput.value.trim() !== '') {
        // Create a new list item
        var listItem = document.createElement('li');
        listItem.className = 'taskItem';

        // Create a span for the task text
        var taskText = document.createElement('span');
        taskText.textContent = taskInput.value;
        listItem.appendChild(taskText);

        // Create a button for deleting the task
        var deleteButton = document.createElement('button');
        deleteButton.textContent = 'Delete';
        deleteButton.className = 'deleteButton';
        deleteButton.addEventListener('click', function () {
            taskList.removeChild(listItem);
        });
        listItem.appendChild(deleteButton);

        // Add the list item to the task list
        taskList.appendChild(listItem);

        // Clear the input field
        taskInput.value = '';
    }
}
