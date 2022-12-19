export const AdminUrl = "/videoAdmin"
export const ReviewWorks = "/videoAdmin/ReviewWorks"
export const ReviewTarget = "/videoAdmin/ReviewTarget"

const routes = [
    {
        path: AdminUrl,
        component: () => import('@/views/videoAdmin/Home'),
        redirect: ReviewWorks,
        children: [
            {
                path: ReviewWorks,
                component: () => import('@/views/videoAdmin/ReviewWorks'),
            },
            {
                path: ReviewTarget,
                component: () => import('@/views/videoAdmin/ReviewTarget'),
            },
        ]
    }
]
export default routes

