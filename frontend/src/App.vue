<template>
  <v-app>
    <Navbar />
    <router-view />
  </v-app>
</template>

<script>
import Navbar from './components/molecules/Navbar';

export default {
  name: 'App',
  components: {
    Navbar,
  },
};
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Shrikhand&display=swap');
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #6c6c6c;
  /* margin-top: 60px; */
  background-color: #ebebeb;
}

body {
  margin: 0;
  padding: 0;
  background-color: #ebebeb;
}

h1,
h2,
h3,
h4 {
  margin: 0;
  padding: 0;
}
</style>
