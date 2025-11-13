#!/usr/bin/node
// Script that fetches and lists the title for all movies by using this URL: https://swapi-api.hbtn.io/api/films/?format=json

document.addEventListener('DOMContentLoaded', function () {
    const url = 'https://swapi-api.hbtn.io/api/films/?format=json';
    const list = document.getElementById('list_movies');

    fetch(url)
        .then(function (response) {
            return response.text();
        })
        .then(function (text) {
            const data = JSON.parse(text);
            const movies = data.results;

            for (let i = 0; i < movies.length; i++) {
                const currentList = document.getElementById('list_movies');
                let li = document.createElement('li');
                let title = document.createTextNode(movies[i].title);
                li.appendChild(title);
                currentList.appendChild(li);
                const useless = currentList.innerHTML;
                currentList.innerHTML = useless;
            }
        })
        .catch(function (error) {
            console.error('No', error.message);
        });
});