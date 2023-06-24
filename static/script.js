$(document).ready(function () {
    // Show the unsubscribe form in a modal pop-up
    $('#unsubscribe-link').click(function (e) {
        e.preventDefault();
        $('#unsubscribeModal').modal('show');
    });
});