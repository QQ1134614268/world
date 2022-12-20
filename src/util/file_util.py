import json
import os
import shutil
import uuid

import yaml

from config.json_config import MyJsonEncoder


def get_file_name_by_uuid(file_name):
    return uuid.uuid1().hex + "." + file_name.split('.')[-1]


def prepare_path(file_path, remove=False):
    """

    :param file_path:
    :param remove:
    :return:
    """
    dic_path = os.path.dirname(file_path)
    if os.path.exists(dic_path):
        if remove:
            shutil.rmtree(dic_path)
    else:
        os.makedirs(dic_path)


class FileUtil:
    @staticmethod
    def to_json(data, file_path):
        content = json.dumps(data, ensure_ascii=False, cls=MyJsonEncoder, indent=2)
        with open(file_path, encoding="utf-8", mode='w') as f:
            f.write(content)

    @staticmethod
    def from_json(file_path):  # 转类
        return json.load(file_path)

    @staticmethod
    def to_yaml(dict_value, save_path):
        """dict保存为yaml"""
        with open(save_path, mode='w', encoding="utf-8") as file:
            file.write(yaml.dump(dict_value, allow_unicode=True))

    @staticmethod
    def from_yaml(yaml_path) -> dict:  # 转类
        with open(yaml_path, encoding="utf-8") as file:
            dict_value = yaml.load(file, Loader=yaml.FullLoader)
            return dict_value

    # TODO 暂不支持list
    @staticmethod
    def to_prop(data: dict, file_path):
        ret_list = FileUtil.__dict_to_prop(data)
        with open(file_path, encoding="utf-8", mode='w') as f:
            f.write("\n".join(ret_list))

    @staticmethod
    def from_prop(file_path):  # 分隔符
        with open(file_path, encoding="utf-8") as f:
            lines = f.readlines()
        new_list = []
        for line in lines:
            line = line.replace("\n", "")
            if line.strip() != "":
                new_list.append(line)
        root = {}
        for line in new_list:
            pos_num = line.find("=")
            arr = line[:pos_num].split(".")
            curr = root
            # 模拟文件夹, 根据路径,从根目录开始, 切换当前目录. 不存在时就创建
            for index, name in enumerate(arr):
                if index == len(arr) - 1:
                    curr[name] = line[pos_num + 1:]
                else:
                    curr = root.setdefault(name, {})
        return root

    @staticmethod
    def __dict_to_prop(data: dict, full_path="", ret=None) -> list:
        if ret is None:
            ret = []
        if full_path:
            full_path += "."
        #  todo 优化 拼接 .
        for k, v in data.items():
            if isinstance(v, dict):
                FileUtil.__dict_to_prop(v, f"{full_path}{k}", ret)
            else:
                ret.append(f"{full_path}{k}={v}")
        return ret

    # 只有值, 类似xmind, 目录结构
    @staticmethod
    def to_xmind(data, file_path, key):
        ret_list = FileUtil._handel_data(data, key=key)
        with open(file_path, encoding="utf-8", mode='w') as f:
            f.write("\n".join(ret_list))

    @staticmethod
    def _handel_data(data_list, level=0, ret=None, key="value"):
        if ret is None:
            ret = []
        if isinstance(data_list, dict):
            data_list = [data_list]

        for dic in data_list:
            line = level * "  " + dic.get(key)
            ret.append(line)
            if dic.get("children"):
                FileUtil._handel_data(dic.get("children"), level + 1, ret, key=key)
        return ret

    @staticmethod
    def from_xmind(file_path):
        with open(file_path, encoding="utf-8") as f:
            lines = f.readlines()
        vos = []
        for line in lines:
            line = line.replace("\n", "")
            if line.strip() != "":
                vos.append({
                    "value": line.lstrip(),
                    "space": len(line) - len(line.lstrip()),
                    "children": []
                })
        root = list(filter(lambda x: x.get("space") == 0, vos))
        for i in range(len(vos) - 1, -1, -1):
            vo = vos[i]
            for j in range(i - 1, -1, -1):
                vo2 = vos[j]
                if vo.get("space") > vo2.get("space"):
                    vo2.get("children").insert(0, vo)
                    break

        return root
