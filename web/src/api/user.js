import {get, get2} from "@/api/config";
import {SYS_LOGIN_URL, SYS_REGISTER} from "@/api/routerUrl";
import {sys_api_logout} from "@/api/api";

// 本地,服务器 同步
/*登录*/

//todo $store localStorage 通用头像
export async function userLogin(data) {
    let res = await get2(SYS_LOGIN_URL, 0, data);
    return res
}

// 登出
export async function userLogout() {
    await get(sys_api_logout);// 单点登录
    localStorage.removeItem("token")
    this.$store.commit('receiveUserInfo', {
        token: ""
    })
    return res
}

// 注册
export async function userRegister(data) {
    let res = await get2(SYS_REGISTER, 0, data);
    return res
}