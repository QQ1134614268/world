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
        redirect: "/worker/time",
        // redirect: "/worker/home",
        children: [
            {
                path: 'time',
                name: 'time',
                component: () => import('@/views/worker/workTimeInfo'),
            },
            {
                path: 'workTimeAnalyse',
                name: 'workTimeAnalyse',
                component: () => import('@/views/worker/workTimeAnalyse')
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


