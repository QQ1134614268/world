const routes = [
    {
        path: '/admin',
        name: '/admin',
        component: () => import('@/views/admin/Home'),
        redirect: "/admin/Approve",
        children: [
            {
                path: 'Approve',
                name: 'Approve',
                component: () => import('@/views/admin/Approve'),
            },
            {
                path: 'Setting',
                name: 'Setting',
                component: () => import('@/views/admin/Setting'),
            },
        ]
    }
]
export default routes

