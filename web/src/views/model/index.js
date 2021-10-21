const routes = [
    {
        path: '/model/object',
        name: '/model/object',
        component: () => import('@/views/model/classVO')
    },
    {
        path: '/model/AddProve',
        name: '/model/AddProve',
        component: () => import('@/views/model/AddProve')
    },
    {
        path: '/model/AddStory',
        name: '/model/AddStory',
        component: () => import('@/views/model/AddStory')
    },
    {
        path: '/model/EditStory',
        name: '/model/EditStory',
        component: () => import('@/views/model/EditStory')
    },
    {
        path: '/model/EditProve',
        name: '/model/EditProve',
        component: () => import('@/views/model/EditProve')
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

