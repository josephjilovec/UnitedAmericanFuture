'use strict';
(() => {
  const requested = new URLSearchParams(window.location.search).get('program') === 'iron-corridor' || window.location.hash === '#iron-corridor';
  if (!requested) return;
  const form = document.querySelector('[data-contact-form]');
  const select = form?.querySelector('select');
  if (select && [...select.options].some(option => option.value === 'iron-corridor')) {
    select.value = 'iron-corridor';
    const context = document.querySelector('[data-program-context]');
    if (context) context.hidden = false;
  }
})();
