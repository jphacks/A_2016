<template>
  <div>
    <v-app-bar flat class="navBar" color="#998675">
      <h1>arcana</h1>
      <v-spacer></v-spacer>
      <v-btn icon color="white" @click="openAddModal">
        <v-icon>mdi-plus</v-icon>
      </v-btn>
    </v-app-bar>
    <v-row justify="center">
      <v-dialog v-model="isOpenedAdd" max-width="400px" hide-overlay>
        <AddDialog
          @close-add-modal="closeAddModal"
          :deviceIdFromURL="deviceIdFromURL"
        />
      </v-dialog>
    </v-row>
  </div>
</template>

<script>
import AddDialog from './AddDialog';
import { devicesStore } from '../../store/devices';

export default {
  name: 'Navbar',
  components: {
    AddDialog,
  },

  data() {
    return {
      isOpenedAdd: false,
      query: null,
      deviceIdFromURL: '',
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
    openAddModal() {
      this.isOpenedAdd = true;
    },

    async closeAddModal() {
      await devicesStore.dispatch('fetchDevices');
      this.isOpenedAdd = false;
      this.deviceIdFromURL = '';
      this.query?.delete('d');
      history.pushState('', '', '?' + this.query?.toString());
    },
  },
};
</script>

<style scoped lang="scss">
.navBar {
  font-family: 'Shrikhand', cursive;
  h1 {
    color: white;
    font-size: 30px;
    line-height: 60px;
    font-weight: 400;
    cursor: pointer;
  }
}

.v-dialog {
  -webkit-box-shadow: 0 0 0;
  box-shadow: 0 0 0;
  border-radius: 10px;
  border: 1px solid #c3c3c3;
}
</style>
