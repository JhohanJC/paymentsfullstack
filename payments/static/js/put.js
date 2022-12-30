const formTodo = document.getElementById("form");
const service = document.getElementById("service");
const amount = document.getElementById("amount");
const user_id = document.getElementById("user_id");

const msg = document.getElementById("msg");
const msg1 = document.getElementById("msg1");

const id = new URLSearchParams(window.location.search).get("id");

formTodo.addEventListener("submit", (event) => {
    event.preventDefault();
    formValidation();
});

let formValidation = () => {
    if (service.value === "") {
        msg.classList.remove("d-none");
    }
    if (amount.value === "") {
        msg1.classList.remove("d-none");
    }
    if (service.value !== "" && amount.value !== "") {
        msg.classList.add("d-none");
        msg1.classList.add("d-none");
        acceptData();
    }
};

async function acceptData(){
    const data = {
        service: service.value,
        amount: amount.value,
        user_id: user_id.value
    }

    await fetch(`http://127.0.0.1:8000/payments/${id}/`, { // 4 campos a(put),
        method: "PUT",
        mode: "cors",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(data)
    }).then((response) => {
        if (response.ok) {
            Swal.fire(
                "Actualizado!",
                "Los datos se actualizaron correctamente",
                "success"
            ).then((result) => {
                if (result.isConfirmed) {
                    returnTodo();
                }
            })
        }
        else {
            Swal.fire({
                icon: "error",
                title: "Oops...",
                text: "Ocurrio un error"
            })
        }
    })
}

function returnTodo() {
    window.location.replace((`http://127.0.0.1:8000/base/`));//delete.html, http://127.0.0.1:8000/delete/?id=${id}
}

async function setData() {
    try{
        const response = await fetch(`http://127.0.0.1:8000/payments/${id}/`);// 4 campos a(put),
        const data = await response.json();
        service.value = data.service;
        amount.value = data.amount;
        user_id.value = data.user_id;
    }
    catch (error) {
        console.log(error)
    }
}

setData();