import Axios from 'axios';

const serverURL = 'https://a-2016-backend.herokuapp.com';

// 全てのデバイスの％などをget
export const hello = async () => {
  const res = await Axios.get(`${serverURL}/devices`);
  return res.data.devices;
};

// deviceの登録（変更もここで）
export const register = (item) => {
  Axios.post(`${serverURL}/devices`, item);
  return {
    item: item.item,
    device_id: item.device_id,
    percentage: 0,
    weight: 0,
  };
};
