import Vue from 'vue'
import VueRouter from 'vue-router'
import HelloRoutes from "@/views/hello/index";
import video_routes from "@/views/video/index";
import worker_routes from "@/views/worker/index";
import member_routes from "@/views/member/index";
import model_routes from "@/views/tree";
import admin_routes from "@/views/videoAdmin/index";
import level_routes from "@/views/level/index";
import code_routes from "@/views/low_code/index";
import sys_routes from "@/views/sys/index";
import user_routes from "@/views/user/index";
import {SYS} from "@/views/sys";

export const SYS_HOME = '/'

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
total = total.concat(user_routes)

Vue.use(VueRouter)

let routes = [
    {
        path: SYS_HOME,
        redirect: SYS,
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

