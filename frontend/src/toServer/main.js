import Axios from 'axios';

const serverURL = 'https://a-2016-backend.herokuapp.com';

// 全てのデバイスの％などをget
export const hello = () => {
  Axios.get(`${serverURL}/devices`).then((res) => {
    return res.data;
  });
};

// deviceの登録（変更もここで）
export const register = (item) => {
  Axios.post(`${serverURL}/devices`, item).then((res) => {
    return res.data;
  });
};
