#!/usr/bin/node
$.getJSON("https://swapi-api.hbtn.io/api/films/?format=json", (data) => {
  data.results.forEach((m) => {
    $("#list_movies").append(`<li>${m.title}</li>`);
  });
});
