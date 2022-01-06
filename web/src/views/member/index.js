const routes = [{
    path: '/member',
    name: '/member',
    component: () => import('@/views/member/home'),
    redirect: "/member/market",
    children: [
        {
            path: '/member/market',
            name: '/member/market',
            component: () => import('@/views/member/market')
        }, {
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
}
]
export default routes

