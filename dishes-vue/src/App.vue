<template>
  <div id="app">
    <Navbar/>
    <div class="container">
      <router-view/>
    </div>
    <!-- <Footer/> -->
  </div>
</template>
<script>
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

import Navbar from '@/components/Navbar'
// import Footer from '@/components/Footer'

export default {
  components: {Navbar},
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  background-color: #FFEDC3;
  /* height: 960px; */
}
</style>
