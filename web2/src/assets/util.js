export function toTree(arr) {
    let ret = []
    let tree = {}
    for (let i = 0; i < arr.length; i++) {
        let obj = arr[i]
        if (tree[obj.type] != undefined) {
            tree[obj.type].push(obj)
        }else {
            ret.push(arr[i].type)
        }
    }
}