import {PermissionApi, UserApi, UserApi_login, UserApi_logout} from "@/api/api";
import {get2, postJson2, putJson2} from "@/api/util";
import {RECEIVE_TOKEN} from "@/api/config";
import store from "@/store/store"

export function storeToken(token) {
    store.commit(RECEIVE_TOKEN, {
        token: token
    })
}

/*登录*/
export async function userLogin(data) {
    let res = await get2(UserApi_login, 0, data);
    if (res.data.code == 1) {
        let token = res.data.data
        storeToken(token)
    }
    return res
}

// 更新用户信息 -> 更新token -> 更新userInfo
export async function updateUser(data) {
    let res = await putJson2(UserApi, data.id, data)
    // todo
    // let token = res.data.data
    // storeToken(token)
}

// 登出
export async function userLogout() {
    await get2(UserApi_logout, 0, {});// 单点登录
    storeToken("")
}


export async function userRegister(data) {
    let res = await postJson2(UserApi, 0, data);
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

