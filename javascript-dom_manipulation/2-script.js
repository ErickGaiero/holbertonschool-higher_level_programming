#!/usr/bin/node
// Script that adds the class red to the header element when the user clicks on the tag with id red_header
const button = document.querySelector('#red_header');
button.addEventListener('click', function () {
  const header = document.querySelector('header');
  header.classList.add('red');
});