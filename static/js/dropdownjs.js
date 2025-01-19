const selected1 = document.querySelector(".selected1");
const selected2 = document.querySelector(".selected2");
const optionsContainer1 = document.querySelector(".options-container1");
const optionsContainer2 = document.querySelector(".options-container2");
const optionsList1 = document.querySelectorAll(".option1");
const optionsList2 = document.querySelectorAll(".option2");
const arrow1 = document.querySelector("#arrow1");
const arrow2 = document.querySelector("#arrow2");

// Function to toggle dropdown
function toggleDropdown(selected, optionsContainer, arrow) {
    selected.style.backgroundColor = "var(--dark)";
    optionsContainer.classList.toggle("active");
    if (arrow.classList.contains("fa-arrow-down")) {
        arrow.classList.remove("fa-arrow-down");
        arrow.classList.add("fa-arrow-up");
    } else {
        arrow.classList.remove("fa-arrow-up");
        arrow.classList.add("fa-arrow-down");
    }
}

// Event listeners for the first dropdown
selected1.onfocus = () => toggleDropdown(selected1, optionsContainer1, arrow1);
selected1.onblur = () => {
    selected1.style.backgroundColor = "initial";
    optionsContainer1.classList.remove("active");
    arrow1.classList.remove("fa-arrow-up");
    arrow1.classList.add("fa-arrow-down");
};

// Select element from the first dropdown list
optionsList1.forEach(item => {
    item.onclick = () => {
        selected1.placeholder = item.innerText;
        optionsContainer1.classList.remove("active");
        arrow1.classList.remove("fa-arrow-up");
        arrow1.classList.add("fa-arrow-down");
    };
});

// Event listeners for the second dropdown
selected2.onfocus = () => toggleDropdown(selected2, optionsContainer2, arrow2);
selected2.onblur = () => {
    selected2.style.backgroundColor = "initial";
    optionsContainer2.classList.remove("active");
    arrow2.classList.remove("fa-arrow-up");
    arrow2.classList.add("fa-arrow-down");
};

// Select element from the second dropdown list
optionsList2.forEach(item => {
    item.onclick = () => {
        selected2.placeholder = item.innerText;
        optionsContainer2.classList.remove("active");
        arrow2.classList.remove("fa-arrow-up");
        arrow2.classList.add("fa-arrow-down");
    };
});