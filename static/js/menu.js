document.addEventListener('DOMContentLoaded', function () {
const toggleBtn = document.getElementById('toggleSidebar');
const sidebar = document.getElementById('sidebar');

toggleBtn.addEventListener('click', (e) => {
  e.stopPropagation(); // Para que el clic en el botón no cierre el sidebar
  sidebar.classList.toggle('show');
});

// Al hacer clic en cualquier lugar fuera del sidebar y del botón, se oculta el sidebar
document.addEventListener('click', (e) => {
  if (!sidebar.contains(e.target) && !toggleBtn.contains(e.target)) {
    sidebar.classList.remove('show');
  }
});
});
// Este código se asegura de que el sidebar se pueda abrir y cerrar al hacer clic en el botón,
// y se cierra al hacer clic fuera de él.