from ScrapBooker import ScrapBooker
import numpy as np

sb = ScrapBooker()


def test_ScrapBooker__crop():
    arr = np.arange(30).reshape(3, 10)
    crop_arr = sb.crop(arr, (1, 3), (2, 5))
    expected = np.array(((25, 26, 27), ))
    assert (crop_arr == expected).all()
    assert crop_arr.shape == expected.shape


def test_ScrapBooker__thin():
    arr = np.arange(30).reshape(3, 10)
    thin_arr = sb.thin(arr, 2, 1)
    expected = np.array((
        (0, 2, 4, 6, 8),
        (10, 12, 14, 16, 18),
        (20, 22, 24, 26, 28),
    ))
    assert (thin_arr == expected).all()
    assert thin_arr.shape == expected.shape


def test_ScrapBooker__juxtapose():
    arr = np.arange(10).reshape(2, 5)
    juxt_arr = sb.juxtapose(arr, 2, 1)
    expected = np.array((
        (0, 1, 2, 3, 4, 0, 1, 2, 3, 4),
        (5, 6, 7, 8, 9, 5, 6, 7, 8, 9),
    ))
    assert (juxt_arr == expected).all()
    assert juxt_arr.shape == expected.shape


def test_ScrapBooker__mosaic():
    arr = np.arange(6).reshape(2, 3)
    mosaic_arr = sb.mosaic(arr, (3, 2))
    expected = np.array((
        (0, 1, 2, 0, 1, 2),
        (3, 4, 5, 3, 4, 5),
        (0, 1, 2, 0, 1, 2),
        (3, 4, 5, 3, 4, 5),
        (0, 1, 2, 0, 1, 2),
        (3, 4, 5, 3, 4, 5),
    ))
    assert (mosaic_arr == expected).all()
    assert mosaic_arr.shape == expected.shape
