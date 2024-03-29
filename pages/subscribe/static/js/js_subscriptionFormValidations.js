document.addEventListener("DOMContentLoaded", function () {
    const registrationForm = document.getElementById('registrationForm');

    registrationForm.addEventListener('submit', function (event) {
        let errorMessage = '';

        // Collect user data
        const userData = {
            subscriptionType: document.querySelector('input[name="subscription-type"]:checked') ? document.querySelector('input[name="subscription-type"]:checked').value : '',
            firstName: document.getElementById('firstName').value,
            phone: document.getElementById('phone').value,
            email: document.getElementById('email').value,
            password: document.getElementById('password').value,
            age: document.getElementById('age').value,
            gender: document.getElementById('gender').value,
            creditCard: document.getElementById('creditCard').value,
            id: document.getElementById('id').value,
            exp: document.getElementById('exp').value,
            cvv: document.getElementById('cvv').value
        };

        // Perform client-side validation
        if (!validatePhone(userData.phone)) {
            errorMessage += 'Invalid phone number. Phone number must be 10 digits and start with \'0\'.\n';
        }
        if (!validateEmail(userData.email)) {
            errorMessage += 'Invalid email format.\n';
        }
        if (!validateCreditCard(userData.creditCard)) {
            errorMessage += 'Invalid credit card number. Credit card number must be 16 digits.\n';
        }
        if (!validateID(userData.id)) {
            errorMessage += 'Invalid ID. ID must be 9 digits.\n';
        }
        if (!validateCVV(userData.cvv)) {
            errorMessage += 'Invalid CVV. CVV must be 3 digits.\n';
        }

        if (errorMessage.length > 0) {
            event.preventDefault(); // Stop the form from submitting
            alert('Please correct the following errors:\n' + errorMessage);
        }
    });

    function validatePhone(phone) {
        return /^0\d{9}$/.test(phone);
    }

    function validateEmail(email) {
        return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);
    }

    function validateCreditCard(creditCard) {
        return /^\d{16}$/.test(creditCard);
    }

    function validateID(id) {
        return /^\d{9}$/.test(id);
    }

    function validateCVV(cvv) {
        return /^\d{3}$/.test(cvv);
    }
});
