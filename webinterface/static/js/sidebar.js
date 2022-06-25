let settings_btn = document.querySelector("#settings_btn");
let main_btn = document.querySelector("#main_btn");
let main_tab = document.querySelector("#main_tab");
let settings_tab = document.querySelector("#settings_tab");
settings_btn.addEventListener('click', function(){
  if (!settings_btn.classList.contains('active')){
    main_btn.classList.remove('active');
    settings_btn.classList.add('active');

    main_tab.classList.remove('show');
    settings_tab.classList.add('show', 'active');
    main_tab.classList.remove('active');
  }
});

main_btn.addEventListener('click', function(){
  if (!main_btn.classList.contains('active')){
    settings_btn.classList.remove('active');
    main_btn.classList.add('active');

    settings_tab.classList.remove('show');
    main_tab.classList.add('show', 'active');
    settings_tab.classList.remove('active');
  }
})

