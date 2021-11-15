# -*- coding:utf-8 -*-
"""
@Time: 2021/11/15
@Description:
"""
from dataclasses import dataclass, field
from multiprocessing import Pool
from typing import Any


@dataclass(order=True)
class PrioritizedItem:
    priority: int
    item: Any = field(compare=False)


def my_print(x):
    print(x)


if __name__ == "__main__":
    x = [1, 2, 3, 4, 5]

    pool = Pool()
    pool.map(my_print, x)
    pool.join()
    pool.close()
