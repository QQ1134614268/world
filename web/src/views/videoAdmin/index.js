const routes = [
    {
        //todo video/admin??
        path: '/videoAdmin',
        name: '/videoAdmin',
        component: () => import('@/views/videoAdmin/Home'),
        redirect:'/videoAdmin/ReviewWorks',
        children: [
            {
                path: 'ReviewWorks',
                name: 'ReviewWorks',
                component: () => import('@/views/videoAdmin/ReviewWorks'),
            },
            {
                path: 'ReviewTarget',
                name: 'ReviewTarget',
                component: () => import('@/views/videoAdmin/ReviewTarget'),
            },
        ]
    }
]
export default routes

