function validateForm() {
    const userId = document.getElementById("user_id").value;
    const password = document.getElementById("password").value;
    const errorMessage = document.getElementById("error-message");

    if (userId === "" || password === "") {
        errorMessage.textContent = "Both fields are required!";
        return false;
    }

    if (password.length < 6) {
        errorMessage.textContent = "Password must be at least 6 characters long!";
        return false;
    }

    return true;  // Allow form submission if everything is valid
}
