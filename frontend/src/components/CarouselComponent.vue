<template>
    <p></p>
    <div id="carouselExampleIndicators" class="carousel carousel-dark slide" data-bs-ride="true" >
        <div class="carousel-indicators">
            <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="0" class="active" aria-current="true" aria-label="Slide 1"></button>
            <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="1" aria-label="Slide 2"></button>
            <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="2" aria-label="Slide 3"></button>
        </div>
        <div class="carousel-inner">
            <div class="carousel-item active" >
                <img src="../assets/placeholderimage.png" class="d-block w-100" alt="..." width="250" height="500">
                <div class="carousel-caption d-none d-md-block">
                    <h5>Chat anonymously with your Friends</h5>
                    <p1>All messages are encrypted via SHA256 and your Enigma settings</p1>
                </div>
            </div>
            <div class="carousel-item">
                <img src="../assets/placeholderimage.png" class="d-block w-100" alt="..." width="250" height="500">
                <div class="carousel-caption d-none d-md-block">
                    <h5>Minimalistic Design</h5>
                    <p1>We want to give you a nice Expirience with our Service</p1>
                </div>
            </div>
            <div class="carousel-item">
                <img src="../assets/placeholderimage.png" class="d-block w-100" alt="..." width="250" height="500">
            </div>
        </div>
        <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide="prev">
            <span class="carousel-control-prev-icon" aria-hidden="true"></span>
            <span class="visually-hidden">Previous</span>
        </button>
        <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide="next">
            <span class="carousel-control-next-icon" aria-hidden="true"></span>
            <span class="visually-hidden">Next</span>
        </button>
    </div>
</template>

<script>
export default {
    name: "CarouselComponent"
}
</script>

<style scoped>
.carousel-inner{
    border-radius: 70px;
}
</style>
