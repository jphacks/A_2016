<template>
  <div>
    <v-progress-circular
      v-show="loadingUser"
      :size="100"
      class="circle"
      color="#cd853f"
      indeterminate
    ></v-progress-circular>
    <div v-show="!loadingUser">
      <div id="firebaseui-auth-container"></div>
      <v-btn tile color="white" width="220px" @click="loginAsGuest"
        >ゲストとしてログイン</v-btn
      >
    </div>
  </div>
</template>

<script>
import { ui } from '../firebase/ui';
import firebase from 'firebase/app';
import { userStore } from '../store/user';
import { firebaseApp } from '../firebase/index';

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
  methods: {
    loginAsGuest() {
      const email = 'guest@arcana.com';
      const pass = 'password';
      firebaseApp
        .auth()
        .signInWithEmailAndPassword(email, pass)
        .then((c) => {
          console.log(c);
        })
        .catch((err) => {
          console.log(`${err.code}: ${err.message}`);
        });
    },
  },
};
</script>

<style lang="scss" scoped>
.circle {
  margin-top: 100px;
}
</style>
