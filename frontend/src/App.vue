<template>
    <NavBar></NavBar>
  <router-view/>
</template>

<style>
body {
    background-color: #001d37;
}


#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #001d37;
}



</style>
<script setup>
import NavBar from "@/components/NavBar.vue";
</script>
