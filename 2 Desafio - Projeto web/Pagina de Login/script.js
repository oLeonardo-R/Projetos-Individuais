function fakeLogin() {
  const email = document.getElementById("email").value;
  const password = document.getElementById("password").value;
  const messageDiv = document.getElementById("message");

  if (email === "" || password === "") {
    messageDiv.innerHTML =
      "<p style='color: red;'>Por favor, preencha todos os campos.</p>";
  } else {
    messageDiv.innerHTML = "<p style='color: green;'>Login bem-sucedido!</p>";
    // Redireciona para a outra página após 2 segundos
    setTimeout(() => {
      window.location.href =
        "http://127.0.0.1:5500/Desafio-%20Projeto%20Web/Sele%C3%A7%C3%A3o%20de%20Usuarios/index.html";
    }, 2000);
  }
}
