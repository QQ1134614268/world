export const CodeRootUrl = "/code"
export const CodeHome = "/code/CodeHome"

export const routes = [
    {
        path: CodeRootUrl,
        component: () => import('@/views/low_code/CodeHome.vue'),
        redirect: CodeHome,
        children: [
            {
                path: CodeHome,
                component: () => import('@/views/low_code/CodeHome.vue'),
            },
        ]
    },
]

export default routes
