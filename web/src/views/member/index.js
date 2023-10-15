export const MemberRootUrl = "/member"
export const UserSpace = "/member/UserSpace"
export const Store = "/member/Store"
export const HomeContent = "/member/HomeContent"
export const MemberAdminHome = "/member/admin"
export const order = "/member/order"

export const GoodsList = "/member/admin/GoodsList"
export const Order = "/member/admin/Order"
export const GoodsAdd = "/member/admin/GoodsAdd"
export const GoodsEdit = "/member/admin/GoodsEdit"
export const Qrcode = "/member/admin/Qrcode"
export const FoodInfo = "/member/admin/OrderInfo"

const routes = [
    {
        path: MemberRootUrl,
        component: () => import('@/views/member/MemberApp.vue'),
        redirect: HomeContent,
        children: [
            {
                path: HomeContent,
                component: () => import('@/views/member/HomeInfo.vue')
            },
            {
                path: Store,
                component: () => import('@/views/member/Store')
            },
            {
                path: UserSpace,
                component: () => import('@/views/member/UserSpace')
            },
            {
                path: order,
                component: () => import('@/views/member/MyOrder')
            },
            {
                path: FoodInfo,
                component: () => import('@/views/member/FoodInfo.vue')
            },
        ],
    },
    {
        path: MemberAdminHome,
        component: () => import('@/views/member/admin/MemberAdminApp.vue'),
        redirect: GoodsList,
        children: [
            {
                path: GoodsList,
                component: () => import('@/views/member/admin/GoodsPage.vue')
            },
            {
                path: Order,
                component: () => import('@/views/member/admin/OrderPage.vue')
            },
            {
                path: GoodsAdd,
                component: () => import('@/views/member/admin/GoodsAdd')
            },
            {
                path: GoodsEdit,
                component: () => import('@/views/member/admin/GoodsEdit')
            },
            {
                path: Qrcode,
                component: () => import('@/views/member/admin/Qrcode')
            },
        ]
    },

]
export default routes

