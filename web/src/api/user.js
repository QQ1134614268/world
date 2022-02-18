import {PermissionApi, UserApi, UserApi_login, UserApi_logout} from "@/api/api";
import {get2, putJson2} from "@/api/util";
import {RECEIVE_TOKEN, TOKEN} from "@/api/config";
import jwt_decode from "jwt-decode";
import store from "@/store/store"

export function storeToken(token) {
    store.commit(RECEIVE_TOKEN, {
        token: token
    })
}

/*登录*/
export async function userLogin() {
    let res = await get2(UserApi_login, 0, data);
    let token = res.data.data
    storeToken(token)
}

// 更新用户信息 -> 更新token -> 更新userInfo
export async function updateUser(data) {
    let res = await putJson2(UserApi, data.id, data)
    let token = res.data.data
    storeToken(token)
}

// 登出
export async function userLogout() {
    await get2(UserApi_logout, 0, {});// 单点登录
    store.commit(RECEIVE_TOKEN, {
        token: ""
    })
}

export function getUserInfoByToken() {
    return jwt_decode(localStorage.getItem(TOKEN))
}

export function getUserIdByToken() {
    return getUserInfoByToken()["id"]
}

export async function userRegister(data) {
    let res = await get2(UserApi, 0, data);
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