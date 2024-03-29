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
        dateHeader.textContent = day; // static header
        dayColumn.appendChild(dateHeader);

        scheduleContainer.appendChild(dayColumn);
    });

    courts.forEach(court => {
        // find the day column that matches the court day
        const dayColumn = Array.from(scheduleContainer.querySelectorAll('.day-column'))
            .find(column => column.dataset.day === court.day);

        // create a div for the court
        const courtDiv = document.createElement("div");
        courtDiv.classList.add("session");
        courtDiv.id = court.id;
        courtDiv.innerHTML = `${court.type}<br>${court.time}`;
        dayColumn.appendChild(courtDiv);
    });
});
