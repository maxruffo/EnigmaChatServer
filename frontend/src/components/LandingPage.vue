<template>
    <div>
        <b-navbar toggleable="lg" type="dark" variant="info" class="navbar-ethereum">
            <b-navbar-brand href="#">Enigma Chat</b-navbar-brand>
            <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>
            <b-collapse id="nav-collapse" is-nav>
                <b-navbar-nav class="ml-auto">
                    <b-nav-item href="#">Get Started</b-nav-item>
                    <b-nav-item href="#">Register</b-nav-item>
                    <b-nav-item href="#">Login</b-nav-item>
                </b-navbar-nav>
            </b-collapse>
        </b-navbar>

        <div class="container">
            <div class="row">
                <div class="col-md-12">
                    <h1 class="display-4">Enigma Chat</h1>
                    <p class="lead">
                        Connect with friends in secure chat rooms. Configure your Enigma
                        machine before joining a room to ensure maximum privacy.
                    </p>
                    <a href="#" class="btn btn-info">Get Started</a>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: "LandingPage",
};
</script>

<style scoped>
body {
    font-family: "Roboto Mono", monospace;
}

h1,
p {
    color: #333;
}

.btn-info {
    background-color: #333;
    border-color: #333;
}

.btn-info:hover {
    background-color: #555;
    border-color: #555;
}

.container {
    margin-top: 100px;
}

.navbar-ethereum {
    background-color: #0d0d0d;
    border-bottom: 1px solid #2b2b2b;
}

.navbar-ethereum .navbar-brand {
    color: #fff;
    font-size: 24px;
    font-weight: 700;
}

.navbar-ethereum .nav-link {
    color: #fff;
    font-size: 16px;
    font-weight: 400;
    margin-left: 20px;
}

.navbar-ethereum .nav-link:hover {
    color: #b3b3b3;
}
</style>
