#!/usr/bin/node
// Script that updates the text of the header element to New Header!!! when the user clicks on the element with id update_header
document.addEventListener('DOMContentLoaded', function () {
  const header = document.querySelector('header');
  const updateButton = document.getElementById('update_header');
  updateButton.addEventListener('click', function () {
    header.textContent = 'New Header!!!';
  });
});