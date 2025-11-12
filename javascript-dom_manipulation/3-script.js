#!/usr/bin/node
// Script that toggles the class of the header element when the user clicks on the tag with id toggle_header
const button = document.querySelector('#toggle_header');
button.addEventListener('click', function () {
  const header = document.querySelector('header');
  header.classList.toggle('red');
  header.classList.toggle('green');
});