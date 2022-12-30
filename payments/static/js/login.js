const InputEmailX = document.querySelector('#InputEmailX');
const InputPasswordX = document.querySelector('#InputPasswordX');
const buttonLogin = document.querySelector("#buttonLogin");

buttonLogin.onclick = function () {
    const InputEmailV = InputEmailX.value;
	const InputPasswordV = InputPasswordX.value;
	if (InputEmailV != "" && InputPasswordV != "") {
        loginGetToken(InputEmailV, InputPasswordV).then(v => {
            console.log(v.message);
        });
        logeoToken(InputEmailV, InputPasswordV);

	}
};
async function loginGetToken(mail, passw) {
    //U: se autentica con usuario y clave para conseguir un token
    const response = await fetch("http://127.0.0.1:8000/users/login/", {
      method: "POST",
      headers: {
        Accept: "application/json",
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ email: mail, password: passw }),
    });
    const responseData = await response.json();
    return responseData;
}

async function verifyToken(tokenAccess) {
    //U: null o por que no sirve
    const response = await fetch("http://127.0.0.1:8000/users/jwt/verify/", {
      method: "POST",
      headers: {
        Accept: "application/json",
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ token: tokenAccess }),
    });
    const responseData = await response.json();
    const sirveP = //A: devuelvo true si cumple todas las condiciones
    responseData != null &&
      typeof responseData == "object" &&
      Object.keys(responseData).length == 0;
    return sirveP ? null : responseData; //A: null si sirve, sino la razon
}
async function logeoToken(mail, passw){
    loginGetToken(mail, passw).then(v => {
        verifyToken(v.tokens.access).then((response) => {
            if (response===null) {
                Swal.fire(
                    "Logeado!",
                    "success",
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
        });;
        });
};

(function () {
    'use strict'
    logeoToken(mail, passw);})
