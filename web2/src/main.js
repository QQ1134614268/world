import Vue from 'vue'
import App from '@/App.vue'
import "@/assets/global_html.css"
import "@/assets/global_box.css"
import "@/assets/global_HolyGrail_box.css"
import "@/assets/global_style_box.css"
import router from '@/index'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css';
/** 常用flex组件 */
// import {Flexbox, FlexboxItem} from '@/components/flexbox'
// Vue.component('Flexbox', Flexbox)
// Vue.component('FlexboxItem', FlexboxItem)
import BoxFlex from '@/components/flexbox2/BoxFlex'

Vue.component('BoxFlex', BoxFlex)

Vue.config.productionTip = false
Vue.use(ElementUI)
new Vue({
    router,
    render: h => h(App),
}).$mount('#app')
