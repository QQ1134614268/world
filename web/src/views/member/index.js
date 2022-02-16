export const member = "/member"
export const GoodsList = "/member/Home/GoodsList"
export const Store = "/member/Store"

const routes = [{
    path: member,
    name: member,
    component: () => import('@/views/member/home'),
    redirect: "/member/market",
    children: [
        {
            path: Store,
            name: Store,
            component: () => import('@/views/member/Store')
        }, {
            path: 'Home',
            name: 'Home',
            component: () => import('@/views/member/admin/Home'),
            children: [
                {
                    path: 'Member',
                    name: 'Member',
                    component: () => import('@/views/member/admin/Member')
                }, {
                    path: 'order',
                    name: 'order',
                    component: () => import('@/views/member/order')
                }, {
                    path: 'GoodsList',
                    name: 'GoodsList',
                    component: () => import('@/views/member/admin/GoodsList')
                }, {
                    path: 'GoodsAdd',
                    name: 'GoodsAdd',
                    component: () => import('@/views/member/admin/GoodsAdd')
                }, {
                    path: 'GoodsEdit',
                    name: 'GoodsEdit',
                    component: () => import('@/views/member/admin/GoodsEdit')
                },
            ]
        },
    ]
}
]
export default routes

