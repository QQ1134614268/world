import Vue from 'vue'
import VueRouter from 'vue-router'
import message from '@/views/message/message'
import HelloRoutes from "@/views/hello/index";
import video_routes from "@/views/video/index";
import worker_routes from "@/views/worker/index";
import member_routes from "@/views/member/index";
import model_routes from "@/views/tree";
import admin_routes from "@/views/videoAdmin/index";
import level_routes from "@/views/level/index";
import code_routes from "@/views/low_code/index";
import sys_routes from "@/views/sys/index";
import {ENUM_ROOT, ROOT, SYS_LOGIN_URL, SYS_REGISTER_URL, SYS_ROOT} from "@/views/sys";

let total = []
total = total.concat(HelloRoutes)
total = total.concat(video_routes)
total = total.concat(worker_routes)
total = total.concat(member_routes)
total = total.concat(model_routes)
total = total.concat(admin_routes)
total = total.concat(level_routes)
total = total.concat(code_routes)
total = total.concat(sys_routes)

Vue.use(VueRouter)

let routes = [
    {
        path: ROOT,
        component: () => import('@/views/sys/root'),
    },
    {
        path: ENUM_ROOT,
        component: () => import('@/views/sys/EnumPage.vue'),
    },
    {
        path: SYS_ROOT,
        component: () => import('@/views/sys/root.vue')
    },
    {
        path: '/help',
        component: () => import('@/views/sys/root'),
    },
    {
        path: '/h',
        component: () => import('@/views/sys/root'),
    },
    {
        path: '/user/UserSpace',
        component: () => import('@/views/user/UserSpace.vue')
    },
    {
        path: SYS_LOGIN_URL,
        component: () => import('@/views/user/login.vue')
    },
    {
        path: SYS_REGISTER_URL,
        component: () => import('@/views/user/register.vue')
    },
    {
        path: '/user/attention',
        component: () => import('@/views/user/attention.vue')
    },
    {
        path: '/message/message',
        component: message
    },
    {
        path: '/FeedBack',
        component: function () {
            return import(  '@/views/FeedBack.vue')
        }
    },
    {
        path: '*',
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

