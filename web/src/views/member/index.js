export const MemberRootUrl = "/member"
export const Store = "/member/Store"
export const Home = "/member/admin"
export const GoodsList = "/member/admin/GoodsList"
export const GoodsAdd = "/member/admin/GoodsAdd"
export const GoodsEdit = "/member/admin/GoodsEdit"
export const order = "/member/admin/order"
export const UserSpace = "/member/UserSpace"
export const OrderInfo = "/member/admin/OrderInfo"
export const UserAdmin = "/member/admin/UserAdmin"

const routes = [
    {
        path: MemberRootUrl,
        component: () => import('@/views/member/Home'),
        redirect: Store,
        children: [
            {
                path: Store,
                component: () => import('@/views/member/Store')
            },
            {
                path: Home,
                component: () => import('@/views/member/admin/Home'),
                redirect: UserAdmin,
                children: [
                    {
                        path: UserAdmin,
                        component: () => import('@/views/member/admin/UserAdmin')
                    },
                    {
                        path: order,
                        component: () => import('@/views/member/MyOrder')
                    },
                    {
                        path: OrderInfo,
                        component: () => import('@/views/member/OrderInfo')
                    },
                    {
                        path: GoodsList,
                        component: () => import('@/views/member/admin/GoodsList')
                    },
                    {
                        path: GoodsAdd,
                        component: () => import('@/views/member/admin/GoodsAdd')
                    },
                    {
                        path: GoodsEdit,
                        component: () => import('@/views/member/admin/GoodsEdit')
                    },
                ]
            },
            {
                path: UserSpace,
                component: () => import('@/views/member/UserSpace')
            }
        ]
    }
]
export default routes

