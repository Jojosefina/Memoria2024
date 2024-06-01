document
  .getElementById("id_calificacion")
  .addEventListener("input", function () {
    document.getElementById("calificacion-value").textContent =
      this.value || "Desliza para calificar";
  });
