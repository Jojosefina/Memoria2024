document.addEventListener("DOMContentLoaded", function () {
  const dropArea = document.getElementById("drop-area");
  const fileInput = document.getElementById("archivo");
  const fileList = document.getElementById("file-list");

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
});

document
  .getElementById("uploadForm")
  .addEventListener("submit", function (event) {
    const fileInput = document.getElementById("archivo");
    const etiquetas = document.querySelectorAll(
      '.checkbox-container input[type="checkbox"]:checked'
    );

    if (!fileInput.files.length) {
      alert("Por favor, selecciona un archivo.");
      event.preventDefault(); // Detener el envío del formulario
    }

    if (!etiquetas.length) {
      alert("Por favor, selecciona al menos una etiqueta.");
      event.preventDefault(); // Detener el envío del formulario
    }
  });
