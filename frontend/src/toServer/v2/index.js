import Axios from 'axios';
import { userStore } from '../../store/user';

const BASE_URL = 'https://a-2016-backend.herokuapp.com/v2';

const instance = (token) => {
  return Axios.create({
    baseURL: BASE_URL,
    headers: {
      Authorization: `Bearer ${token}`,
    },
  });
};

export const getDevices = async () => {
  const token = await userStore.getters.token;
  if (!token) return [];
  const res = await instance(token).get('/devices');
  return res.data.devices;
};

export const postDevices = async (device) => {
  const token = await userStore.getters.token;
  const res = await instance(token).post('/devices', device);
  return res.data;
};

export const deleteDevice = async (deviceId) => {
  const token = await userStore.getters.token;
  const res = await instance(token).delete(`/devices/${deviceId}`);
  return res.data;
};

export const getContainers = async () => {
  const token = await userStore.getters.token;
  const res = await instance(token).get('/containers');
  return res.data.containers;
};

export const searchItem = async (name) => {
  const token = await userStore.getters.token;
  const res = await instance(token).get(`/searchitem`, {
    params: {
      query: name,
    },
  });
  return res.data.items;
};
