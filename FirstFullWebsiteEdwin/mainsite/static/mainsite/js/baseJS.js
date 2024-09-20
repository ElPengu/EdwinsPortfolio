//Lets user confirm some action
function checker(event) {
    var result = confirm('Are you sure?');
    if (result == false) {
        event.preventDefault();
    }
}


function languageSwitch() {
    // Get the button element
    var button = document.getElementById("languageSwitch");
    // Check the current language and toggle
    if (button.innerHTML.trim() === "English") {
        button.innerHTML = "Kiswahili";
    } else if (button.innerHTML.trim() === "Kiswahili") {
        button.innerHTML = "English";
    }
}

var button = document.getElementById("myButton");

var buttonText = button.textContent.trim();

button.innerHTML = "";

button.textContent = buttonText;


function editTodolistitem() {
    // Get the element
    const elementEditToDoListItems = document.getElementById("EditToDoListItems");
    const elementStopEditing = document.getElementById("StopEditing")

    // Get computed styles
    const computedStyleEditToDoListItems = window.getComputedStyle(elementEditToDoListItems);
    const computedStyleStopEditing = window.getComputedStyle(elementStopEditing);

    const displayValueEditToDoListItems = computedStyleEditToDoListItems.display;
    const displayValueStopEditing = computedStyleStopEditing.display;
    
    // Toggle display
    if (displayValueEditToDoListItems === "none") {
        elementEditToDoListItems.style.display = "block";
        elementStopEditing.style.display = "block";
    } else {
        elementEditToDoListItems.style.display = "none";
        elementStopEditing.style.display = "none";
    }
    
}