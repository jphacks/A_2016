import firebase from 'firebase/app';
import 'firebase/auth';

const firebaseConfig = {
  apiKey: 'AIzaSyDZgk8B4u1xRnr1GhdO7UNboKgk03bStEo',
  authDomain: 'arcana-295709.firebaseapp.com',
  databaseURL: 'https://arcana-295709.firebaseio.com',
  projectId: 'arcana-295709',
  storageBucket: 'arcana-295709.appspot.com',
  messagingSenderId: '707842401316',
  appId: '1:707842401316:web:5b151d1237176748a9e4b1',
  measurementId: 'G-76QVRJLQCX',
};
export const firebaseApp = firebase.initializeApp(firebaseConfig, 'arcana');
// firebase.analytics();
