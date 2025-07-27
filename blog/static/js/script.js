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
