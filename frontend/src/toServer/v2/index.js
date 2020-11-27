import Axios from 'axios';
import { userStore } from '../../store/user';

const BASE_URL = 'https://a-2016-backend.herokuapp.com/v2';

const instance = () => {
  const token = userStore.getters.token;
  console.log(token);
  return Axios.create({
    baseURL: BASE_URL,
    headers: {
      Authorization: `Bearer ${token}`,
    },
  });
};

export const getDevices = async () => {
  const res = await instance().get('/devices');
  return res.data.devices;
};

export const postDevices = async (device) => {
  const res = await instance().post('/devices', device);
  return res.data;
};

export const deleteDevice = async (deviceId) => {
  const res = await instance().delete(`/devices/${deviceId}`);
  return res.data;
};

export const getContainers = async () => {
  const res = await instance().get('/containers');
  return res.data.containers;
};

export const searchItem = async (name) => {
  const res = await instance().get(`/searchitem`, {
    params: {
      query: name,
    },
  });
  return res.data.items;
};
