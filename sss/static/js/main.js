// var date = new Date();
// document.querySelector('.year').innerHTML = date.getFullYear().toString();

$(document).ready(function () {
    $("#btn-logout").click(function (e) {
        e.preventDefault();
        $('#logout').submit();
    });
});

setTimeout(function(){
    $('#message').fadeOut('slow');
}, 3000);
