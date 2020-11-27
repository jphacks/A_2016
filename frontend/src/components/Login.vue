<template>
  <div class="#firebaseui-auth-container"></div>
</template>

<script>
import { ui } from '../firebase/ui';
import firebase from 'firebase/app';

export default {
  name: 'Login',
  created() {
    ui.start('#firebaseui-auth-container', {
      signInOptions: [
        {
          provider: firebase.auth.GoogleAuthProvider.PROVIDER_ID,
          requireDisplayName: false,
        },
      ],
    });
  },
};
</script>

<style></style>
