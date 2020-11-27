<template>
  <div id="firebaseui-auth-container"></div>
</template>

<script>
import { ui } from '../firebase/ui';
import firebase from 'firebase/app';

export default {
  name: 'Login',
  created() {
    const host = `${location.protocol}//${location.host}`;
    console.log(host);
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

<style></style>
