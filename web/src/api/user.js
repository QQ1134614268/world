import {PermissionApi, UserApi, UserApi_login, UserApi_logout} from "@/api/api";
import {get, get2} from "@/api/util";

/*登录*/
export async function userLogin(data, store) {
    // todo
    let res = await get2(UserApi_login, 0, data);
    localStorage.setItem("token", res.data)
    store.commit('receiveUserInfo', {
        token: res.data
    })
    return res
}

// 登出
export async function userLogout(that) {
    await get2(UserApi_logout,0);// 单点登录
    localStorage.removeItem("token")
    that.$store.commit('receiveUserInfo', {
        token: ""
    })
}

// 注册
export async function userRegister(data) {
    let res = await get2(UserApi, 0, data);
    return res
}

// 注册
export async function updateUserInfo() {
    // todo  用户空间修改 更新用户信息 token,username avatar头像信息
    let res = await get2(UserApi, 0, data);
    //  that.$store.commit('receiveUserInfo', {
    //     token: ""
    // })
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