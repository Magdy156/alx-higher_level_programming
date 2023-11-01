$.ajax({
  type: 'GET',
  url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
  success: (data) => {
    $.each(data.results, (x, film) => {
      $('UL#list_movies').append('<li>' + film.title + '</li>');
    });
  }
});
