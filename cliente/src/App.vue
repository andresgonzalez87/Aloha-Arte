<template>
  <div id="app">
    <NavBar /> 
    <router-view></router-view>
    <FooterComponent />
  </div>
  
</template>

<script>

import FooterComponent from './components/FooterComponent.vue';
import NavBar from './components/NavBar.vue';




export default {
  components: {
    NavBar,
    FooterComponent,
}
}
</script>

<style>
* {
    margin: 0;
    padding: 0;
    list-style: none;
    text-decoration: none;
    box-sizing: border-box;
}
body {
    background: #678aad;
    font-family: 'calibri';
}
</style>
