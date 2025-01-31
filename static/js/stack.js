function convertExpression(conversionType) {
    let expression = document.getElementById("expression").value;
    
    if (!expression.trim()) {
        alert("Please enter an expression!");
        return;
    }

    console.log("Sending expression:", expression, "Conversion type:", conversionType); // Debug log

    // Optionally, show a loading indicator
    let stepsContainer = document.getElementById("steps");
    stepsContainer.innerHTML = "Loading...";  

    fetch("/work2", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ expression: expression, conversion_type: conversionType })
    })
    .then(response => {
        if (!response.ok) {
            return response.json().then(err => { throw new Error(err.message || "Network response was not ok"); });
        }
        return response.json();
    })
    .then(data => {
        console.log("Received data:", data); // Debug log

        // Clear previous steps
        stepsContainer.innerHTML = "";  

        if (data.steps) {
            data.steps.forEach(step => {
                let stepDiv = document.createElement("div");
                stepDiv.className = "steps-container";
                stepDiv.textContent = step;
                stepsContainer.appendChild(stepDiv);
            });
        } else {
            console.error("No steps found in response");
            stepsContainer.innerHTML = "No steps available.";
        }
    })
    .catch(error => {
        console.error("Error:", error);
        stepsContainer.innerHTML = "An error occurred: " + error.message;
    });
}