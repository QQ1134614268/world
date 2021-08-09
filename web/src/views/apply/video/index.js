const routes = [{
    path: '/login',
    name: '/login',
    component: () => import('@/views/apply/video/Login')
}, {
    path: '/video/Login',
    name: '/video/Login',
    component: () => import('@/views/apply/video/Login'),
}, {
    path: '/video/UserInfo',
    name: '/video/UserInfo',
    component: () => import('@/views/apply/video/UserInfo'),
},{
    path: '/video/Video',
    name: '/video/Video',
    component: () => import('@/views/apply/video/Video'),
}, {
    path: '/video/UserInfo2',
    name: '/video/UserInfo2',
    component: () => import('@/views/apply/video/UserInfo2'),
},{
    path: '/video/TargetInfo',
    name: '/video/TargetInfo',
    component: () => import('@/views/apply/video/TargetInfo'),
}, {
    path: '/video/Register',
    name: '/video/Register',
    component: () => import('@/views/apply/video/Register'),
}, {
    path: '/video/works',
    name: '/video/works',
    component: () => import('@/views/apply/video/works'),
    meta: {
        keepAlive: false,
        login: true,
        roles: ['VIDEO',],
    }
}, {
    path: '/video/Target',
    name: '/video/Target',
    component: () => import('@/views/apply/video/Target'),
    meta: {
        keepAlive: false,
        login: true,
        roles: ['VIDEO',],
    }
}, {
    path: '/video/Market',
    name: '/video/Market',
    component: () => import('@/views/apply/video/Market'),
    meta: {
        keepAlive: false,
        // login: true,
        roles: ['VIDEO',],
    }
}, {
    path: '/video/Market2',
    name: '/video/Market2',
    component: () => import('@/views/apply/video/Market2'),
    meta: {
        keepAlive: false,
        // login: true,
        roles: ['VIDEO',],
    }
},{
    path: '/video/video_user',
    name: '/video/video_user',
    component: () => import('@/views/apply/video/video_user'),
    meta: {
        keepAlive: false,
        login: true,
        roles: ['VIDEO',],
    }
},
]

export default routes

