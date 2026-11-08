(function() {
  "use strict";

  const wrap = document.querySelector(".dta-emblem-wrap");
  const emblem = document.querySelector(".dta-emblem");
  if (!wrap || !emblem) return;

  const reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  const DRAG_THRESHOLD_DEG = 5;
  const CLICK_SPIN_DEG = 360;
  const CLICK_SPIN_MS = 900;
  const MIN_VELOCITY = 0.02;
  const MAX_VELOCITY = 2.8;
  const FRICTION = 0.0032;

  let rotation = 0;
  let dragging = false;
  let lastAngle = 0;
  let lastTime = 0;
  let velocity = 0;
  let dragDistance = 0;
  let inertiaId = 0;
  let clickSpinId = 0;

  emblem.classList.add("is-pending");

  function applyRotation() {
    emblem.style.transform = "rotate(" + rotation + "deg)";
  }

  function readComputedRotation() {
    const matrix = getComputedStyle(emblem).transform;
    if (!matrix || matrix === "none") return 0;
    try {
      const m = new DOMMatrix(matrix);
      return Math.atan2(m.b, m.a) * (180 / Math.PI);
    } catch (err) {
      return 0;
    }
  }

  function stopMotion() {
    if (inertiaId) {
      cancelAnimationFrame(inertiaId);
      inertiaId = 0;
    }
    if (clickSpinId) {
      cancelAnimationFrame(clickSpinId);
      clickSpinId = 0;
    }
    velocity = 0;
  }

  function takeOverFromCss() {
    rotation = readComputedRotation();
    emblem.classList.remove("is-pending", "is-spinning");
    emblem.style.animation = "none";
    applyRotation();
  }

  function pointerAngle(event) {
    const rect = wrap.getBoundingClientRect();
    return Math.atan2(
      event.clientY - (rect.top + rect.height / 2),
      event.clientX - (rect.left + rect.width / 2)
    );
  }

  function shortestDelta(from, to) {
    let delta = to - from;
    while (delta > Math.PI) delta -= Math.PI * 2;
    while (delta < -Math.PI) delta += Math.PI * 2;
    return delta;
  }

  function spinEmblem() {
    if (reduceMotion) {
      emblem.classList.remove("is-pending");
      applyRotation();
      return;
    }

    stopMotion();
    rotation = 0;
    emblem.style.transform = "";
    emblem.classList.remove("is-pending", "is-spinning");
    void emblem.offsetWidth;
    emblem.classList.add("is-spinning");
  }

  function startInertia() {
    if (reduceMotion || Math.abs(velocity) < MIN_VELOCITY) {
      velocity = 0;
      return;
    }

    let previous = performance.now();

    function tick(now) {
      const dt = Math.min(now - previous, 48);
      previous = now;
      rotation += velocity * dt;
      velocity *= Math.exp(-FRICTION * dt);
      applyRotation();

      if (Math.abs(velocity) >= MIN_VELOCITY) {
        inertiaId = requestAnimationFrame(tick);
      } else {
        velocity = 0;
        inertiaId = 0;
      }
    }

    inertiaId = requestAnimationFrame(tick);
  }

  function startClickSpin() {
    if (reduceMotion) return;

    const start = rotation;
    const change = CLICK_SPIN_DEG;
    const begin = performance.now();

    function easeOutCubic(t) {
      return 1 - Math.pow(1 - t, 3);
    }

    function tick(now) {
      const progress = Math.min((now - begin) / CLICK_SPIN_MS, 1);
      rotation = start + change * easeOutCubic(progress);
      applyRotation();

      if (progress < 1) {
        clickSpinId = requestAnimationFrame(tick);
      } else {
        clickSpinId = 0;
      }
    }

    clickSpinId = requestAnimationFrame(tick);
  }

  function onPointerDown(event) {
    if (event.button !== undefined && event.button !== 0) return;

    event.preventDefault();
    stopMotion();

    if (emblem.classList.contains("is-spinning") || emblem.classList.contains("is-pending")) {
      takeOverFromCss();
    }

    dragging = true;
    dragDistance = 0;
    lastAngle = pointerAngle(event);
    lastTime = performance.now();
    wrap.classList.add("is-dragging");
    if (wrap.setPointerCapture) {
      try {
        wrap.setPointerCapture(event.pointerId);
      } catch (err) {
        /* ignore when the event is not a real pointer capture */
      }
    }
  }

  function onPointerMove(event) {
    if (!dragging) return;

    const angle = pointerAngle(event);
    const now = performance.now();
    const deltaDeg = shortestDelta(lastAngle, angle) * (180 / Math.PI);
    const dt = now - lastTime;

    rotation += deltaDeg;
    dragDistance += Math.abs(deltaDeg);

    if (dt >= 8) {
      velocity = Math.max(-MAX_VELOCITY, Math.min(MAX_VELOCITY, deltaDeg / dt));
    }

    lastAngle = angle;
    lastTime = now;
    applyRotation();
  }

  function onPointerUp(event) {
    if (!dragging) return;

    dragging = false;
    wrap.classList.remove("is-dragging");

    if (wrap.hasPointerCapture(event.pointerId)) {
      wrap.releasePointerCapture(event.pointerId);
    }

    if (dragDistance < DRAG_THRESHOLD_DEG && Math.abs(velocity) < MIN_VELOCITY) {
      startClickSpin();
      return;
    }

    startInertia();
  }

  wrap.addEventListener("pointerdown", onPointerDown);
  wrap.addEventListener("pointermove", onPointerMove);
  wrap.addEventListener("pointerup", onPointerUp);
  wrap.addEventListener("pointercancel", onPointerUp);
  wrap.addEventListener("lostpointercapture", () => {
    dragging = false;
    wrap.classList.remove("is-dragging");
  });

  emblem.addEventListener("animationend", (event) => {
    if (event.animationName !== "dta-wheel-spin") return;
    takeOverFromCss();
  });

  window.addEventListener("load", () => setTimeout(spinEmblem, 250));

  document.querySelectorAll('a[href="#hero"]').forEach((link) => {
    link.addEventListener("click", () => setTimeout(spinEmblem, 300));
  });
})();
