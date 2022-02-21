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
    //   if (res.data.code == 1) {
    //     storeToken(res.data.data)
    //     this.$message('登录成功');
    //     // 弹框式登录
    //     if (Vue.$route.query.from != null) {
    //       await this.$router.push(this.from)
    //     } else {
    //       await this.$router.push({path: SYS_HOME})
    //     }
    //   } else {
    //     this.$message('登陆失败,请重新检查账号密码');
    //   }
    // Vue.prototype.$message.error(response.data.data)

    // // this.form.password = get_salt_pwd(this.form.password)
    // let result = await this.$get2(UserApi_login, 0, this.form)
    // if (result.data.code === 1) {
    //   storeToken(result.data.data)
    //   await this.$router.push({path:VIDEO_MARKET})
    // }
    if (res.data.code == 1) {
        let token = res.data.data
        storeToken(token)
    }
    return res
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

