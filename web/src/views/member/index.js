export const MemberRootUrl = "/member"
export const UserSpace = "/member/UserSpace"
export const Store = "/member/Store"
export const MemberAdminHome = "/member/admin"
export const order = "/member/order"

export const GoodsList = "/member/admin/GoodsList"
export const Order = "/member/admin/Order"
export const GoodsAdd = "/member/admin/GoodsAdd"
export const GoodsEdit = "/member/admin/GoodsEdit"
export const Qrcode = "/member/admin/Qrcode"
export const OrderInfo = "/member/admin/OrderInfo"
export const UserAdmin = "/member/admin/UserAdmin"
export const UserRole = "/member/admin/UserRole"
export const RolePermission = "/member/admin/RolePermission"
export const Finance = "/member/admin/Finance"

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
                path: UserSpace,
                component: () => import('@/views/member/UserSpace')
            },
            {
                path: order,
                component: () => import('@/views/member/MyOrder')
            },
            {
                path: OrderInfo,
                component: () => import('@/views/member/OrderInfo')
            },
        ],
    },
    {
        path: MemberAdminHome,
        component: () => import('@/views/member/admin/Home'),
        redirect: UserAdmin,
        children: [
            {
                path: UserAdmin,
                component: () => import('@/views/member/admin/UserAdmin')
            },
            {
                path: UserRole,
                component: () => import('@/views/member/admin/UserRole')
            },
            {
                path: Finance,
                component: () => import('@/views/member/admin/Finance')
            },
            {
                path: RolePermission,
                component: () => import('@/views/member/admin/RolePermission')
            },
            {
                path: GoodsList,
                component: () => import('@/views/member/admin/GoodsList')
            },
            {
                path: Order,
                component: () => import('@/views/member/admin/Order')
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

