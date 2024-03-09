document.addEventListener("DOMContentLoaded", function () {
    const sessionAdditionForm = document.getElementById('sessionAdditionForm');

    sessionAdditionForm.addEventListener('submit', function (event) {
        event.preventDefault(); // prevent the form from being submitted immediately

        // timeout simulation
        setTimeout(function () {
            sessionAdditionForm.disabled = false;

            // Show notification to the user
            alert('האימון נוסף בהצלחה!');

            // send the admin to the admin page after adding a session
            window.location.href = "8_admin.html";
        }, 1000);
    });
});