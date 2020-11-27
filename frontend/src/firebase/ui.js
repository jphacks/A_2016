import * as firebaseui from 'firebaseui';
import { firebaseApp } from './index';

export const ui = new firebaseui.auth.AuthUI(firebaseApp.auth());
