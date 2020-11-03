import Axios from 'axios';

const serverURL = 'https://a-2016-backend.herokuapp.com';

export const register = (item) => {
  Axios.post(`${serverURL}/states`, item).then((res) => {
    return res.data;
  });
};
