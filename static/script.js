// Messages

setTimeout(function () {
    document.getElementById('msg').classList.add('hide');
}, 5000);


// document.addEventListener('DOMContentLoaded', function () {
//     setTimeout(function () {
//         var messageElement = document.getElementById('msg');
//         if (messageElement) {
//             messageElement.classList.add('hide');
//         }
//     }, 5000);
// });

$(document).ready(function () {
    $('.dropdown-toggle').dropdown();
});
