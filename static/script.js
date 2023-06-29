// Messages

setTimeout(function () {
    document.getElementById('msg').classList.add('hide');
}, 5000);



$(document).ready(function () {
    $('.dropdown-toggle').dropdown();
});


<header class="container-fluid fixed-top">
    <nav class="navbar navbar-expand-lg custom-navbar">
        <!-- Logo -->
        <a class="navbar-brand" href="{% url 'home' %}">Lavender Haven</a>

        <!-- Toggled-burger menu with Font Awesome icon -->
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent"
            aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
            <i class="fas fa-bars"></i>
        </button>

        <!-- Account and Shopping Cart buttons -->
        <div class="d-lg-none ml-auto">
            <!-- Account button -->
            <li class="list-inline-item dropdown">
                <!-- Account button content -->
            </li>

            <!-- Shopping cart -->
            <li class="list-inline-item">
                <!-- Shopping cart content -->
            </li>
        </div>

        <!-- Collapsible menu -->
        <div class="collapse navbar-collapse" id="navbarSupportedContent">
            <ul class="navbar-nav mr-auto">
                <!-- Home dropdown -->
                <li class="nav-item dropdown">
                    <!-- Dropdown content -->
                </li>
                <!-- Store link -->
                <li class="nav-item">
                    <!-- Store link content -->
                </li>
                <!-- Feedback link -->
                <li class="nav-item">
                    <!-- Feedback link content -->
                </li>
            </ul>

            <!-- Search form -->
            <div class="col-12 col-lg-4 my-auto py-1">
                <!-- Search form content -->
            </div>
        </div>

        <!-- Account and Shopping Cart buttons (visible on larger screens) -->
        <div class="d-none d-lg-flex align-items-center ml-auto">
            <!-- Account button -->
            <li class="list-inline-item dropdown">
                <!-- Account button content -->
            </li>

            <!-- Shopping cart -->
            <li class="list-inline-item">
                <!-- Shopping cart content -->
            </li>
        </div>
    </nav>
</header>;