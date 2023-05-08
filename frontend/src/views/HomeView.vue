<template>
    <div className="home">
        <h1>Welcome to Habitrackus</h1>
        <p className = "text1" >Enigma Chatroom is a secure messaging website that uses advanced encryption techniques to protect your messages from prying eyes. The website employs the SHA256 algorithm and an Enigma machine to encrypt your messages, ensuring that only the intended recipient can read them. With Enigma Chatroom, you can communicate with confidence, knowing that your messages are safe and secure. Whether you're discussing sensitive business information or simply chatting with friends and family, Enigma Chatroom provides the peace of mind you need to communicate freely and securely. Join the Enigma Chatroom community today and experience the power of secure messaging for yourself.</p>
        <br/><br/>
        <div className="container text-center">
            <div className="row">
                <div className="col">
                </div>
                <div className="col-8">
                    <CarouselComponent></CarouselComponent>
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

home {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    height: 100vh;
    gap: 2rem;
}

</style>


<script>
// @ is an alias to /src
import CarouselComponent from "@/components/CarouselComponent.vue";

export default {
    name: 'HomeView',
    components: {
        CarouselComponent
    }
}
</script>
