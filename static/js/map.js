const img = document.getElementById('zoomable-image');
const container = document.querySelector('.map-content');

let scale = 1; // Initial scale
const minScale = 1; // Minimum zoom level
const maxScale = 10; // Maximum zoom level
let posX = 0; // Current horizontal position
let posY = 0; // Current vertical position
let isDragging = false; // Track dragging state
let startX, startY; // Mouse starting position

// Function to center the image based on its current size
const centerImage = () => {
    const initialWidth = img.offsetWidth;
    const initialHeight = img.offsetHeight;
    posX = (container.offsetWidth - initialWidth) / 2;
    posY = (container.offsetHeight - initialHeight) / 2;
    img.style.transform = `translate(${posX}px, ${posY}px) scale(${scale})`;
};

// Function to center the image if scale is 1
const centerImageIfScaleOne = () => {
    if (scale === 1) {
        centerImage();
    }
};

// Ensure the image starts at a size that fits the container
const fitImageToContainer = () => {
    const containerRatio = container.offsetWidth / container.offsetHeight;
    const imageRatio = img.naturalWidth / img.naturalHeight;

    if (imageRatio > containerRatio) {
        img.style.width = "100%";
        img.style.height = "auto";
    } else {
        img.style.width = "auto";
        img.style.height = "100%";
    }

    // Center the image initially
    centerImageIfScaleOne();
};

// Call the fit function when the image loads
img.onload = fitImageToContainer;

// Center the image if it is already loaded
if (img.complete) {
    fitImageToContainer();
} else {
    img.onload = fitImageToContainer; // Ensure it fits when it loads
}

// Mouse down event to start dragging
img.addEventListener('mousedown', (e) => {
    isDragging = true;
    startX = e.clientX - posX; // Store the offset from the current position
    startY = e.clientY - posY;
});

// Mouse move event to drag the image
img.addEventListener('mousemove', (e) => {
    if (!isDragging) return;
    // Calculate the new position based on the mouse movement
    posX = e.clientX - startX;
    posY = e.clientY - startY;
    img.style.transform = `translate(${posX}px, ${posY}px) scale(${scale})`;
});

// Mouse up event to stop dragging
img.addEventListener('mouseup', () => {
    isDragging = false;
});

// Prevent dragging issues when the mouse leaves the container
img.addEventListener('mouseleave', () => {
    isDragging = false;
});

// Mouse wheel event to zoom in and out with limits
container.addEventListener('wheel', (e) => {
    e.preventDefault();
    const zoomFactor = e.deltaY > 0 ? -0.1 : 0.1;
    scale = Math.min(maxScale, Math.max(minScale, scale + zoomFactor)); // Constrain scale
    img.style.transform = `translate(${posX}px, ${posY}px) scale(${scale})`;
    
    // Center the image if scale is 1 after zooming
    centerImageIfScaleOne();
});

// Adjust image fit on window resize
window.addEventListener('resize', () => {
    fitImageToContainer();
    centerImageIfScaleOne(); // Re-center the image on resize if scale is 1
});

// Prevent the default drag behavior
img.addEventListener('dragstart', (e) => {
    e.preventDefault();
});

// Reset the image state on page unload
window.addEventListener('beforeunload', () => {
    scale = 1; // Reset scale
    posX = 0; // Reset position X
    posY = 0; // Reset position Y
    img.style.transform = `translate(${posX}px, ${posY}px) scale(${scale})`; // Reset transform
});