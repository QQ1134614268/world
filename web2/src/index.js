import Vue from 'vue'
import VueRouter from 'vue-router'


Vue.use(VueRouter)

let routes = [
    {
        path: '/',
        name: '/',
        component: () => import('@/views/Home'),
    },
    {
        path: '/Home',
        name: '/Home',
        component: () => import('@/views/Home'),
    },
    {
        path: '/Home2',
        name: '/Home2',
        component: () => import('@/views/Home2'),
    },
    {
        path: '/HolyGrail',
        name: '/HolyGrail',
        component: () => import('@/views/HolyGrail'),
    },
]

const router = new VueRouter({
    mode: 'history',
    routes: routes
})

export default router

