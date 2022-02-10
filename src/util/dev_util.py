import random
import string
from enum import Enum

from util.time_util import get_now_str


def get_comment(t_enum: Enum):
    return "枚举值: " + " ".join(
        [f'{name}:{member.value};' for name, member in t_enum.__members__.items()])


def create_data(datatype, length):
    if datatype == "String" or datatype == "string":
        return ''.join(random.sample(string.ascii_letters + string.digits, length))
    if datatype == "Time" or datatype == "time":
        return get_now_str()
    if datatype == "Int" or datatype == "int":
        return random.randint(10 ** (length - 1), 10 ** length - 1)
    if datatype == "Float" or datatype == "float":
        return float(random.randint(10 ** (length - 1), 10 ** length - 1) / 100)


if __name__ == '__main__':
    for i in range(1, 10):
        print(create_data("string", 10))
        print(create_data("time", 10))
        print(create_data("int", 10))
        print(create_data("float", 10))
