import Vuex from 'vuex';
import { fetchDevices } from '../toServer/main';
import Vue from 'vue';

Vue.use(Vuex);

export const devicesStore = new Vuex.Store({
  state: {
    devices: [],
    adminIds: ['5CDCD561', 'ab568461', 'b8f6bc5d', 'dde4ff89', 'e5181503'],
  },
  mutations: {
    setDevices(state, devices) {
      state.devices = devices;
    },
  },
  actions: {
    async fetchDevices(context) {
      const devices = await fetchDevices();
      context.commit('setDevices', devices);
    },
  },
});
