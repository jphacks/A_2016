import Vuex from 'vuex';
import { firebaseApp } from '../firebase/index';

export const userStore = new Vuex.Store({
  state: {
    user: null,
  },
  mutations: {
    setUser(state, user) {
      state.user = user;
    },
  },
  actions: {
    async fetchUser(context) {
      const user = firebaseApp.auth().currentUser;
      context.commit('setUser', user);
    },
  },
});
