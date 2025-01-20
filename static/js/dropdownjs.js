const selected1 = document.querySelector(".selected1");
const selected2 = document.querySelector(".selected2");
const optionsContainer1 = document.querySelector(".options-container1");
const optionsContainer2 = document.querySelector(".options-container2");
const optionsList1 = document.querySelectorAll(".option1");
const optionsList2 = document.querySelectorAll(".option2");

// Function to toggle dropdown
function toggleDropdown(selected, optionsContainer) {
    selected.style.backgroundColor = "var(--dark)";
    optionsContainer.classList.toggle("active");
}

// Event listeners for the first dropdown
selected1.onfocus = () => toggleDropdown(selected1, optionsContainer1);
selected1.onblur = () => {
    selected1.style.backgroundColor = "initial";
    optionsContainer1.classList.remove("active");
};

// Select element from the first dropdown list
optionsList1.forEach(item => {
    item.onclick = () => {
        const selected1 = document.getElementById('start');
        selected1.value = item.innerText; // Set the input value
        selected1.placeholder = item.innerText; // Update the placeholder
        optionsContainer1.classList.remove("active"); // Hide options
    };
});

// Event listeners for the second dropdown
selected2.onfocus = () => toggleDropdown(selected2, optionsContainer2);
selected2.onblur = () => {
    selected2.style.backgroundColor = "initial";
    optionsContainer2.classList.remove("active");
};

// Select element from the second dropdown list
optionsList2.forEach(item => {
    item.onclick = () => {
        const selected2 = document.getElementById('end');
        selected2.value = item.innerText; // Set the input value
        selected2.placeholder = item.innerText; // Update the placeholder
        optionsContainer2.classList.remove("active"); // Hide options
    };
});

// Function to find the path
async function findPath() {
    const start = document.getElementById('start').value; // Gets the value from the start input
    const end = document.getElementById('end').value; // Gets the value from the end input

    console.log("Start:", start, "End:", end); // Log the selected start and end stations

    try {
        const response = await fetch('/work4', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ start, end }) // Sends the selected values to the server
        });

        if (!response.ok) {
            throw new Error('Network response was not ok');
        }

        const paths = await response.json(); // Parse the JSON response
        console.log("Paths received:", paths); // Log the paths received

        const resultDiv = document.getElementById('result');
        resultDiv.innerHTML = ''; // Clear previous results

        if (paths.length > 0) {
            paths.forEach((path, index) => {
                const p = document.createElement('p');
                p.textContent = `Path ${index + 1}: ${path.join(' -> ')}`;
                resultDiv.appendChild(p); // Display each path
            });
        } else {
            resultDiv.textContent = 'No path found.'; // Handle case with no paths
        }
    } catch (error) {
        console.error('Error fetching paths:', error); // Log any errors
        const resultDiv = document.getElementById('result');
        resultDiv.textContent = 'An error occurred while finding the path.'; // Display error message
    }
}