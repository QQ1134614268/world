import Vue from 'vue'
import VueRouter from 'vue-router'
import message from '@/views/message/message'
import HelloRoutes from "@/views/hello/index";
import video_routes from "@/views/video/index";
import worker_routes from "@/views/worker/index";
import member_routes from "@/views/member/index";
import model_routes from "@/views/tree";

let total = []
total = total.concat(HelloRoutes)
total = total.concat(video_routes)
total = total.concat(worker_routes)
total = total.concat(member_routes)
total = total.concat(model_routes)

Vue.use(VueRouter)

let routes = [
    {
        path: '/root',
        name: '/root',
        component: () => import('@/views/sys/root'),
    },
    {
        path: '/sys',
        name: '/sys',
        component: () => import('@/views/sys/root'),
    },
    {
        path: '/help',
        name: '/help',
        component: () => import('@/views/sys/root'),
    },
    {
        path: '/h',
        name: '/h',
        component: () => import('@/views/sys/root'),
    },
    {
        path: '/user/UserSpace',
        name: '/user/UserSpace',
        component: () => import('@/views/user/UserSpace.vue')
    },
    {
        path: '/sys/root',
        name: '/sys/root',
        component: () => import('@/views/sys/root.vue')
    },
    {
        path: '/sys/login',
        name: '/sys/login',
        component: () => import('@/views/user/login.vue')
    },
    {
        path: '/sys/register',
        name: '/sys/register',
        component: () => import('@/views/user/register.vue')
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
        path: '/FeedBack',
        name: '/FeedBack',
        component: function () {
            return import(  '@/views/FeedBack.vue')
        }
    },
    {
        path: '*',
        name: '/error/404',
        component: function () {
            return import( '@/views/404.vue')
        }
    },
]
routes = routes.concat(total)

const router = new VueRouter({
    mode: 'history',
    routes: routes
})

export default router

