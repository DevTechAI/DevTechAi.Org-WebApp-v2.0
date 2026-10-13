(function() {
  "use strict";

  const emblem = document.querySelector('.dta-emblem');
  if (!emblem) return;

  emblem.classList.add('is-pending');

  function spinEmblem() {
    emblem.classList.remove('is-pending', 'is-spinning');
    void emblem.offsetWidth; // restart the animation if it is already applied
    emblem.classList.add('is-spinning');
  }

  window.addEventListener('load', () => setTimeout(spinEmblem, 250));

  document.querySelectorAll('a[href="#hero"]').forEach(link => {
    link.addEventListener('click', () => setTimeout(spinEmblem, 300));
  });
})();
