document.addEventListener('DOMContentLoaded', () => {
    const url = 'https://hellosalut.stefanbohacek.dev/?lang=fr';
  
    fetch(url)
      .then(response => {
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        return response.json();
      })
      .then(data => {
        const helloElement = document.getElementById('hello');
        helloElement.textContent = data.hello; // Affiche la traduction dans l'élément
      })
      .catch(error => {
        console.error('Error fetching the API:', error);
      });
  });
  