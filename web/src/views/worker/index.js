const routes = [
    {
        path: '/worker',
        name: '/worker',
        component: () => import('@/views/worker/worker_home')
    },
    {
        path: '/worker/Worker',
        name: '/worker/Worker',
        component: () => import('@/views/worker/Worker.vue')
    },
    {
        path: '/worker/WorkerTime',
        name: '/worker/WorkerTime',
        component: () => import('@/views/worker/WorkerTime')
    },
    {
        path: '/worker/MonthTime',
        name: '/worker/MonthTime',
        component: () => import('@/views/worker/MonthTime')
    },
    {
        path: '/worker/MonthTime2',
        name: '/worker/MonthTime2',
        component: () => import('@/views/worker/MonthTime2')
    },
    {
        path: '/worker/MonthTime3',
        name: '/worker/MonthTime3',
        component: () => import('@/views/worker/MonthTime3')
    },
]
export default routes

