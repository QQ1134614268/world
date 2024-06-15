//用户空间
export const USER_LOGIN_URL = "/user/login"
export const USER_REGISTER_URL = "/user/register"
export const UserSpaceRootUrl = "/user/UserSpace"


export const routes = [
    {
        path: UserSpaceRootUrl,
        component: () => import('@/views/user/UserSpace.vue')
    },
    {
        path: USER_LOGIN_URL,
        component: () => import('@/views/user/login.vue')
    },
    {
        path: USER_REGISTER_URL,
        component: () => import('@/views/user/register.vue')
    },]
export default routes
