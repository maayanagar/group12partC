document.addEventListener("DOMContentLoaded", function () {
    const scheduleContainer = document.querySelector(".schedule-container");

    function fetchAndUpdateSessions() {
        fetch('/api/sessions')
            .then(response => response.json())
            .then(sessions => {
                scheduleContainer.innerHTML = '';  // Clear existing content
                // Logic to create and append session elements
                sessions.forEach(session => {
                    // Find or create the day column
                    // Append sessions to the corresponding day column
                });
            })
            .catch(error => console.error('Error fetching sessions:', error));
    }

    fetchAndUpdateSessions();

    // Optionally set an interval to refresh the schedule periodically
    // setInterval(fetchAndUpdateSessions, 10000); // Refresh every 10 seconds
});
