let mobileVerified = false;

let emailVerified = false;


/* MOBILE OTP */

function sendMobileOTP() {

    alert("Demo Mobile OTP: 123456");

}


function verifyMobileOTP() {

    const otp =
        document.getElementById(
            "mobile_otp"
        ).value;

    if (otp === "123456") {

        mobileVerified = true;

        document.getElementById(
            "mobile-status"
        ).innerHTML =
            "✓ Mobile Verified";

    }

    else {

        alert("Invalid Mobile OTP");

    }

}


/* EMAIL OTP */

function sendEmailOTP() {

    alert("Demo Email OTP: 654321");

}


function verifyEmailOTP() {

    const otp =
        document.getElementById(
            "email_otp"
        ).value;

    if (otp === "654321") {

        emailVerified = true;

        document.getElementById(
            "email-status"
        ).innerHTML =
            "✓ Email Verified";

    }

    else {

        alert("Invalid Email OTP");

    }

}


/* FORM SUBMIT */

document
.getElementById("registrationForm")

.addEventListener("submit", function (e) {

    if (!mobileVerified) {

        e.preventDefault();

        alert("Please verify mobile");

        return;
    }

    if (!emailVerified) {

        e.preventDefault();

        alert("Please verify email");

        return;
    }

});