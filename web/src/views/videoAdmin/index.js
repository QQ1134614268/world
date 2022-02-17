export const AdminUrl = "/videoAdmin"
export const ReviewWorks = "/videoAdmin/ReviewWorks"
export const ReviewTarget = "/videoAdmin/ReviewTarget"

const routes = [
    {
        path: AdminUrl,
        name: AdminUrl,
        component: () => import('@/views/videoAdmin/Home'),
        redirect: ReviewWorks,
        children: [
            {
                path: ReviewWorks,
                name: ReviewWorks,
                component: () => import('@/views/videoAdmin/ReviewWorks'),
            },
            {
                path: ReviewTarget,
                name: ReviewTarget,
                component: () => import('@/views/videoAdmin/ReviewTarget'),
            },
        ]
    }
]
export default routes

