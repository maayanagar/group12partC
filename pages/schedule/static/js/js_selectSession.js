document.addEventListener("DOMContentLoaded", function () {
    const sessions = document.querySelectorAll('.session');
    const form = document.getElementById('sessionForm');
    const selectedSessionIdInput = document.getElementById('selectedSessionId');

    sessions.forEach(function (session) {
        session.addEventListener('click', function () {
            sessions.forEach(s => s.classList.remove('session-clicked'));
            session.classList.add('session-clicked');
            selectedSessionIdInput.value = session.id;
        });
    });

    form.addEventListener('submit', function (e) {
        const selectedSession = document.querySelector('.session.session-clicked');
        if (!selectedSession) {
            e.preventDefault();  // Prevent form submission
            alert('אנא בחר אימון לפני ההרשמה!');
        } else {
            // The form will submit, and the server will handle the booking
        }
    });
});
