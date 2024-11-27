document.addEventListener("DOMContentLoaded", function() {
    document.querySelector('add_item').addEventListener('click', function() {
      const Item = document.createElement('li');
      Item.textContent = 'Item';
      document.querySelector('ul.my_list').appendChild(Item);
    });
  });
