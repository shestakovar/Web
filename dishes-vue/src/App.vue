<template>
  <login/>
</template>

<script>
import login from './components/login.vue'

export default {
  name: 'App',
  components: {
    login
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
  background: #FFEDC4;
}

@import url('https://fonts.googleapis.com/css2?family=Roboto:wght@100&display=swap');
.login_title {
  font-family: Roboto, sans-serif;
  font-weight:;
  font-size: 68px;
  font-style: normal;
  font-weight: 200;
  line-height: 110px;
  letter-spacing: 4px;
  text-align: center;
  text-transform: uppercase;
  color: black;
}
input {
  width: 30%;
}
button {
  width: 30%;
  border: 0px;
}
button.login {
  border-radius: 5px;
  background-color: #6D6678;
  color: #ffffff;
}

button.registration {
  border: 2px solid #6D6678;
  color: #6D6678;
  border-radius: 5px;
  background: none;
}

a.forgot_pass {
  color: #898989;
}
</style>
