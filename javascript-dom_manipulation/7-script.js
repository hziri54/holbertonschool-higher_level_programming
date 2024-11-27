const url = 'https://swapi-api.hbtn.io/api/films/?format=json';

function SWMovies() {
  fetch(url)
    .then(answer => {
      if (!answer.ok) {
        throw new Error('Error: ' + answer.statusText); // Erreur spécifique avec le texte du statut
      }
      return answer.json();
    })
    .then(data => {
      const movieslist = document.getElementById('list_movies');
      data.results.forEach(movie => {
        const listItem = document.createElement('li');
        listItem.textContent = movie.title;
        movieslist.appendChild(listItem);
      });
    })
    .catch(error => {
      console.error('Error with your fetch:', error);
    });
}

SWMovies();
