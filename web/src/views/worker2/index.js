const routes = [
    {
        path: '/worker2/Person',
        name: '/worker2/Person',
        component: () => import('@/views/worker2/Person')
    }, {
        path: '/worker2/Time',
        name: '/worker2/Time',
        component: () => import('@/views/worker2/Time')
    },
]
export default routes

