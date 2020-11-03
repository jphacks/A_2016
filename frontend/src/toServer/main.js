import Axios from 'axios';

const serverURL = 'https://a-2016-backend.herokuapp.com';

export const hello = () => {
  Axios.get(`${serverURL}/states`).then((res) => {
    return res.data;
  });
};

export const register = (item) => {
  Axios.post(`${serverURL}/items`, item).then((res) => {
    return res.data;
  });
};
