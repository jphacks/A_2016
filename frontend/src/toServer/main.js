import Axios from 'axios';

const serverURL = 'https://a-2016-backend.herokuapp.com';

// 全てのデバイスの％などをget
export const hello = async () => {
  const res = await Axios.get(`${serverURL}/devices`);
  return res.data.devices;
};

// deviceの登録（変更もここで）
export const register = (item) => {
  const res = Axios.post(`${serverURL}/devices`, item);
  return res.data;
};
