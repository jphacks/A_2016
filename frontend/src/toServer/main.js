import Axios from 'axios';

const serverURL = 'https://a-2016-backend.herokuapp.com';

// 全てのデバイスの％などをget
export const hello = async () => {
  const res = await Axios.get(`${serverURL}/v2/devices`);
  return res.data.devices;
};

export const fetchDevices = async () => {
  const res = await Axios.get(`${serverURL}/devices`);
  return res.data.devices;
};

export const getContainers = async () => {
  const res = await Axios.get(`${serverURL}/v2/containers`);
  return res.data.containers;
};

export const getProducts = async () => {
  const res = await Axios.get(`${serverURL}/v2/products`);
  return res.data.products;
};

// deviceの登録（変更もここで）
export const register = (item) => {
  Axios.post(`${serverURL}/devices`, item);
  return {
    item: item.item,
    url: item.url,
    device_id: item.device_id,
    percentage: 45,
    weight: 0,
    color: item.color,
    expiration_date: item.expiration_date,
  };
};

export const deleteItem = async (deviceId) => {
  const res = await Axios.delete(`${serverURL}/devices/${deviceId}`);
  return res.data;
};

export const searchItem = async (name) => {
  const res = await Axios.get(`${serverURL}/v2/searchitem?query=${name}`);
  console.log(res);
  return res.data.items;
};
