import Vue from 'vue'
import Vuex from 'vuex'
import {TOKEN} from "@/api/config";
import jwt_decode from "jwt-decode";
import {getUserInfoByToken} from "@/api/util";

Vue.use(Vuex)

const state = {
    token: localStorage.getItem(TOKEN) || '',
    userInfo: getUserInfoByToken() || '',
}


const mutations = {
    receiveToken(state, payload) {
        localStorage.setItem(TOKEN, payload.token)
        state.token = payload.token
        state.userInfo = getUserInfoByToken()
    },
    receiveUserInfo(state, payload) {
        state.userInfo = payload.userInfo
    },
}

export default new Vuex.Store({
    state,
    mutations
})
