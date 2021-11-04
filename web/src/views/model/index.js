let ADD_PROVE = '/model/AddProve'
let ADD_STORY = '/model/AddStory'
let EDIT_STORY = '/model/EditStory'
let EDIT_PROVE = '/model/EditProve'
export {
    ADD_PROVE,
    ADD_STORY,
    EDIT_STORY,
    EDIT_PROVE,
}

const routes = [
    {
        path: '/model/object',
        name: '/model/object',
        component: () => import('@/views/model/classVO')
    },
    {
        path: '/model',
        name: '/model',
        component: () => import('@/views/model/Catalogue')
    },
    {
        path: '/model/AddProve',
        name: '/model/AddProve',
        component: () => import('@/views/model/AddProve')
    },
    {
        path: '/model/AddStory',
        name: '/model/AddStory',
        component: () => import('@/views/model/AddStory')
    },
    {
        path: '/model/EditBook',
        name: '/model/EditBook',
        component: () => import('@/views/model/EditBook')
    },
    {
        path: '/model/Book',
        name: '/model/Book',
        component: () => import('@/views/model/Book')
    },
    {
        path: '/model/Book2',
        name: '/model/Book2',
        component: () => import('@/views/model/Book2')
    },
    {
        path: '/model/Catalogue',
        name: '/model/Catalogue',
        component: () => import('@/views/model/Catalogue')
    },
    {
        path: '/model/Compare',
        name: '/model/Compare',
        component: () => import('@/views/model/Compare')
    },
]


export default routes

