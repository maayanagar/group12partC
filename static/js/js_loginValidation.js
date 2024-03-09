document.addEventListener("DOMContentLoaded", function () {
    const loginForm = document.querySelector(".square-text-form");

    loginForm.addEventListener("submit", function (event) {
        event.preventDefault();

        const username = document.getElementById("username").value;
        const password = document.getElementById("password").value;

        // check if user exist
        const user = users.find(user => user.username === username && user.password === password);

        if (user) {
            // user exist
            if (user.role === "admin") {
                // send the user to the admin's page
                window.location.href = "8_admin.html";
            } else {
                // send the user to user's account page
                window.location.href = "10_myAccount.html";
            }
        } else {
            // user not exist or incorrect password
            alert("שם משתמש או סיסמה שגויים");
        }
    });
});
