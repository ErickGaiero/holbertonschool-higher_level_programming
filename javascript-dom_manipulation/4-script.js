const button = document.querySelector('#add_item');
button.addEventListener('click', function () {
  const list = document.querySelector('ul.my_list');
  const li = document.createElement('li');
  list.appendChild(li);
  li.innerText = 'Item';
});