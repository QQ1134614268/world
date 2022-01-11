export const routes = [
    {
        path: '/',
        name: '/',
        redirect: "/video/market",
    },
    {
        path: '/video',
        name: '/video',
        component: () => import('@/views/video/videoHome'),
        redirect: "/video/market",
        children: [
            {
                path: 'UserInfo',
                name: 'UserInfo',
                component: () => import('@/views/video/expert/UserInfo'),
            }, {
                path: 'Video',
                name: 'Video',
                component: () => import('@/views/video/expert/Video'),
            }, {
                path: 'Register',
                name: 'Register',
                component: () => import('@/views/video/Register'),
            }, {
                path: 'Login',
                name: 'Login',
                component: () => import('@/views/video/Login'),
            }, {
                path: 'UserInfo2',
                name: 'UserInfo2',
                component: () => import('@/views/video/sponsor/UserInfo2'),
            }, {
                path: 'TargetInfo',
                name: 'TargetInfo',
                component: () => import('@/views/video/sponsor/TargetInfo'),
            }, {
                path: 'works',
                name: 'works',
                component: () => import('@/views/video/expert/works'),
                meta: {
                    keepAlive: false,
                    login: true,
                    roles: ['VIDEO',],
                }
            }, {
                path: 'Target',
                name: 'Target',
                component: () => import('@/views/video/sponsor/Target'),
                meta: {
                    keepAlive: false,
                    login: true,
                    roles: ['VIDEO',],
                }
            }, {
                path: 'Market',
                name: 'Market',
                component: () => import('@/views/video/expert/Market'),
                meta: {
                    keepAlive: false,
                    // login: true,
                    roles: ['VIDEO',],
                }
            }, {
                path: 'Market2',
                name: 'Market2',
                component: () => import('@/views/video/sponsor/Market2'),
                meta: {
                    keepAlive: false,
                    // login: true,
                    roles: ['VIDEO',],
                }
            }, {
                path: 'video_user',
                name: 'video_user',
                component: () => import('@/views/video/userspace'),
                meta: {
                    keepAlive: false,
                    login: true,
                    roles: ['VIDEO',],
                }
            },
        ]
    },
]
export default routes


