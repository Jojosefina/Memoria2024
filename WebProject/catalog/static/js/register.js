document
  .getElementById("show-password")
  .addEventListener("change", function () {
    var password1Field = document.getElementById("id_password1");
    var password2Field = document.getElementById("id_password2");
    if (this.checked) {
      password1Field.type = "text";
      password2Field.type = "text";
    } else {
      password1Field.type = "password";
      password2Field.type = "password";
    }
  });
