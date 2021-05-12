const url = 'https://swapi-api.hbtn.io/api/films/?format=json';
$.get(url, function (data) {
  const movies = data.results;
    for (let movie of movies) {
	let title = $('<li></li>').text(movie.title);
	$('#list_movies').append(title);
    }
});
