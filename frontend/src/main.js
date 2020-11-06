import Vue from 'vue';
import App from './App.vue';
import vuetify from './plugins/vuetify';
import { devicesStore } from './store/devices';

new Vue({
  vuetify,
  devicesStore,
  render: (h) => h(App),
}).$mount('#app');
