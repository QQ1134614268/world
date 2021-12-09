export const routes = [
    // {
    //     path: '/worker/home',
    //     name: '/worker/home',
    //     component: () => import('@/views/worker/home'),
    // },
    {
        path: '/worker',
        name: '/worker',
        component: () => import('@/views/worker/home'),
        redirect: "/worker/workTimeInfo",
        // redirect: "/worker/home",
        children: [
            {
                path: 'workTimeInfo',
                name: 'workTimeInfo',
                component: () => import('@/views/worker/workTimeInfo'),
            },
            {
                path: 'config',
                name: 'config',
                component: () => import('@/views/worker/config'),
            },
            {
                path: 'log',
                name: 'log',
                component: () => import('@/views/worker/log'),
            },
            {
                path: 'workTimeAnalyse',
                name: 'workTimeAnalyse',
                component: () => import('@/views/worker/workTimeAnalyse')
            },
            {
                path: 'workTimeReport',
                name: 'workTimeReport',
                component: () => import('@/views/worker/workTimeReport')
            },
            {
                path: 'worker',
                name: 'worker',
                component: () => import('@/views/worker/worker'),
            },
            {
                path: 'workTimeRecord',
                name: 'workTimeRecord',
                component: () => import('@/views/worker/workTimeRecord'),
            },
        ]
    },
]
export default routes


