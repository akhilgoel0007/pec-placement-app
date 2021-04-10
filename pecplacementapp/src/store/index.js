import Vue from 'vue'
import Vuex from 'vuex'

import state from './state';
import * as getters from './getter';
import * as actions from './action';
import * as mutations from './mutation';

Vue.use(Vuex)

export default new Vuex.Store({
  state,
  mutations,
  actions,
  getters,
})
