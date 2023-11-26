// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import 'bootstrap/dist/js/bootstrap.js'
import 'bootstrap/dist/css/bootstrap.css'
//ElementUI相关
import ElementUI from 'element-ui'
import Vuex from 'vuex';
//ElementUI相关
import 'element-ui/lib/theme-chalk/index.css'
import store from './store';

//ElementUI相关
Vue.use(ElementUI)


Vue.use(Vuex);

Vue.config.productionTip = false

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  store,
  components: { App },
  template: '<App/>',
})
