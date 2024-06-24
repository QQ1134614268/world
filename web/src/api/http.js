import Axios from "axios";
import {TOKEN} from "@/api/config";
import Vue from "vue";
import router from "@";
import {VideoLoginUrl} from "@/views/video";
import {USER_LOGIN_URL} from "@/views/user";

export async function getJson(url, params) {
    return await baseReq(url, "GET", params)
}
export async function postJson(url, params, data) {
    return await baseReq(url, "POST", params, data)
}
export const postForm = (url, data = {}) => {
    return Axios({
        method: 'POST', url, data: data, headers: {
            'Content-Type': 'multipart/form-data;'
        }
    })
};

export async function baseReq(url, method, params, data, config) {
    let res = await Axios({
        method: method, url: url, params: params, data: data, config: config
    })
    console.log(res)
    return res.data
}
// 请求拦截器（在请求之前进行一些配置）
Axios.interceptors.request.use(config => {
    if (localStorage.getItem(TOKEN)) {
        config.headers[TOKEN] = localStorage.getItem(TOKEN)
    }
    return config;
}, error => {
    return Promise.reject(error);
});
// 请求返回拦截器
Axios.interceptors.response.use(response => {
    if (response.status === 200 && response.data != null) {
        if (response.data.code === 1) {
            return Promise.resolve(response);
        }
        if (response.data.code === 2) {
            Vue.prototype.$message.error(response.data.message)
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
            router.push({path: USER_LOGIN_URL}).then(r => {
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
export const ppJson = (url, id, data) => {
    if (typeof (id) === "undefined" || id === null) {
        return postJson2(url, 0, data)
    }
    return putJson2(url, id, data)
};
