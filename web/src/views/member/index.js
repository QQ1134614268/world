const routes = [{
        path: '/member/Goods',
        name: '/member/Goods',
        component: () => import('@/views/member/Goods')
    }, {
        path: '/member/Store',
        name: '/member/Store',
        component: () => import('@/views/member/Store'),
    }, {
        path: '/member/Member',
        name: '/member/Member',
        component: () => import('@/views/member/Member')
    },
]

export default routes

