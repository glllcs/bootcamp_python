import numpy as np
from typing import Tuple, Any, List


class NumPyCreator():
    @staticmethod
    def from_list(lst: List[Any]):
        return np.array(lst)

    @staticmethod
    def from_tuple(tpl: Tuple[Any]):
        return np.array(tpl)

    @staticmethod
    def from_iterable(itr):
        return np.array(itr)

    @staticmethod
    def from_shape(shape: Tuple[int, int], value: Any = 0):
        return np.full(shape=shape, fill_value=value)

    @staticmethod
    def random(shape: Tuple[int, int]):
        return np.random.rand(*shape)

    @staticmethod
    def identity(n):
        return np.identity(n)
