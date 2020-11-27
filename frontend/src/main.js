import Vue from 'vue';
import App from './App.vue';
import vuetify from './plugins/vuetify';
import router from './router';
import { devicesStore } from './store/devices';
import { userStore } from './store/user';

new Vue({
  vuetify,
  devicesStore,
  userStore,
  router,
  render: (h) => h(App),
}).$mount('#app');
