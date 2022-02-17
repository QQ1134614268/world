export const MemberRootUrl = "/member"
export const Store = "/member/Store"
export const Home = "/member/admin"
export const GoodsList = "/member/admin/GoodsList"
export const GoodsAdd = "/member/admin/GoodsAdd"
export const GoodsEdit = "/member/admin/GoodsEdit"
export const order = "/member/admin/order"
export const member2 = "/member/admin/Member"

const routes = [{
    path: MemberRootUrl,
    component: () => import('@/views/member/home'),
    redirect: Store,
    children: [
        {
            path: Store,
            component: () => import('@/views/member/Store')
        },
        {
            path: Home,
            component: () => import('@/views/member/admin/Home'),
            redirect: member2,
            children: [
                {
                    path: member2,
                    component: () => import('@/views/member/admin/Member')
                }, {
                    path: order,
                    component: () => import('@/views/member/order')
                }, {
                    path: GoodsList,
                    component: () => import('@/views/member/admin/GoodsList')
                }, {
                    path: GoodsAdd,
                    component: () => import('@/views/member/admin/GoodsAdd')
                }, {
                    path: GoodsEdit,
                    component: () => import('@/views/member/admin/GoodsEdit')
                },
            ]
        },
    ]
}
]
export default routes

