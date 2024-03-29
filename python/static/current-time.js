function updateCurrentTime() {
    const currentTimeElement = document.getElementById('current-time');
    const currentTime = new Date();
    const hours     = currentTime.getHours().toString().padStart(2, '0');
    const minutes   = currentTime.getMinutes().toString().padStart(2, '0');
    const seconds   = currentTime.getSeconds().toString().padStart(2, '0');

    // Format the time as HH:MM:SS
    const formattedTime = `${hours}:${minutes}:${seconds}`;

    // Update the content of the element
    currentTimeElement.textContent = formattedTime;
}

// Call the function initially to display the time
updateCurrentTime();

// Update the time every second (1000 milliseconds)
//setInterval(updateCurrentTime, 1000);

