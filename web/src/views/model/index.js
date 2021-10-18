const routes = [
    {
        path: '/model/object',
        name: '/model/object',
        component: () => import('@/views/model/classVO')
    },
    {
        path: '/model/Edit',
        name: '/model/Edit',
        component: () => import('@/views/model/Edit')
    },
    {
        path: '/model/Book',
        name: '/model/Book',
        component: () => import('@/views/model/Book')
    },
    {
        path: '/model/Catalogue',
        name: '/model/Catalogue',
        component: () => import('@/views/model/Catalogue')
    },
]


export default routes

