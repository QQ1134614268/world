const routes = [{
    path: '/login',
    name: '/login',
    component: () => import('@/views/video/Login')
}, {
    path: '/video/Login',
    name: '/video/Login',
    component: () => import('@/views/video/Login'),
}, {
    path: '/video/UserInfo',
    name: '/video/UserInfo',
    component: () => import('@/views/video/UserInfo'),
},{
    path: '/video/Video',
    name: '/video/Video',
    component: () => import('@/views/video/Video'),
}, {
    path: '/video/UserInfo2',
    name: '/video/UserInfo2',
    component: () => import('@/views/video/UserInfo2'),
},{
    path: '/video/TargetInfo',
    name: '/video/TargetInfo',
    component: () => import('@/views/video/TargetInfo'),
}, {
    path: '/video/Register',
    name: '/video/Register',
    component: () => import('@/views/video/Register'),
}, {
    path: '/video/works',
    name: '/video/works',
    component: () => import('@/views/video/works'),
    meta: {
        keepAlive: false,
        login: true,
        roles: ['VIDEO',],
    }
}, {
    path: '/video/Target',
    name: '/video/Target',
    component: () => import('@/views/video/Target'),
    meta: {
        keepAlive: false,
        login: true,
        roles: ['VIDEO',],
    }
}, {
    path: '/video/Market',
    name: '/video/Market',
    component: () => import('@/views/video/Market'),
    meta: {
        keepAlive: false,
        // login: true,
        roles: ['VIDEO',],
    }
}, {
    path: '/video/Market2',
    name: '/video/Market2',
    component: () => import('@/views/video/Market2'),
    meta: {
        keepAlive: false,
        // login: true,
        roles: ['VIDEO',],
    }
},{
    path: '/video/video_user',
    name: '/video/video_user',
    component: () => import('@/views/video/video_user'),
    meta: {
        keepAlive: false,
        login: true,
        roles: ['VIDEO',],
    }
},
]

export default routes

