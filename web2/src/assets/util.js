export function toTree(arr) {
    let ret = {}
    for (let i = 0; i < arr.length; i++) {
        if (ret[arr[i].type]) {
            ret[arr[i].type].push(arr[i])
        } else {
            ret[arr[i].type] = [arr[i]]
        }
    }
}