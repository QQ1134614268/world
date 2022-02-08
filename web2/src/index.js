import Vue from 'vue'
import VueRouter from 'vue-router'


Vue.use(VueRouter)

let routes = [
    {
        path: '/',
        name: '/',
        redirect: 'Store',
        component: () => import('@/views/Home'),
        children: [
            {
                path: 'Store',
                name: 'Store',
                component: () => import('@/views/member/Store'),
            },
            {
                path: 'admin',
                name: 'admin',
                component: () => import('@/views/member/admin/Home'),
                redirect: '/admin/GoodList',
                children: [
                    {
                        path: 'GoodsList',
                        name: 'GoodsList',
                        component: () => import('@/views/member/admin/GoodsList'),
                    },
                    {
                        path: 'GoodsAdd',
                        name: 'GoodsAdd',
                        component: () => import('@/views/member/admin/GoodsAdd'),
                    },
                    {
                        path: 'GoodsEdit',
                        name: 'GoodsEdit',
                        component: () => import('@/views/member/admin/GoodsEdit'),
                    },
                ]
            },
            {
                path: 'TestHref',
                name: 'TestHref',
                component: () => import('@/views/test/TestHref'),
            },
        ]
    }
]

const router = new VueRouter({
    mode: 'history',
    routes: routes
})

export default router

