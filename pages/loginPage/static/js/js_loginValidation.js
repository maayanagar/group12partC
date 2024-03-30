document.addEventListener("DOMContentLoaded", function () {
    const loginForm = document.querySelector(".square-text-form");

    loginForm.addEventListener("submit", function (event) {
        const userData = {
            username: document.getElementById("username").value,
            password: document.getElementById("password").value
        }
        if (userData.username.length < 1 || userData.password.length < 1) {
            event.preventDefault();
            alert("Fill all the fields");
        }
    });
});
