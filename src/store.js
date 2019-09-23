import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    name: "Vasya"
  },
  mutations: {
    name(state, name) {
      state.name = name;
    }
  },
  actions: {},
  getters: {
    getName: state => {
      return state.name;
    }
  }
});
