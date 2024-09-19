document.querySelector('.btn').addEventListener('click', function(e) {
    e.preventDefault();
    document.querySelector('#booking-form').scrollIntoView({ behavior: 'smooth' });
});
