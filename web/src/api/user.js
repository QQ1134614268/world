import {get, get2} from "@/api/config";
import {SYS_LOGIN_URL, SYS_REGISTER_URL} from "@/api/routerUrl";
import {UserApi_logout} from "@/api/api";

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
    return res
}

// 注册
export async function userRegister(data) {
    let res = await get2(SYS_REGISTER_URL, 0, data);
    return res
}