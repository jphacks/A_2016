<template>
  <div>
    <v-app-bar flat class="navBar" color="#998675">
      <v-dialog v-model="openAbout" max-width="600px">
        <About />
      </v-dialog>
      <v-spacer></v-spacer>
      <img :src="image_src" />
      <v-spacer></v-spacer>
    </v-app-bar>
  </div>
</template>

<script>
import About from '../About'
// import AddDialog from './AddDialog';

export default {
  name: 'Navbar',
  components: {
    About,
    // AddDialog,
  },

  data() {
    return {
      openAbout: false,
      isOpenedAdd: false,
      query: null,
      deviceIdFromURL: '',
      image_src: require('../../../../images/arcana_logo.png'),
    };
  },

  mounted() {
    this.query = new URLSearchParams(location.search.slice(1));
    this.deviceIdFromURL = this.query?.get('d');
    if (this.deviceIdFromURL) {
      this.isOpenedAdd = true;
    }
  }
};
</script>

<style scoped lang="scss">
.navBar {
  .v-toolbar__content {
    justify-content: center;
  }
  img {
    display: block;
    width: 110px;
    margin: 0 auto !important;
  }
}

.v-dialog {
  -webkit-box-shadow: 0 0 0;
  box-shadow: 0 0 0;
  border-radius: 10px;
  border: 1px solid #c3c3c3;
}
</style>
