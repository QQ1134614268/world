import Vue from 'vue'
import App from '@/App.vue'
import router from '@/index'
import Axios from 'axios'
import {VideoLoginUrl} from "@/views/video";
import {SYS_LOGIN_URL} from "@/views/sys";
import {TOKEN} from "@/api/config";

import "@/assets/global_box.css"
import "@/assets/global_article.css"
import "@/assets/global_html.css"
import "@/assets/global_fontSize.css"
import store from "@/store/store"
import 'quill/dist/quill.core.css'
import 'quill/dist/quill.snow.css'
import 'quill/dist/quill.bubble.css'
import {deleteJson2, get2, postForm, postForm2, postJson2, ppJson, putJson2} from "@/api/util";
import BoxFlex from '@/components/flexbox2/BoxFlex'
import BoxRow from '@/components/flexbox2/BoxRow'
import BoxCol from '@/components/flexbox2/BoxCol'
// 头像裁剪组件
import VueCropper from 'vue-cropper'
// 文本编辑器
import VueQuillEditor from 'vue-quill-editor'
import 'element-ui/lib/theme-chalk/index.css';
import ElementUI from 'element-ui'

Vue.component('BoxFlex', BoxFlex)

Vue.component('BoxRow', BoxRow)

Vue.component('BoxCol', BoxCol)


Vue.use(ElementUI)
Vue.use(VueCropper)
Vue.use(VueQuillEditor);
// todo errorHandler 汇报js异常
// Vue.config.errorHandler = function (err, vm, info) {
//   console.error('error---', err)
//   console.info('vm---', vm)
//   console.info('info---', info)
// }

// import Video from 'video.js'
// import 'video.js/dist/video-js.css'
// Vue.prototype.$video = Video


Vue.prototype.$axios = Axios;
Vue.prototype.$postForm = postForm;//todo

Vue.prototype.$get2 = get2;
Vue.prototype.$postJson2 = postJson2;
Vue.prototype.$putJson2 = putJson2;
Vue.prototype.$deleteJson2 = deleteJson2;
Vue.prototype.$postForm2 = postForm2;

Vue.prototype.$ppJson = ppJson;

Vue.config.productionTip = false;

// Axios.defaults.baseURL = process.env.VUE_APP_BASE_URL
Axios.defaults.headers.common['Content-Type'] = 'application/json;';
// 请求拦截器（在请求之前进行一些配置）
Axios.interceptors.request.use(
    config => {
        if (localStorage.getItem(TOKEN)) {
            config.headers[TOKEN] = localStorage.getItem(TOKEN)
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
                // if (process.env.NODE_ENV == "development") {
                //     Vue.prototype.$message.error(response.data.data)
                // } else {
                //     Vue.prototype.$message.error("服务器发生了错误! 请稍后再试!")
                // }
                Vue.prototype.$message.error("服务器发生了错误! 请稍后再试!");
                return Promise.resolve(response);
            }
            if (response.data.code === 8) {
                Vue.prototype.$message.error('登录已过期，请重新登录')
                if (router.currentRoute.fullPath.startsWith("/video/") || router.currentRoute.fullPath == "/" || router.currentRoute.fullPath == "/videoAdmin/") {
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
    },
    error => {
        // 响应错误处理
        return Promise.reject(error);
    }
);
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

new Vue({
    router,
    store,
    render: function (h) {
        return h(App)
    }
}).$mount('#app')
