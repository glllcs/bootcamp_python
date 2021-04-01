from NumPyCreator import NumPyCreator
import numpy
from numpy import array


def test_NumPyCreator__from_list():
    npc = NumPyCreator()
    np_array = npc.from_list([[1, 2, 3], [6, 3, 4]])
    assert type(np_array) == numpy.ndarray
    assert np_array[0][0] == 1


def test_NumPyCreator__from_tuple():
    npc = NumPyCreator()
    np_array = npc.from_tuple(("a", "b", "c"))
    assert type(np_array) == numpy.ndarray
    assert np_array[0] == 'a'


def test_NumPyCreator__from_iterable():
    npc = NumPyCreator()
    np_array = npc.from_iterable(range(5))
    assert type(np_array) == numpy.ndarray
    assert np_array[0] == 0


def test_NumPyCreator__from_shape():
    npc = NumPyCreator()
    shape = [3, 5]
    np_array = npc.from_shape(shape)
    print(np_array)
    assert type(np_array) == numpy.ndarray
    assert np_array.shape == (3, 5)


def test_NumPyCreator__random():
    npc = NumPyCreator()
    shape = (3, 5)
    np_array = npc.random(shape)
    assert type(np_array) == numpy.ndarray
    assert np_array.shape == (3, 5)


def test_NumPyCreator__identity():
    npc = NumPyCreator()
    np_array = npc.identity(4)
    assert type(np_array) == numpy.ndarray
    assert np_array[0][0] == 1.0
