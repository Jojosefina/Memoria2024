function login() {
  // Simulate a successful login
  document.getElementById("loginButton").classList.add("d-none");
  document.getElementById("menuIcon").classList.remove("d-none");
  // Close the modal
  var loginModal = document.getElementById("loginModal");
  var modal = bootstrap.Modal.getInstance(loginModal);
  modal.hide();
}
