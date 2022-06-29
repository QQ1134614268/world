//测试
export const CodeUrl = "/code/code"

const routes = [
    {
        path: CodeUrl,
        component: () => import('@/views/code/Code')
    }
]
export default routes

