//人人影
export const ROOT_URL = "/"
export const RenrenRootUrl = "/video"
export const UserInfoUrl = "/video/UserInfo"
export const VideoRegisterUrl = "/video/register"
export const TargetInfoUrl = "/video/TargetInfo"
export const WorksUrl = "/video/works"
export const VideoLoginUrl = "/video/Login"
export const VIDEO_MARKET = "/video/market"
export const VIDEO_MARKET2 = "/video/Market2"
export const video_user = "/video/video_user"
export const InvitationCode = "/video/InvitationCode"
export const Setting = "/video/Setting"
export const UserInfo = "/video/UserInfo"
export const VideoUrl = "/video/video"
export const Video = "/video/Video"
export const Register = "/video/Register"
export const Login = "/video/Login"
export const UserInfo2 = "/video/UserInfo2"
export const TargetInfo = "/video/TargetInfo"
export const Target = "/video/Target"

export const routes = [
    {
        path: ROOT_URL,
        redirect: VIDEO_MARKET,
    },
    {
        path: RenrenRootUrl,
        name: RenrenRootUrl,
        component: () => import('@/views/video/videoHome'),
        redirect: VIDEO_MARKET,
        children: [
            {
                path: InvitationCode,
                name: InvitationCode,
                component: () => import('@/views/video/InvitationCode'),
            },
            {
                path: Setting,
                name: Setting,
                component: () => import('@/views/video/Setting'),
            }, {
                path: UserInfo,
                name: UserInfo,
                component: () => import('@/views/video/expert/UserInfo'),
            }, {
                path: Video,
                component: () => import('@/views/video/expert/Video'),
            }, {
                path: Register,
                component: () => import('@/views/video/Register'),
            }, {
                path: Login,
                component: () => import('@/views/video/Login'),
            }, {
                path: UserInfo2,
                component: () => import('@/views/video/sponsor/UserInfo2'),
            }, {
                path: TargetInfo,
                component: () => import('@/views/video/sponsor/TargetInfo'),
            }, {
                path: WorksUrl,
                component: () => import('@/views/video/expert/works'),
                meta: {
                    keepAlive: false,
                    login: true,
                    roles: ['VIDEO',],
                }
            }, {
                path:Target,
                component: () => import('@/views/video/sponsor/Target'),
                meta: {
                    keepAlive: false,
                    login: true,
                    roles: ['VIDEO',],
                }
            }, {
                path: VIDEO_MARKET,
                name: VIDEO_MARKET,
                component: () => import('@/views/video/expert/Market'),
                meta: {
                    keepAlive: false,
                    // login: true,
                    roles: ['VIDEO',],
                }
            }, {
                path: VIDEO_MARKET2,
                name: VIDEO_MARKET2,
                component: () => import('@/views/video/sponsor/Market2'),
                meta: {
                    keepAlive: false,
                    // login: true,
                    roles: ['VIDEO',],
                }
            }, {
                path: video_user,
                name:video_user,
                component: () => import('@/views/video/userspace'),
                meta: {
                    keepAlive: false,
                    login: true,
                    roles: ['VIDEO',],
                }
            },
        ]
    },
]

export default routes


