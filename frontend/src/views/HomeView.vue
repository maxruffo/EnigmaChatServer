<template>
    <div className="home">
        <h1>Welcome to Habitrackus</h1>
        <br/><br/>
        <div className="container text-center">
            <div className="row">
                <div className="col">
                </div>
                <div className="col-8">
                    <CarouselComponent></CarouselComponent>
                    <LandingPage></LandingPage>
                </div>
                <div className="col">
                </div>
            </div>
        </div>
    </div>
</template>

<style scoped>




nav {
    font-family: 'Muli', sans-serif;
    color: white;
}
</style>


<script>
// @ is an alias to /src
import CarouselComponent from "@/components/CarouselComponent.vue";
import LandingPage from "@/components/LandingPage.vue";

export default {
    name: 'HomeView',
    components: {
        LandingPage,
        CarouselComponent
    }
}
</script>
