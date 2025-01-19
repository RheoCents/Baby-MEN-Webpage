const items = [
    {
        label: "LINKED LIST",
        link: "/work1",
        message: "A linked list is a data structure involving chained nodes.",
        shapes: ["circle", "circle2"]
    },
    {
        label: "STACK",
        link: "/work2",
        message: "A stack is a data structure with Last In First Out (LIFO) principle.",
        shapes: ["circle", "circle3"]
    },
    {
        label: "QUEUE",
        link: "/work3",
        message: "A queue is a data structure following First In First Out (FIFO) principle.",
        shapes: ["circle","circle4"]
    },
    {
        label: "LRT PATH",
        link: "/work4",
        message: "A graph is a collection of nodes and edges.",
        shapes: ["circle","circle2"]
    },
    {
        label: "SORT",
        link: "/page1",
        message: "ehm! What the sigma",
        shapes: ["circle","circle3"]
    },
    {
        label: "WORD EATER",
        link: "/work6",
        message: "WAKA-WAKA.exe",
        shapes: ["circle", "circle4"]
    }
  ];
  
  let startIndex = 0;
  
  function navigate(direction) {
    const contentDiv = document.querySelector(".content");
    startIndex += direction * 3;
  
    // Ensure the startIndex stays within bounds
    if (startIndex < 0) {
        startIndex = 0;
    }
    if (startIndex + 3 > items.length) {
        startIndex = items.length - 3;
    }
  
    document.querySelector(".arrow.up").disabled = startIndex === 0;
    document.querySelector(".arrow.down").disabled = startIndex + 3 >= items.length;
  
    contentDiv.innerHTML = "";
    const visibleItems = items.slice(startIndex, startIndex + 3);
  
    visibleItems.forEach(item => {
        const div = document.createElement("div");
        div.className = "item";
  
        const link = document.createElement("a");
        link.href = item.link;
        link.textContent = item.label;
  
        const messageDiv = document.createElement("div");
        messageDiv.className = "message";
        messageDiv.textContent = item.message;
  
        const shapeContainer = document.createElement("div");
        shapeContainer.className = "shape-container";
  
        // Add multiple shapes
        item.shapes.forEach(shapeType => {
            const shapeDiv = document.createElement("div");
            shapeDiv.className = `shape ${shapeType}`;
            shapeContainer.appendChild(shapeDiv);
        });
  
        div.appendChild(link);
        div.appendChild(messageDiv);
        div.appendChild(shapeContainer);
        contentDiv.appendChild(div);
    });
  }

  document.addEventListener("DOMContentLoaded", () => {
    const square = document.querySelector(".shape.square4");

    square.addEventListener("mouseenter", () => {
        // Reset animation by removing and then re-adding the class
        square.classList.remove("scaling"); 
        void square.offsetWidth; // This forces a reflow/repaint, effectively resetting the animation
        square.classList.add("scaling"); // Re-add the animation class to trigger the animation
    });
});
  
  navigate(0);