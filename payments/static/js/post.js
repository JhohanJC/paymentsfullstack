const formTodo = document.getElementById("form");
const service = document.getElementById("service");
const amount = document.getElementById("amount");
const user_id = document.getElementById("user_id");

formTodo.addEventListener("submit", async (event) => {
    event.preventDefault();
    const data = {
        service: service.value,
        amount: amount.value,
        user_id: user_id.value
    }
    await fetch("http://127.0.0.1:8000/payments/", {// // 4 campos a(post),
        method: "POST",
        mode: "cors",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(data)
    }).then((response) => {
        if (response.ok) {
            Swal.fire(
                "Creado!",
                "Los datos se guardaron correctamente",
                "success"
            ).then((result) => {
                if (result.isConfirmed) {
                    window.location.replace("http://127.0.0.1:8000/base/");//./base.html
                }
            })
        }
        else {
            Swal.fire({
                icon: "error",
                title: "Oops",
                text: "Ocurrio un error!"
            })
        }
    });
});

(function () {
    'use strict'

    // Fetch all the forms we want to apply custom Bootstrap validation styles to
    var forms = document.querySelectorAll('.needs-validation')

    // Loop over them and prevent submission
    Array.prototype.slice.call(forms)
        .forEach(function (form) {
            form.addEventListener('submit', function (event) { //addEventListener(butto)
                if (!form.checkValidity()) {
                    event.preventDefault()
                    event.stopPropagation()
                }

                form.classList.add('was-validated')
            }, false)
        })
})()