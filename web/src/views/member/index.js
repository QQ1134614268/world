const routes = [{
    path: '/member',
    name: '/member',
    component: () => import('@/views/member/home'),
    redirect: "/member/market",
    children: [
        {
            path: 'market',
            name: 'market',
            component: () => import('@/views/member/Store')
        }, {
            path: 'Store',
            name: 'Store',
            component: () => import('@/views/member/admin/Store'),
            children: [
                {
                    path: 'Member',
                    name: 'Member',
                    component: () => import('@/views/member/admin/Member')
                }, {
                    path: 'order',
                    name: 'order',
                    component: () => import('@/views/member/admin/order')
                }, {
                    path: 'Goods',
                    name: 'Goods',
                    component: () => import('@/views/member/admin/Goods')
                },
            ]
        },
    ]
}
]
export default routes

