export const SYS = "/sys"
export const SYS_ROOT = "/sys/root"


export const SYS_LOGOUT = "/sys/logout"

export const ENUM_ROOT = "/sys/enum"
export const ENUM_INFO = "/sys/enum/info"

const routes = [
    {
        path: SYS,
        redirect: SYS_ROOT
    },
    {
        path: SYS_ROOT,
        component: () => import('@/views/sys/RootHome.vue')
    },
    {
        path: ENUM_ROOT,
        component: () => import('@/views/sys/EnumPage.vue'),
    },
    {
        path: ENUM_INFO,
        component: () => import('@/views/sys/info/EnumInfoPage.vue'),
    },
]
export default routes

