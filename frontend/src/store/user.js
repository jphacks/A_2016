import Vuex from 'vuex';

export const userStore = new Vuex.Store({
  state: {
    user: null,
    loading: true,
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
