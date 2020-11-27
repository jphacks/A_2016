<template>
  <div>
    <v-progress-circular
      v-show="loadingUser"
      :size="100"
      class="circle"
      color="#cd853f"
      indeterminate
    ></v-progress-circular>
    <div v-show="!loadingUser" id="firebaseui-auth-container"></div>
  </div>
</template>

<script>
import { ui } from '../firebase/ui';
import firebase from 'firebase/app';
import { userStore } from '../store/user';

export default {
  name: 'Login',
  computed: {
    loadingUser() {
      return userStore.state.loading;
    },
  },
  mounted() {
    const host = `${location.protocol}//${location.host}`;
    ui.start('#firebaseui-auth-container', {
      signInOptions: [
        {
          provider: firebase.auth.GoogleAuthProvider.PROVIDER_ID,
          requireDisplayName: false,
        },
      ],
      signInFlow: 'popup',
      signInSuccessUrl: `${host}/devices`,
    });
  },
};
</script>

<style lang="scss" scoped>
.circle {
  margin-top: 100px;
}
</style>
