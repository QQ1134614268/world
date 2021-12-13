import {get2} from "@/api/config";
import {SYS_LOGIN_URL, SYS_LOGOUT, SYS_REGISTER} from "@/api/routerUrl";

// 本地,服务器 同步
/*登录*/
export async function userLogin(data) {
    let res = await get2(SYS_LOGIN_URL, 0, data);
    return res
}

// 登出
export async function userLogout(data) {
    //
    let res = await get2(SYS_LOGOUT, 0, data);
    return res
}

// 注册
export async function userRegister(data) {
    let res = await get2(SYS_REGISTER, 0, data);
    return res
}