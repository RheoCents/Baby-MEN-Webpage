let array = [];
    const arrayContainer = document.getElementById('array');

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
            arrayContainer.appendChild(bar);
        });
    }

    async function bubbleSort() {
        const bars = document.querySelectorAll('.bar');
        const n = array.length;

        for (let i = 0; i < n - 1; i++) {
            for (let j = 0; j < n - i - 1; j++) {
                bars[j].style.backgroundColor = 'red';
                bars[j + 1].style.backgroundColor = 'red';

                await new Promise(resolve => setTimeout(resolve, 500));

                if (array[j] > array[j + 1]) {
                    [array[j], array[j + 1]] = [array[j + 1], array[j]];
                    bars[j].style.height = `${array[j] * 30}px`;
                    bars[j + 1].style.height = `${array[j + 1] * 30}px`;
                }

                bars[j].style.backgroundColor = 'teal';
                bars[j + 1].style.backgroundColor = 'teal';
            }
            bars[n - i - 1].classList.add('sorted');
        }
        bars[0].classList.add('sorted');
    }

    function startBubbleSort() {
        bubbleSort();
    }
    randomizeArray();