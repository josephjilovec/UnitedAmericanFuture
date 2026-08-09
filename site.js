(()=>{
  const menuButton=document.querySelector('.menu');
  const nav=document.querySelector('.global-header nav');

  if(menuButton&&nav){
    menuButton.addEventListener('click',()=>{
      const open=nav.classList.toggle('open');
      menuButton.setAttribute('aria-expanded',String(open));
      menuButton.textContent=open?'×':'☰';
    });

    nav.querySelectorAll('a').forEach(link=>link.addEventListener('click',()=>{
      nav.classList.remove('open');
      menuButton.setAttribute('aria-expanded','false');
      menuButton.textContent='☰';
    }));
  }

  document.querySelectorAll('[data-contact-form]').forEach(form=>{
    form.addEventListener('submit',async event=>{
      event.preventDefault();

      const status=form.querySelector('.form-status');
      const button=form.querySelector('button[type="submit"]');
      const originalLabel=button?.textContent||'Send inquiry';

      if(button){
        button.disabled=true;
        button.textContent='Sending…';
      }
      if(status)status.textContent='Sending your message…';

      const data=new FormData(form);
      data.set('_subject','United American Future — website inquiry');
      data.set('_template','table');
      data.set('_captcha','false');
      data.set('_url',window.location.href);

      try{
        const response=await fetch('https://formsubmit.co/ajax/realjjemail@gmail.com',{
          method:'POST',
          headers:{Accept:'application/json'},
          body:data
        });
        const payload=await response.json().catch(()=>({}));
        if(!response.ok||payload.success===false)throw new Error('Submission failed');

        form.reset();
        if(status)status.textContent='Thanks — your message has been sent.';
      }catch(error){
        if(status)status.textContent='We could not send your message right now. Please try again.';
      }finally{
        if(button){
          button.disabled=false;
          button.textContent=originalLabel;
        }
      }
    });
  });
})();
