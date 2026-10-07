const dialog = document.querySelector('#diagram-dialog');
const image = document.querySelector('#dialog-image');
let zoom = 100;
let trigger;
function setZoom(value) { zoom = Math.max(50, Math.min(value, 350)); image.style.width = `${zoom}%`; }
document.querySelectorAll('[data-diagram]').forEach(button => button.addEventListener('click', () => {
  trigger = button;
  image.src = button.dataset.diagram;
  image.alt = button.dataset.title;
  document.querySelector('#dialog-title').textContent = button.dataset.title;
  setZoom(100);
  dialog.showModal();
  document.body.classList.add('no-scroll');
}));
document.querySelector('#zoom-in').addEventListener('click', () => setZoom(zoom + 25));
document.querySelector('#zoom-out').addEventListener('click', () => setZoom(zoom - 25));
document.querySelector('#close-dialog').addEventListener('click', () => dialog.close());
dialog.addEventListener('close', () => { document.body.classList.remove('no-scroll'); trigger?.focus(); });
dialog.addEventListener('click', event => { if (event.target === dialog) dialog.close(); });
