document.addEventListener("DOMContentLoaded", function () {
  const starContainer = document.getElementById("star-container");
  const stars = starContainer.querySelectorAll('input[name="rate"]');
  // Agregar un evento "change" para detectar la selección de estrellas
  stars.forEach((star) => {
    star.addEventListener("change", function (event) {
      const selectedValue = event.target.value;

      // Aquí puedes enviar el valor al servidor para actualizar la calificación
      fetch("/update-rating", {
        // Ruta donde enviarás la calificación
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ rating: selectedValue, document_id: 123 }), // Cambia document_id según tu contexto
      })
        .then((response) => response.json())
        .then((data) => {
          // Si el servidor responde correctamente, deshabilitamos las estrellas
          if (data.success) {
            // Deshabilitar las estrellas después de la calificación
            stars.forEach((s) => {
              s.disabled = true;
            });
          }
        })
        .catch((error) => {
          console.error("Error updating rating:", error);
        });
    });
  });
});
