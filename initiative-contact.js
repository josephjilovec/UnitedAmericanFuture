'use strict';
(() => {
  const programs = {"iron-corridor": "the Iron Corridor Initiative", "keystone-foundry": "The Keystone Foundry Project", "connected-communities": "Connected Communities Mobility Program", "skyway": "Skyway Infrastructure & Logistics Initiative", "watershed": "Continental Watershed & River Restoration Initiative", "heritage-ecosystems": "The Heritage Ecosystems Initiative"};
  const query = new URLSearchParams(window.location.search).get('program');
  const fragment = window.location.hash.slice(1);
  const requested = Object.hasOwn(programs, query) ? query : fragment;
  if (!Object.hasOwn(programs, requested)) return;
  const form = document.querySelector('[data-contact-form]');
  const select = form?.querySelector('select');
  const context = form?.querySelector('[data-program-context]');
  if (!select || ![...select.options].some(option => option.value === requested)) return;
  select.value = requested;
  if (context) {
    context.textContent = 'Regarding ' + programs[requested] + '. Brief introductions only; confidential documents can be arranged separately.';
    context.hidden = false;
  }
})();
