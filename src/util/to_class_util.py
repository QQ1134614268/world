def to_class(data, clz):
    if isinstance(data, list):
        return list(map(lambda item: dict2class(item, clz), data))
    if isinstance(data, dict):
        return dict2class(data, clz)
    raise Exception("参数不正确")


def dict2class(data, clz):
    dic = {k: v for k, v in data.items() if k in clz.__dict__.keys()}
    return clz(**dic)
