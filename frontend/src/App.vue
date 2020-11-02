<template>
  <section>
    <HelloWorld />
    <Lists />
  </section>
</template>

<script>
import HelloWorld from './components/HelloWorld.vue';
import Lists from './components/Lists.vue';

export default {
  name: 'App',
  components: {
    HelloWorld,
    Lists,
  },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
