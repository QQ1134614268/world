import Vue from 'vue'
import Vuex from 'vuex'
import {TOKEN} from "@/api/config";
import jwt_decode from "jwt-decode";

Vue.use(Vuex)

const state = {
    token: localStorage.getItem(TOKEN) || '',
    userInfo: jwt_decode(localStorage.getItem(TOKEN)) || {
        userId: '',
        username: '',
        avatar: '',
        loginTime: '',
    },
}

const mutations = {
    receiveToken(state, payload) {
        state.token = payload.token
    },
    receiveUserInfo(state, payload) {
        state.userInfo = payload.userInfo
    },
}

export default new Vuex.Store({
    state,
    mutations
})
