export const MemberRootUrl = "/member"
export const member2 = "/member/Member"
export const GoodsList = "/member/Home/GoodsList"
export const GoodsAdd = "/member/Home/GoodsAdd"
export const GoodsEdit = "/member/Home/GoodsEdit"
export const Store = "/member/Home/Store"
export const order = "/member/Home/order"
export const Home = "/member/Home"

const routes = [{
    path: MemberRootUrl,
    name: MemberRootUrl,
    component: () => import('@/views/member/home'),
    redirect: Store,
    children: [
        {
            path: Store,
            name: Store,
            component: () => import('@/views/member/Store')
        },
        {
            path: Home,
            name: Home,
            component: () => import('@/views/member/admin/Home'),
            children: [
                {
                    path: member2,
                    name: member2,
                    component: () => import('@/views/member/admin/Member')
                }, {
                    path: order,
                    name: order,
                    component: () => import('@/views/member/order')
                }, {
                    path: GoodsList,
                    name: GoodsList,
                    component: () => import('@/views/member/admin/GoodsList')
                }, {
                    path: GoodsAdd,
                    name: GoodsAdd,
                    component: () => import('@/views/member/admin/GoodsAdd')
                }, {
                    path:GoodsEdit,
                    name: GoodsEdit,
                    component: () => import('@/views/member/admin/GoodsEdit')
                },
            ]
        },
    ]
}
]
export default routes

