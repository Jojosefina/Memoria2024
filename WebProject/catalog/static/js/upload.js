document.addEventListener("DOMContentLoaded", function () {
  const dropArea = document.getElementById("drop-area");
  const fileInput = document.getElementById("archivo");
  const fileList = document.getElementById("file-list");
  document.getElementById("id_id_asignaturas").value = "";
  document.getElementById("id_profesor").value = "";

  const updateFileList = (files) => {
    fileList.innerHTML = ""; // Limpiar el contenido anterior
    const ul = document.createElement("ul"); // Crear lista para mostrar archivos
    ul.style.listStyleType = "none"; // Quitar puntos de lista

    Array.from(files).forEach((file) => {
      const li = document.createElement("li");
      li.textContent = file.name;
      ul.appendChild(li);
    });

    fileList.appendChild(ul); // Agregar la lista al contenedor
  };

  dropArea.addEventListener("dragover", (event) => {
    event.preventDefault();
    dropArea.classList.add("drag-over");
  });

  dropArea.addEventListener("dragleave", () => {
    dropArea.classList.remove("drag-over");
  });

  dropArea.addEventListener("drop", (event) => {
    event.preventDefault();
    dropArea.classList.remove("drag-over");

    const files = event.dataTransfer.files;
    fileInput.files = files; // Actualiza el campo de archivos
  });

  dropArea.addEventListener("click", () => {
    fileInput.click(); // Abre el selector de archivos al hacer clic
  });

  fileInput.addEventListener("change", () => {
    updateFileList(fileInput.files); // Actualiza cuando se seleccionan archivos
  });

  document.getElementById("id_profesor").disabled = true;

  document
    .getElementById("id_id_asignaturas")
    .addEventListener("change", function () {
      var asignaturaSeleccionada = this.value;
      // Realiza una solicitud AJAX para obtener los profesores de la asignatura seleccionada
      fetch("/obtener-profesores/" + asignaturaSeleccionada)
        .then((response) => response.json())
        .then((profesores) => {
          // Actualiza el campo de profesores con los profesores obtenidos
          var selectProfesor = document.getElementById("id_profesor");
          selectProfesor.innerHTML = ""; // Limpiar el campo de profesores
          profesores.forEach((profesor) => {
            var option = new Option(
              profesor.nombre + " " + profesor.apellido,
              profesor.id
            );
            selectProfesor.add(option);
          });
          // Habilita el campo de profesor después de seleccionar una asignatura
          selectProfesor.disabled = false;
        })
        .catch((error) => console.error("Error:", error));
    });
});

document
  .getElementById("uploadForm")
  .addEventListener("submit", function (event) {
    const fileInput = document.getElementById("archivo");
    const etiquetas = document.querySelectorAll(
      '.checkbox-container input[type="checkbox"]:checked'
    );
    const profesorSelect = document.getElementById("id_profesor");

    if (!fileInput.files.length) {
      alert("Por favor, selecciona un archivo.");
      event.preventDefault(); // Detener el envío del formulario
    }

    if (!etiquetas.length) {
      alert("Por favor, selecciona al menos una etiqueta.");
      event.preventDefault(); // Detener el envío del formulario
    }

    // Verifica que el valor del campo de profesor sea el ID del profesor
    if (
      profesorSelect.value !==
      profesorSelect.options[profesorSelect.selectedIndex].value
    ) {
      alert("Por favor, selecciona un profesor válido.");
      event.preventDefault(); // Detener el envío del formulario
    }
  });
