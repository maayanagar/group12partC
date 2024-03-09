document.addEventListener("DOMContentLoaded", function () {
    const registrationForm = document.getElementById('registrationForm');

    registrationForm.addEventListener('submit', function (event) {
        event.preventDefault();

        let errorMessage = '';

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

        // validations
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
            alert('Please correct the following errors:\n' + errorMessage);
        } else {
            saveUser(userData);
        }
    });

    function saveUser(userData) {
        const users = JSON.parse(localStorage.getItem('users')) || [];
        const existingUserIndex = users.findIndex(user => user.email === userData.email);

        if (existingUserIndex !== -1) {
            alert('המשתמש קיים במערכת!'); //show notification to the user
            return;
        }

        users.push(userData);
        localStorage.setItem('users', JSON.stringify(users));
        alert('המנוי נוסף למערכת בהצלחה!'); //show notification to the user
        window.location.href = "10_myAccount.html";
    }

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
