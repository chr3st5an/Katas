from __future__ import annotations

from typing import Any, Callable
from functools import reduce


class callchain(object):
    def __init__(self, __func: Callable, *, is_root: bool = True) -> None:
        self.__func    = __func
        self.__is_root = is_root
        self.__chain   = []

    def __call__(self, *args, called_by_root: bool = False, **kwargs) -> Any:
        res = self.__func(*args, **kwargs)

        if self.__is_root or called_by_root:
            res = reduce(lambda x, y: y(x, called_by_root=True), self.__chain, res)

        return res

    def callback(self, priority: int) -> Callable:
        def wrapper(__func: Callable) -> callchain:
            subchain = callchain(__func, is_root=False)

            if isinstance(priority, int):
                self.__chain[priority:priority] = [subchain]
            else:
                self.__chain.append(subchain)

            return subchain

        return wrapper(priority) if callable(priority) else wrapper
