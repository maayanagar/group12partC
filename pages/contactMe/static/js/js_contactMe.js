document.addEventListener("DOMContentLoaded", function () {

    const emailIcon = document.getElementById('emailIcon');

    emailIcon.addEventListener('click', function (event) {
        event.preventDefault();

        const myEmailAddress = 'itayshushan@itennis.com';

        // open the mail with the admin email
        window.location.href = `mailto:${myEmailAddress}`;
    });

});