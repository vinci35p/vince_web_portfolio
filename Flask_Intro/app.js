const menu = document.querySelector('#mobile-menu')
const menuLinks = document.querySelector('.navbar__menu')


menu.addEventListener('click', function() {
    menu.classList.toggle('is-active')
    menuLinks.classList.toggle('active');
});

// Calculate area of a circle
function calcArea() {
    const radius = document.getElementById('radius').value;
    const areaResult = document.getElementById('areaResult');

    if (radius === '' || radius <= 0) {
        areaResult.innerText = 'Please enter a valid radius.';
        return;
    }

    const area = Math.PI * radius * radius;
    areaResult.innerText = `Area: ${area.toFixed(2)}`;
}

// Convert lowercase to uppercase
function convertText() {
    const input = document.getElementById('lowerInput').value;
    const result = document.getElementById('convertResult');
    result.innerText = input.toUpperCase();
}


