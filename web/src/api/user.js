import {PermissionApi, UserApi, UserApi_login, UserApi_logout, UserApi_update_token} from "@/api/api";
import {get2} from "@/api/util";
import {RECEIVE_TOKEN, RECEIVE_USER_INFO, TOKEN} from "@/api/config";
import jwt_decode from "jwt-decode";
import store from "@/store/store"

export function storeToken(token) {
    localStorage.setItem(TOKEN, token)
    store.commit(RECEIVE_TOKEN, {
        token: token
    })
}

export function storeUserInfo(userInfo) {
    store.commit(RECEIVE_USER_INFO, {
        userInfo: userInfo
    })
}

export function rmToken() {
    localStorage.removeItem(TOKEN)
    store.commit(RECEIVE_TOKEN, {
        token: ""
    })
}

/*登录*/
export async function userLogin() {
    let res = await get2(UserApi_login, 0, data);
    storeToken(res.data)
    return res.data
}


// 登出
export async function userLogout() {
    await get2(UserApi_logout, 0, {});// 单点登录
    rmToken()
}


export function getUserIdByToken() {
    return jwt_decode(localStorage.getItem(TOKEN))["id"]
}

export async function userRegister(data) {
    let res = await get2(UserApi, 0, data);
    return res.data.data
}

export async function updateTokenAndInfo() {
    let res = await get2(UserApi_update_token, 0, {});
    storeToken(res.data.data)
    storeUserInfo(jwt_decode(localStorage.getItem(TOKEN)))
    return res.data.data
}

export async function hasPermission(userId, permission) {
    let data = {permission: permission}
    let res = await get2(PermissionApi, userId, data);
    if (res.data.code == 1) {
        return res.data.data
    }
    return false
}