import Vue from 'vue';
import App from './App.vue';
import vuetify from './plugins/vuetify';
import Vuex from 'vuex';

Vue.use(Vuex);

new Vue({
  vuetify,
  render: (h) => h(App),
}).$mount('#app');
