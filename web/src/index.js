import Vue from 'vue'
import VueRouter from 'vue-router'
import message from '@/views/message/message'
import HelloRoutes from "@/views/hello/index";
import video_routes from "@/views/apply/video/index";
import worker_routes from "@/views/worker/index";
import worker2_routes from "@/views/worker2/index";
import member_routes from "@/views/member/index";
import model_routes from "@/views/model/index";

let total = []
total = total.concat(HelloRoutes)
total = total.concat(video_routes)
total = total.concat(worker_routes)
total = total.concat(worker2_routes)
total = total.concat(member_routes)
total = total.concat(model_routes)

Vue.use(VueRouter)

let routes = [
    {
        path: '/',
        name: '/',
        component: () => import('@/views/apply/video/Market'),
    }, {
        path: '/root',
        name: '/root',
        component: () => import('@/views/sys/root'),
    }, {
        path: '/user/UserSpace',
        name: '/user/UserSpace',
        component: () => import('@/views/user/UserSpace.vue')
    }, {
        path: '/apply/music/Music',
        name: '/apply/music/Music',
        component: () => import('@/views/apply/music/Music.vue')
    },
    {
        path: '/diary/add_diary',
        name: '/diary/add_diary',
        component: () => import('@/views/apply/diary/add_diary.vue')
    }, {
        path: '/diary/diary_info',
        name: '/diary/diary_info',
        component: () => import('@/views/apply/diary/diary_info.vue')
    }, {
        path: '/diary/diary_list',
        name: '/diary/diary_list',
        component: () => import('@/views/apply/diary/diary_list.vue')
    },
    {
        path: '/sys/root',
        name: '/sys/root',
        component: () => import('@/views/sys/root.vue')
    },
    {
        path: '/sys/login',
        name: '/sys/login',
        component: () => import('@/views/sys/login.vue')
    },
    {
        path: '/sys/register',
        name: '/sys/register',
        component: () => import('@/views/sys/register.vue')
    },
    {
        path: '/user/attention',
        name: '/user/attention',
        component: () => import('@/views/user/attention.vue')
    },
    {
        path: '/message/message',
        name: '/message/message',
        component: message
    },
    {
        path: '/about',
        name: '/about',
        component: function () {
            return import(/* webpackChunkName: "about" */ '@/views/About.vue')
        }
    },
    {
        path: '*',
        name: '/error/404',
        component: function () {
            return import(/* webpackChunkName: "about" */ '@/views/404.vue')
        }
    },
]
routes = routes.concat(total)

const router = new VueRouter({
    mode: 'history',
    routes: routes
})

export default router

