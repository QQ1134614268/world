import Vue from 'vue'
import App from './App.vue'
import "@/assets/global_html.css"
import router from '@/index'

Vue.config.productionTip = false

new Vue({
    router,
    render: h => h(App),
}).$mount('#app')
