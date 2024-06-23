//真实之树
export const TreeRootUrl = "/tree"
let ADD_PROVE = '/tree/AddProve'
let ADD_STORY = '/tree/AddStory'
let EDIT_STORY = '/tree/EditStory'
let EDIT_PROVE = '/tree/EditProve'
export {
    ADD_PROVE,
    ADD_STORY,
    EDIT_STORY,
    EDIT_PROVE,
}

const routes = [
    {
        path: '/tree',
        name: '/tree',
        component: () => import('@/views/tree/treeHome'),
        redirect: '/tree/Catalogue',
        children: [
            {
                path: 'Catalogue',
                name: 'Catalogue',
                components: {
                    tree: () => import('@/views/tree/Catalogue'),
                    default: () => import('@/views/tree/Catalogue')
                }
            },
            {
                path: 'Story',
                name: 'Story',
                component: () => import('@/views/tree/Story')
            },
            {
                path: 'AddProve',
                name: 'AddProve',
                component: () => import('@/views/tree/AddProve')
            },
            {
                path: 'AddStory',
                name: 'AddStory',
                component: () => import('@/views/tree/AddStory')
            },
            {
                path: 'EditBook',
                name: 'EditBook',
                component: () => import('@/views/tree/EditBook')
            },
            {
                path: 'Book',
                name: 'Book',
                component: () => import('@/views/tree/Book')
            },
            {
                path: 'Book2',
                name: 'Book2',
                component: () => import('@/views/tree/Book2')
            },
            {
                path: 'Compare',
                name: 'Compare',
                component: () => import('@/views/tree/Compare')
            },
            {
                path: 'Parent',
                name: 'Parent',
                component: () => import('@/views/tree/Parent')
            },
            {
                path: 'KeyWord',
                name: 'KeyWord',
                component: () => import('@/views/tree/components/KeyWord')
            },
            {
                path: 'MuchChildren',
                name: 'MuchChildren',
                component: () => import('@/views/tree/components/MuchChildren')
            },
            {
                path: 'PopularWord',
                name: 'PopularWord',
                component: () => import('@/views/tree/components/PopularWord')
            },
        ]
    },
]


export default routes
