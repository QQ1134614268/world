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
]


export default routes

