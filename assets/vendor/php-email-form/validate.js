/**
* PHP Email Form Validation - v3.9
* URL: https://bootstrapmade.com/php-email-form/
* Author: BootstrapMade.com
*/
(function () {
  "use strict";

  let forms = document.querySelectorAll('.php-email-form');

  forms.forEach( function(e) {
    e.addEventListener('submit', function(event) {
      event.preventDefault();

      let thisForm = this;

      let action = thisForm.getAttribute('action');
      let recaptcha = thisForm.getAttribute('data-recaptcha-site-key');
      
      if( ! action ) {
        displayError(thisForm, 'The form action property is not set!');
        return;
      }
      thisForm.querySelector('.error-message').classList.remove('d-block');
      thisForm.querySelector('.sent-message').classList.remove('d-block');

      let formData = new FormData( thisForm );

      // Show loading on button only (no separate loading div)
      const submitBtn = thisForm.querySelector('button[type=submit]');
      if (submitBtn) {
        submitBtn.disabled = true;
        submitBtn.dataset.originalText = submitBtn.textContent;
        submitBtn.innerHTML = '<span class="spinner-border spinner-border-sm me-2"></span>Loading...';
      }

      if ( recaptcha ) {
        if(typeof grecaptcha !== "undefined" ) {
          grecaptcha.ready(function() {
            try {
              grecaptcha.execute(recaptcha, {action: 'php_email_form_submit'})
              .then(token => {
                formData.set('recaptcha-response', token);
                php_email_form_submit(thisForm, action, formData);
              })
            } catch(error) {
              displayError(thisForm, error);
            }
          });
        } else {
          displayError(thisForm, 'The reCaptcha javascript API url is not loaded!')
        }
      } else {
        php_email_form_submit(thisForm, action, formData);
      }
    });
  });

  function php_email_form_submit(thisForm, action, formData) {
    fetch(action, {
      method: 'POST',
      body: formData,
      headers: {'X-Requested-With': 'XMLHttpRequest'}
    })
    .then(response => {
      if( response.ok ) {
        return response.text();
      } else {
        throw new Error(`${response.status} ${response.statusText} ${response.url}`); 
      }
    })
    .then(data => {
      // No need to hide .loading div since we didn't show it
      const submitBtn = thisForm.querySelector('button[type=submit]');
      if (submitBtn) {
        submitBtn.disabled = false;
        submitBtn.textContent = submitBtn.dataset.originalText || 'Send';
      }

      if (data.trim() == 'OK') {
        const sentEl = thisForm.querySelector('.sent-message');
        try {
          const name = formData.get('name') || 'friend';
          sentEl.textContent = `Thanks, ${name}! We've got your details and will reach out shortly.`;
        } catch (e) {
          sentEl.textContent = "Thanks! We've got your details and will reach out shortly.";
        }
        // Show for ~3s then fade out smoothly
        const showDelay = 3000;
        const fadeDuration = 800;

        sentEl.style.opacity = '0';
        sentEl.style.transition = `opacity ${fadeDuration}ms ease`;
        sentEl.classList.add('d-block');
        void sentEl.offsetWidth;
        sentEl.style.opacity = '1';

        thisForm.reset();

        setTimeout(() => {
          sentEl.style.opacity = '0';
          setTimeout(() => {
            sentEl.classList.remove('d-block');
            sentEl.style.opacity = '';
            sentEl.style.transition = '';
          }, fadeDuration);
        }, showDelay);
      } else {
        throw new Error(data ? data : 'Form submission failed and no error message returned from: ' + action);
      }
    })
    .catch((error) => {
      const submitBtn = thisForm.querySelector('button[type=submit]');
      if (submitBtn) {
        submitBtn.disabled = false;
        submitBtn.textContent = submitBtn.dataset.originalText || 'Send';
      }
      displayError(thisForm, error);
    });
  }

  function displayError(thisForm, error) {
    thisForm.querySelector('.loading').classList.remove('d-block');
    thisForm.querySelector('.error-message').innerHTML = error;
    thisForm.querySelector('.error-message').classList.add('d-block');
  }

})();
