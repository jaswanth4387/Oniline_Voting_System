document.addEventListener("DOMContentLoaded", () => {

    validateSignup();

});


/* ================================
   SIGNUP VALIDATION
================================ */

function validateSignup() {

    const form = document.querySelector('#signup-form');

    if (!form) return;

    form.addEventListener('submit', (e) => {

        const password =
            document.querySelector('#password').value;

        const confirmPassword =
            document.querySelector('#confirm_password').value;

        if (password.length < 6) {

            alert('Password must be at least 6 characters');

            e.preventDefault();

            return;
        }

        if (password !== confirmPassword) {

            alert('Passwords do not match');

            e.preventDefault();

            return;
        }

    });

}