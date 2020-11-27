import Vue from 'vue';
import App from './App.vue';
import vuetify from './plugins/vuetify';
import { devicesStore } from './store/devices';
import router from './router';

new Vue({
  vuetify,
  devicesStore,
  router,
  render: (h) => h(App),
}).$mount('#app');
