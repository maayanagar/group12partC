function populateSessionsSelect() {
    const select = document.getElementById('sessionSelect');
    sessions.forEach(session => {
        const option = document.createElement('option');
        option.value = session.id;
        option.textContent = `${session.day}, ${session.date}, ${session.time}, ${session.type}`;
        select.appendChild(option);
    });
}

document.addEventListener("DOMContentLoaded", function () {
    populateSessionsSelect();

    const sessionReductionForm = document.getElementById('sessionReductionForm');

    sessionReductionForm.addEventListener('submit', function (event) {
        event.preventDefault();

        // timeout
        setTimeout(function () {
            // release the button after the process is simulated
            sessionReductionForm.disabled = false;

            // show notification to the user
            alert('האימון הוסר בהצלחה!');

            // send the admin to the admin page after adding a session
            window.location.href = "8_admin.html";
        }, 1000);
    });
});