# TODO 后端组装树形结构, 前段组装, 每次请求一个子节点, 循环遍历,  path路径, json存储
def getTreeFromList(arr):
    root = []
    map_dic = {}
    for vo in arr:
        vo["children"] = []
        id_path = vo["fullPath"] + str(vo["id"]) + "/"
        map_dic[id_path] = vo
        if vo["fullPath"] not in map_dic:
            root.append(vo)
        else:
            map_dic[vo["fullPath"]]["children"].append(vo)
    return root


def get_tree(arr):
    root = []
    map_dic = {}
    for vo in arr:
        vo["children"] = []
        id_path = vo["path"] + str(vo["id"]) + "/"
        map_dic[id_path] = vo
        if vo["path"] not in map_dic:
            root.append(vo)
        else:
            map_dic[vo["path"]]["children"].append(vo)
    return root
