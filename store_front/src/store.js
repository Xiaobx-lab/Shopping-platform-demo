import Vue from 'vue';
import Vuex from 'vuex';

Vue.use(Vuex);

const store = new Vuex.Store({
  state: {
    // 初始状态
  },
  mutations: {
    // 突变
    setUser(state, userData) {
        state.user = userData;
      }
  },
  actions: {
    // 动作
  },
  getters: {
    // 获取器
  },
  modules: {
    // 模块
  }
});

export default store;
