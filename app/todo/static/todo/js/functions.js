function ProfileMenu(){
    document.getElementById("dropdown-block").classList.toggle("show");
}

function AddTask(){
    task = document.getElementById("add-task-block-form");
    task_name = task.querySelector("#id_name");
    task_text = task.querySelector("#id_text");
    task_name.value = '';
    task_text.value = '';
    document.getElementById("add-task-button-prev").classList.toggle("hidden");
    document.getElementById("add-task-block-form").classList.toggle("hidden");
}

function EditTask(task_id, name, text) {
    document.getElementById(`task-text-block-${task_id}`).classList.toggle("hidden");
    let task = document.getElementById(`task-edit-block-${task_id}`);
    task.classList.toggle("hidden");
    let task_name = task.querySelector('#id_name');
    let task_text = task.querySelector('#id_text');
    task_name.value = name;
    task_text.value = text;
}

function EditTaskCancel(task_id) {
    document.getElementById(`task-text-block-${task_id}`).classList.toggle("hidden");
    document.getElementById(`task-edit-block-${task_id}`).classList.toggle("hidden");
}

function InsertValues(task_id) {
    console.log("ONLOAD");
    // let task = document.getElementById(`task-edit-block-${task_id}`);
    // let task_name = task.querySelector('id_name');
    // task_name.value = "PIVO";
}

function SelectDay(day_number) {
    document.getElementsByClassName("selected-day")[0].classList.toggle("selected-day");
    document.getElementById(`day-${day_number}`).classList.toggle("selected-day");
}

function PreSelectDay(day) {
    console.log(day);
}

window.onclick = function(event) {
    if (!event.target.matches('.profile-name')) {
        var block = document.getElementById("dropdown-block");
        if (block.classList.contains("show")) {
            block.classList.remove("show");
        }
    }
}

