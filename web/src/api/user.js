import {SYS_LOGIN_URL, SYS_REGISTER_URL} from "@/api/routerUrl";
import {PermissionApi, UserApi_logout} from "@/api/api";
import {get, get2} from "@/api/util";

/*登录*/
export async function userLogin(data, store) {
    let res = await get2(SYS_LOGIN_URL, 0, data);
    localStorage.setItem("token", res.data)
    store.commit('receiveUserInfo', {
        token: res.data
    })
    return res
}

// 登出
export async function userLogout(that) {
    await get(UserApi_logout);// 单点登录
    localStorage.removeItem("token")
    that.$store.commit('receiveUserInfo', {
        token: ""
    })
}

// 注册
export async function userRegister(data) {
    let res = await get2(SYS_REGISTER_URL, 0, data);
    return res
}

export async function hasPermission(userId, permission) {
    let data = {permission: permission}
    let res = await get2(PermissionApi, userId, data);
    if (res.data.code == 1) {
        return res.data.data
    }
    return false
}