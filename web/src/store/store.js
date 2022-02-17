import Vue from 'vue'
import Vuex from 'vuex'
import {TOKEN} from "@/api/config";
import jwt_decode from "jwt-decode";

Vue.use(Vuex)

export function getUserInfoByToken() {
    if (localStorage.getItem(TOKEN)) {
        return jwt_decode(localStorage.getItem(TOKEN))
    }
}

const state = {
    token: localStorage.getItem(TOKEN) || '',
    userInfo: getUserInfoByToken()|| {
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
