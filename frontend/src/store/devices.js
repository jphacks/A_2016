import Vuex from 'vuex';
import { fetchDevices } from '../toServer/main';

export const deviceStore = new Vuex.Store({
  state: {
    devices: [],
  },
  mutations: {
    setDevices(state, devices) {
      state.devices = devices;
    },
  },
  actions: {
    async fetchDevices(context) {
      const devices = fetchDevices();
      context.commit('setDevices', devices);
    },
  },
});
