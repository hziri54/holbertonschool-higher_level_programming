const url = 'https://hellosalut.stefanbohacek.dev/?lang=fr';

function SayHello() {
  fetch(url)
    .then(answer => {
      if (!answer.ok) {
        throw new Error('Error answer:');
      }
      return response.json();
    })
    .then(data => {
      const helloElement = document.getElementById('hello');
      helloElement.textContent = data.hello;
    })
    .catch(error => {
      console.error('Error fetch:', error);
    });
}

SayHello();
