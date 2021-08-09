const routes = [
    {
        path: '/hello/BgColor',
        name: '/hello/BgColor',
        component: () => import('@/views/hello/BgColor')
    },
    {
        path: '/hello/test_vue-cropper',
        name: '/hello/test_vue-cropper',
        component: () => import('@/views/hello/test_vue-cropper')
    },
    {
        path: '/hello/home',
        name: '/hello/home',
        component: () => import('@/views/hello/TestHome')
    },
    {
        path: '/hello/check',
        name: '/hello/check',
        component: () => import('@/views/hello/check')
    },
    {
        path: '/hello/test_input',
        name: '/hello/test_input',
        component: () => import('@/views/hello/test_input')
    },
    {
        path: '/hello/hello',
        name: '/hello/hello',
        component: () => import('@/views/hello/Hello')
    },
    {
        path: '/hello/test_component',
        name: '/hello/test_component',
        component: () => import('@/views/hello/test_component')
    },
    {
        path: '/hello/test_vuex',
        name: '/hello/test_vuex',
        component: () => import('@/views/hello/vuex_test/Parent')
    },
    {
        path: '/hello/test_popup',
        name: '/hello/test_popup',
        component: () => import('@/views/hello/test_popup')
    },
    {
        path: '/hello/TestWordStyle',
        name: '/hello/TestWordStyle',
        component: () => import("@/views/hello/TestWordStyle.vue")
    }, {
        path: '/hello/test_echarts',
        name: '/hello/test_echarts',
        component: () => import('@/views/hello/test_echarts')
    }, {
        path: '/hello/flex-test',
        name: '/hello/flex-test',
        component: () => import('@/views/hello/flex-test')
    }, {
        path: '/hello/test_search',
        name: '/hello/test_search',
        component: () => import('@/views/hello/test_search')
    }, {
        path: '/hello/test_search_page',
        name: '/hello/test_search_page',
        component: () => import('@/views/hello/test_search_page')
    }, {
        path: '/hello/test',
        name: '/hello/test',
        component: () => import('@/views/hello/test')
    },
]
export default routes

