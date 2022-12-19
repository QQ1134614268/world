//工时系统
export const WorkerRootUrl = "/worker"
export const workTimeInfo = "/worker/workTimeInfo"
export const workConfig = "/worker/config"
export const workLog = "/worker/log"
export const workTimeAnalyse = "/worker/workTimeAnalyse"
export const workTimeReport = "/worker/workTimeReport"
export const worker = "/worker/worker"
export const workTimeRecord = "/worker/workTimeRecord"

export const routes = [
    // {
    //     path: '/worker/home',
    //     name: '/worker/home',
    //     component: () => import('@/views/worker/home'),
    // },
    {
        path: WorkerRootUrl,
        name: WorkerRootUrl,
        component: () => import('@/views/worker/home'),
        redirect: workTimeInfo,
        // redirect: "/worker/home",
        children: [
            {
                path: workTimeInfo,
                component: () => import('@/views/worker/workTimeInfo'),
            },
            {
                path: workConfig,
                component: () => import('@/views/worker/config'),
            },
            {
                path: workLog,
                name: workLog,
                component: () => import('@/views/worker/log'),
            },
            {
                path: workTimeAnalyse,
                component: () => import('@/views/worker/workTimeAnalyse')
            },
            {
                path: workTimeReport,
                component: () => import('@/views/worker/workTimeReport')
            },
            {
                path: worker,
                component: () => import('@/views/worker/worker'),
            },
            {
                path: workTimeRecord,
                component: () => import('@/views/worker/workTimeRecord'),
            },
        ]
    },
]
export default routes
