
# TODO 后端组装树形结构, 前段组装, 每次请求一个子节点, 循环遍历,  path路径, json存储


arr = [
    {"id": 1, "name": 1, 'parentId': 0},
    {"id": 1, "name": 1, 'parentId': 0},
]


def getList():
    arr = []
    for i in range(1, 20):
        # for i in range(20):
        arr.append({"id": i, "name": 1, 'parentId': i // 2})
    print(arr)
    return arr


def getTreeFromList(arr, p_name, c_name, root_val):
    root = []
    o_dict = {}
    arr2 = []
    for vo in arr:
        if root_val == vo.parentId:
            root.append(vo)
    for root_vo in root:
        root_vo.child = []
        for vo in arr:
            if root_vo.id == vo.parentId:
                root_vo.child.append(vo)


def getTreeFromList2(arr, path, c_name, root_val):
    ziduan = "fullPath"
    for i in range(len(arr) - 1):
        arr[i].child=[]
        if  arr[i].fullPath == arr[i + 1].fullPath:
            pass
        if not arr[i].fullPath == arr[i + 1].fullPath and arr[i + 1].fullPath.startswith(arr[i].fullPath):
            arr[i].child.append(arr[i+1])

        pass
    for vo in arr:
        pass


if __name__ == '__main__':
    print()
    getList()
