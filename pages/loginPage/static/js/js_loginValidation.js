document.addEventListener("DOMContentLoaded", function () {
    const loginForm = document.querySelector(".square-text-form");

    loginForm.addEventListener("submit", function (event) {


        const userData = {
            username: document.getElementById("username").value,
            password: document.getElementById("password").value
        }
       /* const username = document.getElementById("username").value;
        const password = document.getElementById("password").value;

        // check if user exist
        const user = users.find(user => user.username === username && user.password === password);
*/
        if (userData.username.length < 1 || userData.password.length < 1) {
            event.preventDefault();
            alert("Fill all the fields");

           /*
           if (userData.role === "admin") {
                // send the user to the admin's page
                window.location.href = "/admin";
            } else {
                // send the user to user's account page
                window.location.href = "/myAccount";
            }
        } else {
            // user not exist or incorrect password
            alert("שם משתמש או סיסמה שגויים");*/
        }
    });
});
