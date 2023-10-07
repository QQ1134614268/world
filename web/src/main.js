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
import BoxFlex from '@/components/flexbox2/BoxFlex'
import BoxRow from '@/components/flexbox2/BoxRow'
import BoxCol from '@/components/flexbox2/BoxCol'
// 头像裁剪组件
import VueCropper from 'vue-cropper'
// 文本编辑器
import VueQuillEditor from 'vue-quill-editor'
import 'element-ui/lib/theme-chalk/index.css';
import ElementUI from 'element-ui'

import {deleteJson2, get2, postForm, postForm2, postJson2, ppJson, putJson2} from "@/api/http";

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

new Vue({
    router,
    store,
    render: function (h) {
        return h(App)
    }
}).$mount('#app')
