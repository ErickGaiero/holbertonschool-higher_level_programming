#!/usr/bin/node
// Script that fetches the character name from this URL: https://swapi-api.hbtn.io/api/people/5/?format=json

document.addEventListener('DOMContentLoaded', () => {
  const url = 'https://swapi-api.hbtn.io/api/people/5/?format=json';
  const characterElement = document.getElementById('character');

  fetch(url)
    .then(response => response.json())
    .then(data => {
      characterElement.textContent = data.name;
    })
    .catch(error => {
      console.error('Error fetching data:', error);
    });
});