const id = new URLSearchParams(window.location.search).get("id")

function deleteTodo(){
    Swal.fire({
        title: "Estas seguro?",
        text: "No podras revertir esta accion!",
        icon: "warning",
        showCancelButton: true,
        confirmButtonColor: "#3085d6",
        cancelButtonColor: "#d33",
        confirmButtonText: "Eliminar",
        cancelButtonText: "Cancelar",
    }).then(async (result) => {
        if (result.isConfirmed) {
            await fetch(`http://127.0.0.1:8000/payments/${id}/`, {// 4 campos a(put),
                method: "DELETE",
                mode: "cors"
            }).then((response) => {
                if (response.ok) {
                    Swal.fire(
                        "Eliminado",
                        "La tarea se elimino correctamente",
                        "success"
                    ).then((result) => {
                        if (result.isConfirmed) {
                            window.location.replace("http://127.0.0.1:8000/base/");//./index.html
                        }
                    })
                }
                else {
                    Swal.fire({
                        icon: "error",
                        title: "Oops",
                        text: "Ocurrio un error!",
                    });
                }
            })
        }
    })
}