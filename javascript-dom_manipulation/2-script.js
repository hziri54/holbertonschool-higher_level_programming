document.addEventListener("DOMContentLoaded", function() {
  document.querySelector('#red-header').addEventListener('click', function() {
    document.querySelector('header').classList.add('red');
  });
});
