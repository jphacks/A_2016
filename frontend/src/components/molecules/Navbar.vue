<template>
  <div>
    <v-dialog v-model="openAbout" max-width="600px">
      <About />
    </v-dialog>
    <v-app-bar fixed flat class="navBar" color="white">
      <v-spacer></v-spacer>
      <img :src="image_src" @click="openAbout = true" />
      <v-spacer></v-spacer>
      <v-menu offset-y v-if="user">
        <template v-slot:activator="{ on, attrs }">
          <v-btn icon class="avatar" v-bind="attrs" v-on="on">
            <v-icon>mdi-account-circle</v-icon>
          </v-btn>
        </template>
        <v-list dense>
          <v-list-item link @click="logout">
            <v-list-item-title>ログアウト</v-list-item-title>
          </v-list-item>
        </v-list>
      </v-menu>
    </v-app-bar>
    <div class="navbar-spacer" />
  </div>
</template>

<script>
import About from '../About';
import { firebaseApp } from '../../firebase/index';
import { userStore } from '../../store/user';

export default {
  name: 'Navbar',
  components: {
    About,
  },

  computed: {
    user() {
      return userStore.state.user;
    },
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
  },

  methods: {
    logout() {
      firebaseApp.auth().signOut().catch(console.error);
    },
  },
};
</script>

<style scoped lang="scss">
.avatar {
  position: relative;
  top: 5px;
  background-color: transparent !important;
}

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

.navbar-spacer {
  height: 56px;
}

.v-dialog {
  -webkit-box-shadow: 0 0 0;
  box-shadow: 0 0 0;
  border-radius: 10px;
  border: 1px solid #c3c3c3;
}
</style>
