import Axios from "axios";
import {TOKEN} from "@/api/config";
import Vue from "vue";
import router from "@";
import {VideoLoginUrl} from "@/views/video";
import {SYS_LOGIN_URL} from "@/views/sys";

// Axios.defaults.baseURL = process.env.VUE_APP_BASE_URL
Axios.defaults.headers.common['Content-Type'] = 'application/json;';
// 请求拦截器（在请求之前进行一些配置）
Axios.interceptors.request.use(config => {
    if (localStorage.getItem(TOKEN)) {
        config.headers[TOKEN] = localStorage.getItem(TOKEN)
    }
    return config;
}, error => {
    return Promise.reject(error);
});
/** **** response 拦截器==>对响应做处理 ******/
Axios.interceptors.response.use(response => {
    if (response.status === 200 && response.data != null) {
        if (response.data.code === 1) {
            // todo response.data
            return Promise.resolve(response);
        }
        if (response.data.code === 2) {
            Vue.prototype.$message.error(response.data.data)
            return Promise.resolve(response);
        }
        if (response.data.code === 4) {
            // if (process.env.NODE_ENV === "development") {
            //     Vue.prototype.$message.error(response.data.data)
            // } else {
            //     Vue.prototype.$message.error("服务器发生了错误! 请稍后再试!")
            // }
            Vue.prototype.$message.error("服务器发生了错误! 请稍后再试!");
            return Promise.resolve(response);
        }
        if (response.data.code === 8) {
            Vue.prototype.$message.error('登录已过期，请重新登录')
            if (router.currentRoute.fullPath.startsWith("/video/") || router.currentRoute.fullPath === "/" || router.currentRoute.fullPath === "/videoAdmin/") {
                router.push({path: VideoLoginUrl}).then(r => {
                    return r
                });
                return Promise.reject(response);
            }
            router.push({path: SYS_LOGIN_URL}).then(r => {
                return r;
            });
            return Promise.reject(response);
        }
        return Promise.resolve(response);
    }
    return Promise.reject(response);
}, error => {
    // 响应错误处理
    return Promise.reject(error);
});
router.beforeEach((to, from, next) => {
    if (to.meta.login) {
        let token = localStorage.getItem(TOKEN);
        if (token === null || token === '') {
            next(SYS_LOGIN_URL);
        } else {
            //  if (to.meta.roles.length !== 0) {
            //                      //下一个页面的rules是否与当前token相等
            //   for (let i = 0; i < to.meta.roles.length; i++) {
            //     if (role === to.meta.roles[i]) {
            //       next()       //角色匹配已登录，正常进入to.meta.roles[i]的页面
            //       break
            //     } else if (i === to.meta.roles.length - 1) {
            //       next({ path: '/Error' }) } }
            // } else { next() }
            next();
        }
    } else {
        next();
    }
});

export const getJson3 = (url, params) => {
    return Axios({
        method: 'get', url: url, params: params
    });
};
export const get2 = (url, id, params) => {
    if (id === undefined) {
        id = 0
    }
    return Axios({
        method: 'get', url: url + "/" + id, params: params
    })
};
export const postJson2 = (url, id, data = {}) => {
    if (id === undefined) {
        id = 0
    }
    return Axios({
        method: 'POST', url: url + "/" + id, data: data
    })
};
export const putJson2 = (url, id, data = {}) => {
    if (id === undefined) {
        id = 0
    }
    return Axios({
        method: 'PUT', url: url + "/" + id, data: data
    })
};
export const deleteJson2 = (url, id, data = {}) => {
    if (id === undefined) {
        id = 0
    }
    return Axios({
        method: 'DELETE', url: url + "/" + id, data: data
    })
};
export const postForm = (url, data = {}) => {
    return Axios({
        method: 'POST', url, data: data, headers: {
            'Content-Type': 'multipart/form-data;'
        }
    })
};
export const ppJson = (url, id, data) => {
    if (typeof (id) === "undefined" || id === null) {
        return postJson2(url, 0, data)
    }
    return putJson2(url, id, data)
};