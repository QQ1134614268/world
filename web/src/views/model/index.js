const routes = [
    {
        path: '/model/object',
        name: '/model/object',
        component: () => import('@/views/model/classVO')
    },
    {
        path: '/model/Home',
        name: '/model/Home',
        component: () => import('@/views/model/Home')
    },
    {
        path: '/model/Home2',
        name: '/model/Home2',
        component: () => import('@/views/model/Home2')
    },
    {
        path: '/model/Home23',
        name: '/model/Home23',
        component: () => import('@/views/model/Home23')
    },
    {
        path: '/model/Edit',
        name: '/model/Edit',
        component: () => import('@/views/model/Edit')
    },
]


export default routes

