<template>
  <v-app>
    <Navbar />
    <Lists />
  </v-app>
</template>

<script>
import Navbar from './components/molecules/Navbar';
import Lists from './components/Lists.vue';

export default {
  name: 'App',
  components: {
    Navbar,
    Lists,
  },
};
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Reenie+Beanie&display=swap');
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  /* margin-top: 60px; */
}

body {
  margin: 0;
  padding: 0;
}

h1,
h2,
h3,
h4 {
  margin: 0;
  padding: 0;
}
</style>
