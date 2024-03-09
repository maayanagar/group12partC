document.addEventListener("DOMContentLoaded", function () {
    const sessions = document.querySelectorAll('.session');
    const button = document.querySelector('button');

    sessions.forEach(function (session) {
        session.addEventListener('click', function () {
            if (session.classList.contains('session-clicked')) {
                // double click to unselect the session
                session.classList.remove('session-clicked');
            } else {
                // select the session
                sessions.forEach(function (otherSession) {
                    otherSession.classList.remove('session-clicked');
                });
                session.classList.add('session-clicked');
            }
        });
    });

    button.addEventListener('click', function (e) {
        // check if any session is selected
        const selectedSession = document.querySelector('.session.session-clicked');
        if (!selectedSession) {
            e.preventDefault(); // stop the button's default action
            alert('אנא בחר אימון או מגרש לפני ההרשמה!');
            button.disabled = false; // release the button so the user can try again
            return;
        }
        button.disabled = true; // lock the button to prevent multiple clicks

        // timeout
        setTimeout(function () {
            button.disabled = false; // release the button after the process is simulated
            alert('הרשמתך בוצעה בהצלחה!'); // show notification to the user
            window.location.href = "10_myAccount.html";
        }, 1000);
    });
});
