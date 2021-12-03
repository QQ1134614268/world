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
        path: '/tree',
        name: '/tree',
        component: () => import('@/views/model/treeHome'),
        redirect: '/tree/Catalogue',
    },
    {
        path: '/tree',
        name: '/tree',
        component: () => import('@/views/model/treeHome'),
        redirect: '/tree/Catalogue',
        children: [
            {
                path: 'Catalogue',
                name: 'Catalogue',
                components: {
                    tree: () => import('@/views/model/Catalogue'),
                    default: () => import('@/views/model/Catalogue')
                    //    todo test <router-view  name="tree"/>
                }
            },
            {
                path: 'Story',
                name: 'Story',
                component: () => import('@/views/model/Story')
            },
            {
                path: 'AddProve',
                name: 'AddProve',
                component: () => import('@/views/model/AddProve')
            },
            {
                path: 'AddStory',
                name: 'AddStory',
                component: () => import('@/views/model/AddStory')
            },
            {
                path: 'EditBook',
                name: 'EditBook',
                component: () => import('@/views/model/EditBook')
            },
            {
                path: 'Book',
                name: 'Book',
                component: () => import('@/views/model/Book')
            },
            {
                path: 'Book2',
                name: 'Book2',
                component: () => import('@/views/model/Book2')
            },
            {
                path: 'Compare',
                name: 'Compare',
                component: () => import('@/views/model/Compare')
            },
            {
                path: 'Parent',
                name: 'Parent',
                component: () => import('@/views/model/Parent')
            },
            {
                path: 'KeyWord',
                name: 'KeyWord',
                component: () => import('@/views/model/components/KeyWord')
            },
            {
                path: 'MuchChildren',
                name: 'MuchChildren',
                component: () => import('@/views/model/components/MuchChildren')
            },
            {
                path: 'PopularWord',
                name: 'PopularWord',
                component: () => import('@/views/model/components/PopularWord')
            },
        ]
    },
]


export default routes

