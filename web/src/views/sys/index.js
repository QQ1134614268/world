import {
    FoodInfo, GoodsAdd, GoodsEdit,
    GoodsList,
    HomeContent,
    MemberAdminHome,
    MemberRootUrl, Order,
    order, Qrcode,
    Store,
    UserSpace
} from "@/views/member";

export const SYS_HOME = '/'
export const SYS_LOGIN_URL = "/sys/login"
export const SYS_REGISTER_URL = "/sys/register"
export const SYS_LOGOUT = "/sys/logout"
export const SYS_ROOT = "/sys/root"
export const ROOT = "/root"
export const ENUM_ROOT = "/sys/enum"
export const ENUM_INFO = "/sys/enum/info"

const routes = [
    {
        path: ENUM_INFO,
        component: () => import('@/views/sys/info/EnumInfoPage.vue'),
    },
]
export default routes

