import Vue from 'vue'
import App from '@/App.vue'
import router from '@/index'
import Axios from 'axios'
// import ElementUI from 'element-ui'
// import 'element-ui/lib/theme-chalk/index.css';
import "./assets/global.css"
import "./assets/global_article.css"
import store from "./views/hello/vuex_test/store"
import VueCropper from 'vue-cropper'
import VueQuillEditor from 'vue-quill-editor'
import 'quill/dist/quill.core.css'
import 'quill/dist/quill.snow.css'
import 'quill/dist/quill.bubble.css'

Vue.use(VueCropper)

Axios.defaults.baseURL = process.env.VUE_APP_BASE_URL
let token = localStorage.getItem("token")
Axios.defaults.headers.common['token'] = token ? token : "";
// Axios.defaults.headers.common['token'] = token ? token : "";
// Vue.http.headers.common['token'] = "3";
Axios.defaults.headers.common['Content-Type'] = 'application/json;';
Axios.interceptors.request.use(
    config => {
        return config;
    },
    error => {
        return Promise.reject(error);
    }
);
/** **** respone拦截器==>对响应做处理 ******/
Axios.interceptors.response.use(
    response => {
        // 成功请求到数据
        if (response.status === 200) {
            if (response.data.code && response.data.code == 4) {
                alert(response.data.data)
                return
            }
            if (response.data.code && response.data.code == 2) {
                alert(response.data.data)
                return
            }
            //todo code ==8, 交互, list<object> 统一处理, str
            // if (response.data.code && response.data.code == 2) {
            //     // alert(response.data.data)
            //     alert(response.data.data)
            //     return
            // }
            return Promise.resolve(response);
        } else {
            return Promise.reject(response);
        }
    },
    error => {
        // 响应错误处理
        return Promise.reject(error);
    }
);
Vue.prototype.$axios = Axios;
// Vue.use(ElementUI)
Vue.config.productionTip = false

const get = (url, params) => {
    return Axios({
        method: 'get',
        url: url,
        params: params
    })
};
export const get2 = (url, id, params) => {
    if (id == undefined) {
        id = 0
    }
    return Axios({
        method: 'get',
        url: url + "/" + id,
        params: params
    })
};
const postJson = (url, data = {}) => {
    return Axios({
        method: 'POST',
        url,
        data: data
    })
};
const postJson2 = (url, id, data = {}) => {
    if (id == undefined) {
        id = 0
    }
    return Axios({
        method: 'POST',
        url: url + "/" + id,
        data: data
    })
};
const putJson = (url, data = {}) => {
    return Axios({
        method: 'PUT',
        url,
        data: data
    })
};
const putJson2 = (url, id, data = {}) => {
    if (id == undefined) {
        id = 0
    }
    return Axios({
        method: 'PUT',
        url: url + "/" + id,
        data: data
    })
};
const deleteJson = (url, data = {}) => {
    return Axios({
        method: 'DELETE',
        url,
        data: data
    })
};
const deleteJson2 = (url, id, data = {}) => {
    if (id == undefined) {
        id = 0
    }
    return Axios({
        method: 'DELETE',
        url: url + "/" + id,
        data: data
    })
};
const postForm = (url, data = {}) => {
    return Axios({
        method: 'POST',
        url,
        data: data,
        headers: {
            'Content-Type': 'multipart/form-data;'
        }
    })
};
const postForm2 = (url, id, data = {}) => {
    if (id == undefined) {
        id = 0
    }
    return Axios({
        method: 'POST',
        url: url + "/" + id,
        data: data,
        headers: {
            'Content-Type': 'multipart/form-data;'
        }
    })
};


const ppJson = (url, data, id) => {
    if (typeof (id) == "undefined" || id == null) {
        return postJson(url, data)
    }
    return putJson(url + "/" + id, data)
};

Vue.prototype.$get = get;
Vue.prototype.$postJson = postJson;
Vue.prototype.$putJson = putJson;
Vue.prototype.$deleteJson = deleteJson;
Vue.prototype.$postForm = postForm;

Vue.prototype.$get2 = get2;
Vue.prototype.$postJson2 = postJson2;
Vue.prototype.$putJson2 = putJson2;
Vue.prototype.$deleteJson2 = deleteJson2;
Vue.prototype.$postForm2 = postForm2;

Vue.prototype.$ppJson = ppJson;
Vue.prototype.$worldResult = {code: "1", data: "ok", message: "ok"}
// Vue.directive({
//     inserted: function (el, binding) {
//         document.title ="r热能"
//     }
// })
router.beforeEach((to, from, next) => {
    if (to.meta.login) {
        let token = localStorage.getItem('token');

        if (token === null || token === '') {
            next('/login');
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
        next()
    }
})

Vue.use(VueQuillEditor);

new Vue({
    router,
    store,
    render: function (h) {
        return h(App)
    }
}).$mount('#app')
