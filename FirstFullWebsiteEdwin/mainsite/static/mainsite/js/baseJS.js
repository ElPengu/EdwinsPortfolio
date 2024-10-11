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

/*To unhide all elements in a table when the table 
is clicked, typically for editing the table*/
function editingMode(tableDivByID) {

    /**Get parent div from argument */
    const tableDiv = document.getElementById(tableDivByID);

    /**Get all elements with class 'hidden' and 'unhidden' in tableDiv*/
    const hiddenElements = tableDiv.getElementsByClassName('hidden');
    const unhiddenElements = tableDiv.getElementsByClassName('unhidden');
    

    const unhiddenElementsCount = unhiddenElements.length;
    const hiddenElementsCount = hiddenElements.length;

    /**If no unhidden elements, convert all to hidden 
     * to unhidden! */
    if (unhiddenElementsCount === 0 ||
        unhiddenElementsCount <= hiddenElementsCount
    ) {
        /**Change inner html */
        document.getElementById("editModeToDoListTable")
        .innerHTML = "Exit editing mode";

        /*Now switch all hidden to unhidden*/
        for (let i = hiddenElementsCount-1; i >= 0; i--) {
            hiddenElements[i].className = 'unhidden';
        }
    }
    /**Else if no hidden elements, convert all unhidden 
     * to hidden
    */
    else if (hiddenElementsCount === 0 || 
        hiddenElementsCount <= unhiddenElementsCount) {
        /**Change inner html */
        document.getElementById("editModeToDoListTable")
        .innerHTML = "Enter editing mode";
        
            /*Now switch all unhidden to hidden*/
        for (let i = unhiddenElementsCount-1; i>=0; i--) {
            unhiddenElements[i].className = 'hidden';
        }
    }
}