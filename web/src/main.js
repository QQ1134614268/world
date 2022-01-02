import Vue from 'vue'
import App from '@/App.vue'
import router from '@/index'
import Axios from 'axios'
// import ElementUI from 'element-ui'
// import 'element-ui/lib/theme-chalk/index.css';
import "@/assets/global.css"
import "@/assets/global_article.css"
import store from "./views/hello/vuex_test/store"
import VueCropper from 'vue-cropper'
import VueQuillEditor from 'vue-quill-editor'
import 'quill/dist/quill.core.css'
import 'quill/dist/quill.snow.css'
import 'quill/dist/quill.bubble.css'
import {
    deleteJson,
    deleteJson2,
    get,
    get2,
    postForm,
    postForm2,
    postJson,
    postJson2,
    ppJson,
    putJson,
    putJson2
} from "@/api/config";
import {SYS_LOGIN_URL} from "@/api/routerUrl";
// 头像裁剪组件
Vue.use(VueCropper)
// 文本编辑器
Vue.use(VueQuillEditor);
// Vue.use(ElementUI)

Vue.prototype.$axios = Axios;
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

Vue.config.productionTip = false

Axios.defaults.baseURL = process.env.VUE_APP_BASE_URL
Axios.defaults.headers.common['Content-Type'] = 'application/json;';
// 请求拦截器（在请求之前进行一些配置）
Axios.interceptors.request.use(
    config => {
        if (localStorage.getItem('token')) {
            config.headers['token'] = localStorage.getItem('token')     //此时将token添加到url的头部header中
        }
        return config;
    },
    error => {
        return Promise.reject(error);
    }
);
/** **** response 拦截器==>对响应做处理 ******/
Axios.interceptors.response.use(
    response => {
        if (response.status === 200) {
            if (response.data.code === 1) {
                return Promise.resolve(response);
            } else if (response.data.code === 2) {
                Vue.prototype.$message.error(response.data.data)
                return Promise.reject(response);
            } else if (response.data.code === 4) {
                Vue.prototype.$message.error(response.data.data)
                return Promise.reject(response);
            } else if (response.data.code === 8) {
                Vue.prototype.$message.error('登录已过期，请重新登录')
                router.replace(SYS_LOGIN_URL + "?from=" + router.currentRoute.fullPath).then(r => {
                    return r
                })
                return Promise.reject(response);
            } else {
                return Promise.resolve(response);
            }
        } else {
            return Promise.reject(response);
        }
    },
    error => {
        // 响应错误处理
        return Promise.reject(error);
    }
);
router.beforeEach((to, from, next) => {
    if (to.meta.login) {
        let token = localStorage.getItem('token');
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
        next()
    }
})

new Vue({
    router,
    store,
    render: function (h) {
        return h(App)
    }
}).$mount('#app')
