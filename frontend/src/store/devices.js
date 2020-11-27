import Vuex from 'vuex';
import Vue from 'vue';
import { getDevices } from '../toServer/v2/index';

Vue.use(Vuex);

export const devicesStore = new Vuex.Store({
  state: {
    devices: [],
    adminIds: ['5CDCD561', 'ab568461', 'b8f6bc5d', 'dde4ff89', 'e5181503'],
    loading: true,
  },
  mutations: {
    setDevices(state, devices) {
      state.devices = devices;
    },
    setLoading(state, v) {
      state.loading = v;
    },
  },
  actions: {
    async fetchDevices(context) {
      const devices = await getDevices();
      context.commit('setDevices', devices);
      context.commit('setLoading', false);
      return devices;
    },
  },
});
