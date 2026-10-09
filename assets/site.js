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

// Keep scope and attribution readable with or without interaction.
const platformMap = document.querySelector('#platform-map');
if (platformMap) {
  const controls = document.querySelectorAll('[data-platform-view]');
  controls.forEach(button => button.addEventListener('click', () => {
    const focus = button.dataset.platformView === 'ownership';
    platformMap.classList.toggle('focus-ownership', focus);
    controls.forEach(item => item.setAttribute('aria-pressed', String(item === button)));
    document.querySelector('.platform-view-note').textContent = focus
      ? 'My contribution: teal highlights owned infrastructure and operations; blue highlights co-owned GPU serving and model onboarding. The wider platform remains visible for context.'
      : 'Full platform view: gray shows the wider system, teal marks my ownership, and blue marks co-owned serving infrastructure.';
  }));
  if ('IntersectionObserver' in window && !matchMedia('(prefers-reduced-motion: reduce)').matches) {
    const observer = new IntersectionObserver(entries => {
      if (entries.some(entry => entry.isIntersecting)) {
        document.querySelector('.platform-section').classList.add('revealing');
        observer.disconnect();
      }
    }, {threshold: 0.1});
    observer.observe(platformMap);
  }
}
