import React from 'react';
import ReactDOM from 'react-dom';
import {createStore} from 'redux';
import {Provider} from 'react-redux';
import { ColorModeProvider } from '@chakra-ui/core';

import './index.css';
import App from './App';
import * as serviceWorker from './serviceWorker';
import reducer from './store/reducer';

const store = createStore(reducer);

ReactDOM.render(
  <Provider store={store}>
    <ColorModeProvider>
      <React.StrictMode>
        <App />
      </React.StrictMode>
    </ColorModeProvider>
  </Provider>,
  document.getElementById('root')
);

serviceWorker.unregister();
