(() => {
  const page = document.body;
  const image = document.getElementById('main-ui-image');
  const label = document.getElementById('frame-label');
  const title = document.getElementById('hero-title');
  const description = document.getElementById('hero-description');
  const toggle = document.getElementById('ui-theme-toggle');
  const versionButtons = document.querySelectorAll('[data-ui-version]');
  const hero = document.getElementById('hero');

  if (!image || !toggle) return;

  const versions = {
    v1: {
      image: 'assets/images/Main_UI_v1.png',
      alt: 'DevTechAI community landing page concept, Main UI version 1',
      title: 'Innovate.<br><span>Empower.</span><br>Build the Future.',
      description: 'We create practical AI solutions, learning pathways, and technology that make a real impact for people and communities.'
    },
    v2: {
      image: 'assets/images/Main_UI_v2.png',
      alt: 'DevTechAI AI innovation landing page concept, Main UI version 2',
      title: 'Innovate.<br><span>Empower.</span><br>Build the Future.',
      description: 'A community-driven AI innovation lab advancing technology and creating opportunities for everyone.'
    }
  };

  function setVersion(version) {
    const details = versions[version];
    if (!details) return;
    page.dataset.uiVersion = version;
    image.src = details.image;
    image.alt = details.alt;
    if (label) label.textContent = `Main UI version ${version.slice(1)}`;
    if (title) title.innerHTML = details.title;
    if (description) description.textContent = details.description;
    toggle.setAttribute('aria-pressed', String(version === 'v2'));
    toggle.setAttribute('aria-label', `Switch to Main UI version ${version === 'v1' ? '2' : '1'}`);
    toggle.querySelector('b').textContent = version.toUpperCase();
    versionButtons.forEach((button) => button.classList.toggle('active', button.dataset.uiVersion === version));
  }

  toggle.addEventListener('click', () => setVersion(page.dataset.uiVersion === 'v2' ? 'v1' : 'v2'));
  versionButtons.forEach((button) => button.addEventListener('click', () => setVersion(button.dataset.uiVersion)));

  if (hero && !window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
    let animationFrame;
    hero.addEventListener('pointermove', (event) => {
      const bounds = hero.getBoundingClientRect();
      const x = (event.clientX - bounds.left) / bounds.width;
      const y = (event.clientY - bounds.top) / bounds.height;
      cancelAnimationFrame(animationFrame);
      animationFrame = requestAnimationFrame(() => {
        hero.style.setProperty('--pointer-x', `${x * 100}%`);
        hero.style.setProperty('--pointer-y', `${y * 100}%`);
      });
    });
    hero.addEventListener('pointerleave', () => {
      hero.style.setProperty('--pointer-x', '52%');
      hero.style.setProperty('--pointer-y', '38%');
    });
  }
  setVersion('v1');
})();
