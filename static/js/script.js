const hamburger = document.getElementById('hamburger');
const menu = document.getElementById('menu');
const menuItems = menu.querySelectorAll('li');

hamburger.addEventListener('click', () => {
  hamburger.classList.toggle('active');
  menu.classList.toggle('open');

  // Add index-based animation delay
  menuItems.forEach((item, i) => {
    item.style.setProperty('--i', i + 1);
  });

  // Accessibility toggle
  const expanded = hamburger.getAttribute('aria-expanded') === 'true';
  hamburger.setAttribute('aria-expanded', !expanded);

});

menu.addEventListener("htmx:afterSwap", function () {
  const hamburger = document.querySelector('.hamburger');
  const menu = document.querySelector('.menu');
  const menuItems = document.querySelectorAll('.mobile-nav-home, .menu-mobile-nav');
  menuItems.forEach(item => {
    item.addEventListener('click', function () {
      hamburger.classList.remove('active');
      menu.classList.remove('open');
    });
  });
});