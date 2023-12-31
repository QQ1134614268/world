//测试
export const HelloRootUrl = "/hello"
export const test_box = "/hello/test_box"
export const BgColor = '/hello/BgColor'

const routes = [
    {
        path: HelloRootUrl,
        component: () => import('@/views/hello/TestHome')
    },
    {
        path: test_box,
        component: () => import('@/views/hello/test_box')
    },
    {
        path: BgColor,
        component: () => import('@/views/hello/BgColor')
    },
    {
        path: '/hello/test_navmenu',
        component: () => import('@/views/hello/test_navmenu')
    },
    {
        path: '/hello/testHeader',
        component: () => import('@/views/hello/testHeader')
    },
    {
        path: '/hello/test_vue-cropper',
        component: () => import('@/components/WrdVueCropper')
    },
    {
        path: '/hello/home',
        component: () => import('@/views/hello/TestHome')
    },
    {
        path: '/hello/test_object_fit',
        component: () => import('@/views/hello/test_object_fit')
    },
    {
        path: '/hello/form_check',
        component: () => import('@/views/hello/test_form_check')
    },
    {
        path: '/hello/test_input',
        component: () => import('@/views/hello/test_form')
    },
    {
        path: '/hello/hello',
        component: () => import('@/views/hello/Hello')
    },
    {
        path: '/hello/test_component',
        component: () => import('@/views/hello/test_component')
    },
    {
        path: '/hello/test_popup',
        component: () => import('@/views/hello/test_popup')
    },
    {
        path: '/hello/test_echarts',
        component: () => import('@/views/hello/test_echarts')
    },
    {
        path: '/hello/test_search',
        component: () => import('@/views/hello/test_search')
    },
    {
        path: '/hello/test_search_page',
        component: () => import('@/views/hello/test_search_page')
    },
    {
        path: '/hello/test',
        component: () => import('@/views/hello/test')
    },
    {
        path: '/hello/test_upload',
        component: () => import('@/views/hello/test_upload')
    },
    {
        path: '/hello/parent_child/Parent',
        component: () => import('@/views/hello/parent_child/Parent')
    },
    {
        path: '/hello/test_img_highlight',
        component: () => import('@/views/hello/test_img_highlight')
    },
]
export default routes

