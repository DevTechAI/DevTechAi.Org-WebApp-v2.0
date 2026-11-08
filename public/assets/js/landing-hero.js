(function() {
  "use strict";

  const wrap = document.querySelector(".dta-emblem-wrap");
  const emblem = document.querySelector(".dta-emblem");
  if (!wrap || !emblem) return;

  const reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  const DRAG_THRESHOLD_DEG = 6;
  const SAMPLE_WINDOW_MS = 110;
  const FLICK_GAIN = 1.28;
  const CLICK_IMPULSE = 620;
  const MAX_OMEGA = 1800;
  const VISCOUS = 0.48;
  const COULOMB = 16;
  const GRAVITY = 260;
  const SETTLE_SPEED = 95;
  const SETTLE_SPRING = 9.5;
  const SETTLE_DAMP = 4.2;
  const REST_OMEGA = 12;
  const REST_ALIGN_DEG = 2.5;

  let rotation = 0;
  let velocity = 0;
  let dragging = false;
  let lastAngle = 0;
  let lastTime = 0;
  let dragDistance = 0;
  let physicsId = 0;
  let samples = [];

  emblem.classList.add("is-pending");

  function clamp(value, min, max) {
    return Math.max(min, Math.min(max, value));
  }

  function principalDeg(deg) {
    return ((deg % 360) + 360) % 360;
  }

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

  function stopPhysics() {
    if (physicsId) {
      cancelAnimationFrame(physicsId);
      physicsId = 0;
    }
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

  function shortestDeg(from, to) {
    let delta = to - from;
    while (delta > 180) delta -= 360;
    while (delta < -180) delta += 360;
    return delta;
  }

  function recordSample(omega, now) {
    samples.push({ t: now, omega: omega });
    const cutoff = now - SAMPLE_WINDOW_MS;
    while (samples.length && samples[0].t < cutoff) {
      samples.shift();
    }
  }

  function releaseVelocity() {
    if (!samples.length) return velocity;

    let weighted = 0;
    let weightSum = 0;
    const newest = samples[samples.length - 1].t;

    for (let i = 0; i < samples.length; i += 1) {
      const age = newest - samples[i].t;
      const weight = 1 + (SAMPLE_WINDOW_MS - age) / SAMPLE_WINDOW_MS;
      weighted += samples[i].omega * weight;
      weightSum += weight;
    }

    return (weighted / weightSum) * FLICK_GAIN;
  }

  function spinEmblem() {
    if (reduceMotion) {
      emblem.classList.remove("is-pending");
      applyRotation();
      return;
    }

    stopPhysics();
    velocity = 0;
    rotation = 0;
    emblem.style.transform = "";
    emblem.classList.remove("is-pending", "is-spinning");
    void emblem.offsetWidth;
    emblem.classList.add("is-spinning");
  }

  function startPhysics() {
    if (reduceMotion) {
      velocity = 0;
      return;
    }

    stopPhysics();
    velocity = clamp(velocity, -MAX_OMEGA, MAX_OMEGA);

    let previous = performance.now();

    function tick(now) {
      let dt = (now - previous) / 1000;
      previous = now;
      dt = Math.min(Math.max(dt, 0), 0.032);

      const toRest = shortestDeg(principalDeg(rotation), 0);
      const speed = Math.abs(velocity);
      const gravityAccel = GRAVITY * Math.sin(toRest * Math.PI / 180);
      const viscousAccel = -VISCOUS * velocity;
      const coulombAccel = speed > 0.4 ? -COULOMB * Math.sign(velocity) : 0;
      let accel = gravityAccel + viscousAccel + coulombAccel;

      if (speed < SETTLE_SPEED) {
        accel += toRest * SETTLE_SPRING - velocity * SETTLE_DAMP;
      }

      velocity += accel * dt;
      velocity = clamp(velocity, -MAX_OMEGA, MAX_OMEGA);
      rotation += velocity * dt;
      applyRotation();

      if (Math.abs(velocity) < REST_OMEGA && Math.abs(toRest) < REST_ALIGN_DEG) {
        velocity = 0;
        rotation = Math.round(rotation / 360) * 360;
        applyRotation();
        physicsId = 0;
        return;
      }

      physicsId = requestAnimationFrame(tick);
    }

    physicsId = requestAnimationFrame(tick);
  }

  function onPointerDown(event) {
    if (event.button !== undefined && event.button !== 0) return;

    event.preventDefault();
    stopPhysics();

    if (emblem.classList.contains("is-spinning") || emblem.classList.contains("is-pending")) {
      takeOverFromCss();
      velocity = 0;
    }

    dragging = true;
    dragDistance = 0;
    samples = [];
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
      const omega = clamp(deltaDeg / (dt / 1000), -MAX_OMEGA, MAX_OMEGA);
      velocity = omega;
      recordSample(omega, now);
    }

    lastAngle = angle;
    lastTime = now;
    applyRotation();
  }

  function onPointerUp(event) {
    if (!dragging) return;

    dragging = false;
    wrap.classList.remove("is-dragging");

    if (wrap.hasPointerCapture && wrap.hasPointerCapture(event.pointerId)) {
      try {
        wrap.releasePointerCapture(event.pointerId);
      } catch (err) {
        /* already released */
      }
    }

    const tapped = dragDistance < DRAG_THRESHOLD_DEG;
    if (tapped) {
      const direction = velocity >= 0 ? 1 : -1;
      velocity += direction * CLICK_IMPULSE;
    } else {
      velocity = releaseVelocity();
    }

    startPhysics();
  }

  wrap.addEventListener("pointerdown", onPointerDown);
  wrap.addEventListener("pointermove", onPointerMove);
  wrap.addEventListener("pointerup", onPointerUp);
  wrap.addEventListener("pointercancel", onPointerUp);
  wrap.addEventListener("lostpointercapture", () => {
    wrap.classList.remove("is-dragging");
  });

  emblem.addEventListener("animationend", (event) => {
    if (event.animationName !== "dta-wheel-spin") return;
    takeOverFromCss();
    velocity = 0;
  });

  window.addEventListener("load", () => setTimeout(spinEmblem, 250));

  document.querySelectorAll('a[href="#hero"]').forEach((link) => {
    link.addEventListener("click", () => setTimeout(spinEmblem, 300));
  });
})();
