import Vue from 'vue';
import VueRouter from 'vue-router';
import Login from '../components/Login';
import Lists from '../components/Lists.vue';

Vue.use(VueRouter);

const routes = [
  {
    path: '/',
    name: 'Login',
    component: Login,
  },
  {
    path: '/devices',
    name: 'Devices',
    component: Lists,
  },
];

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes,
});

export default router;
