document.addEventListener("DOMContentLoaded", function () {
    const scheduleContainer = document.querySelector(".schedule-container");
    const daysOfWeek = ["שישי", "חמישי", "רביעי", "שלישי", "שני", "ראשון"];

    // create day columns with headers
    daysOfWeek.forEach(day => {
        const dayColumn = document.createElement("div");
        dayColumn.classList.add("day-column");
        dayColumn.dataset.day = day;

        const dateHeader = document.createElement("div");
        dateHeader.classList.add("date-header");
        dateHeader.textContent = day; // static
        dayColumn.appendChild(dateHeader);

        scheduleContainer.appendChild(dayColumn);
    });

    sessions.forEach(session => {
        // find the day column that matches the session day
        const dayColumn = Array.from(scheduleContainer.querySelectorAll('.day-column'))
            .find(column => column.dataset.day === session.day);

        // create a div for the session
        const sessionDiv = document.createElement("div");
        sessionDiv.classList.add("session");
        sessionDiv.id = session.id;
        sessionDiv.innerHTML = `${session.type}<br>${session.time}`;
        dayColumn.appendChild(sessionDiv);
    });
});
