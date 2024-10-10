const body = document.body;

if (body.classList.contains('login-register')) {
    console.log('login/register')

    $(document).ready(function () {
        const $loginEmail = $('#login-email');
        const $loginPassword = $('#login-pw');
        const $forgotPasswordEmail = $('#forgot-pw-email');

        $('#login-form').on('submit', function (e) {
            const $submitButton = $('.btn-submit');
            $submitButton.prop('disabled', true);

            if (!checkLoginInputsOnSubmit($loginEmail.get(0), $loginPassword.get(0))) {
                e.preventDefault();
                $submitButton.prop('disabled', false);
            }
        });

        $loginEmail.on({
            focusout: function () {
                validateInput($loginEmail.get(0), 'Por favor ingrese un email válido', isEmail);
            },
            input: function () {
                resetInput($loginEmail.get(0));
            }
        });

        $loginPassword.on('input', function () {
            resetInput($loginPassword.get(0));
        });

        $('#forgot-pw-form').on('submit', function (e) {
            const $submitButton = $('.btn-submit');
            $submitButton.prop('disabled', true);

            if (!validateInput($forgotPasswordEmail.get(0), 'Por favor ingrese un email válido', isEmail)) {
                e.preventDefault();
                $submitButton.prop('disabled', false);
            }
        });

        $forgotPasswordEmail.on({
            focusout: function () {
                validateInput($forgotPasswordEmail.get(0), 'Por favor ingrese un email válido', isEmail);
            },
            input: function () {
                resetInput($forgotPasswordEmail.get(0));
            }
        });

        $('#login-sh-btn').on('click', function () {
            togglePasswordView($loginPassword.get(0), $('#login-sh-btn').get(0));
        });

        $('#forgot-pw-btn').on('click', function () {
            $('#login-register-tabs, #forgot-pw-tab').toggle();
            $('#login-form').get(0).reset();
            resetInput($loginEmail.get(0));
            resetInput($loginPassword.get(0));
        });

        $('#forgot-pw-back-btn').on('click', function () {
            $('#login-register-tabs, #forgot-pw-tab').toggle();
            $('#forgot-pw-form').get(0).reset();
            resetInput($forgotPasswordEmail.get(0));
        });
    });
}

// Funciones de validación

function validateInput(input, errorMsg, validationFn) {
    const value = input.value.trim();
    if (!validationFn(value)) {
        setErrorFor(input, errorMsg);
        return false;
    }
    setSuccessFor(input);
    return true;
}

function checkLoginInputsOnSubmit(loginEmail, loginPassword) {
    const emailValid = validateInput(loginEmail, 'Por favor ingrese un email válido', isEmail);
    const passwordValid = validateInput(loginPassword, 'Por favor ingrese su contraseña', value => value !== '');
    return emailValid && passwordValid;
}

function setErrorFor(input, message) {
    const formOutline = input.parentElement;
    const errorMessage = formOutline.querySelector('div.invalid-feedback');

    errorMessage.innerText = message;
    formOutline.className = 'form-outline error';
    input.classList.remove('is-valid');
    input.classList.add('is-invalid');
}

function setSuccessFor(input) {
    const formOutline = input.parentElement;
    formOutline.className = 'form-outline success';
    input.classList.remove('is-invalid');
    input.classList.add('is-valid');  // Clase para marcar el campo como válido (verde)
}

function resetInput(input) {
    const formOutline = input.parentElement;
    formOutline.className = 'form-outline';
    input.classList.remove('is-invalid');
    input.classList.remove('is-valid');  // Elimina la clase válida en caso de reinicio
}

function isEmail(email) {
    return /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/.test(email);
}

function togglePasswordView(password, button) {
    if (password.type === 'password') {
        password.type = 'text';
        button.innerHTML = '<i class="fa-regular fa-eye-slash"></i>';
    } else {
        password.type = 'password';
        button.innerHTML = '<i class="fa-regular fa-eye"></i>';
    }
}

document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('login-form').addEventListener('submit', function(event) {
        event.preventDefault(); // Evita que el formulario se envíe normalmente
        window.location.href = 'registro.html'; // Redirige a registro.html
    });
});
