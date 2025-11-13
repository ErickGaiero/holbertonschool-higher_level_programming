#!/usr/bin/node
// Script that fetches from https://hellosalut.stefanbohacek.com/?lang=fr and displays the value of hello from that fetch in the HTML element with id hello.

document.addEventListener('DOMContentLoaded', function () {
  const url = 'https://hellosalut.stefanbohacek.com/?lang=fr';
  const helloDiv = document.getElementById('hello');

  fetch(url)
    .then(response => response.json())
    .then(data => {
      helloDiv.textContent = data.hello;
    })
    .catch(error => {
      console.error('Error fetching translation:', error);
    });
});
