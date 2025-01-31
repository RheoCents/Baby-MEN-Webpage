let array = [];
        const arrayContainer = document.getElementById('array');
        const iterationDisplay = document.getElementById('iterationDisplay');
        const historyDisplay = document.getElementById('history');

        function randomizeArray() {
            const numBars = Math.floor(Math.random() * 10) + 5; 
            array = Array.from({ length: numBars }, () => Math.floor(Math.random() * 10) + 1); 
            createBars();
        }

        function createBars() {
            arrayContainer.innerHTML = '';
            array.forEach(value => {
                const bar = document.createElement('div');
                bar.className = 'bar';
                bar.style.height = `${value * 30}px`; 

                // Create a span to show the value
                const barValue = document.createElement('span');
                barValue.className = 'bar-value';
                barValue.innerText = value; // Set the value of the bar

                bar.appendChild(barValue); // Append the value to the bar
                arrayContainer.appendChild(bar);
            });
        }

        async function startBubbleSort() {
            const n = array.length;
            const bars = document.querySelectorAll('.bar');

            for (let i = 0; i < n - 1; i++) {
                for (let j = 0; j < n - i - 1; j++) {
                    // Highlight the bars being compared
                    bars[j].style.backgroundColor = 'red';
                    bars[j + 1].style.backgroundColor = 'red';

                    await new Promise(resolve => setTimeout(resolve, 500)); // Pause for visualization

                    // Swap if the current element is greater than the next
                    if (array[j] > array[j + 1]) {
                        [array[j], array[j + 1]] = [array[j + 1], array[j]];
                        bars[j].style.height = `${array[j] * 30}px`;
                        bars[j + 1].style.height = `${array[j + 1] * 30}px`;

                        // Update the displayed values
                        bars[j].querySelector('.bar-value').innerText = array[j];
                        bars[j + 1].querySelector('.bar-value').innerText = array[j + 1];
                    }

                    // Reset the color of the bars
                    bars[j].style.backgroundColor = 'teal';
                    bars[j + 1].style.backgroundColor = 'teal';
                }
                bars[n - i - 1].classList.add('sorted'); // Mark the last element as sorted

                // Display the current state of the array after each outer loop iteration
                iterationDisplay.innerText = `Iteration ${i + 1}: [${array.join(', ')}]`;
                
                // Append the current state to the history
                const historyItem = document.createElement('div');
                historyItem.innerText = `Iteration ${i + 1}: [${array.join(', ')}]`;
                historyDisplay.appendChild(historyItem);
            }
            bars[0].classList.add('sorted'); // Mark the first element as sorted
        }
        

    async function selectionSort() {
        const bars = document.querySelectorAll('.bar');
        const n = array.length;

        for (let i = 0; i < n - 1; i++) {
            let minIndex = i;
            bars[minIndex].style.backgroundColor = 'red'; // Highlight the current minimum

            for (let j = i + 1; j < n; j++) {
                bars[j].style.backgroundColor = 'red'; // Highlight the current bar being compared

                await new Promise(resolve => setTimeout(resolve, 500));

                if (array[j] < array[minIndex]) {
                    if (minIndex !== i) {
                        bars[minIndex].style.backgroundColor = 'teal'; // Reset previous minimum
                    }
                    minIndex = j; // Update the minimum index
                } else {
                    bars[j].style.backgroundColor = 'teal'; // Reset the current bar
                }
            }

            // Swap the found minimum element with the first element
            if (minIndex !== i) {
                [array[i], array[minIndex]] = [array[minIndex], array[i]];
                bars[i].style.height = `${array[i] * 30}px`;
                bars[minIndex].style.height = `${array[minIndex] * 30}px`;
            }

            bars[i].style.backgroundColor = 'green'; // Mark the sorted element
        }
        bars[n - 1].style.backgroundColor = 'green'; // Mark the last element as sorted
    }

    function startBubbleSort() {
        bubbleSort();
    }

    function startSelectionSort() {
        selectionSort();
    }

    randomizeArray();