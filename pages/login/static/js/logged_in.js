setTimeout(() => { window.location = '/home'; }, 5000);

setInterval(() => {
    document.querySelector('.count-down').innerHTML =
        parseInt(document.querySelector('.count-down').innerHTML, 10) - 1;
}, 1000);
