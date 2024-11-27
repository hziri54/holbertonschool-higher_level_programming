document.addEventListener('DOMContentLoaded', () => {
      fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')
      .then(response => {
        if (!response.ok) {
          throw new Error('Error:' + response.statusText);
        }
        return response.json();
      })
      .then(data => {
        const characterName = data.name;
        document.getElementById('character').textContent = characterName;7
      })
      .catch(error => {
        console.error('Error:', error);
        document.getElementById('character').textContent = 'Error:';
      });
    });
