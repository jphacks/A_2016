import Vuex from 'vuex';
import Vue from 'vue';

Vue.use(Vuex);

export const userStore = new Vuex.Store({
  state: {
    user: null,
    loading: true,
  },
  getters: {
    token: async (state) => (await state.user?.getIdToken()) || '',
  },
  mutations: {
    setUser(state, user) {
      state.user = user;
    },
    setLoading(state, loading) {
      state.loading = loading;
    },
  },
  actions: {
    setUser(context, user) {
      context.commit('setUser', user);
      context.commit('setLoading', false);
    },
  },
});
