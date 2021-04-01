from typing import Tuple, Any
import numpy as np


class ScrapBooker():
    @staticmethod
    def crop(
            arr: np.array,
            dimensions: Tuple[int, int],
            position: Tuple[int, int] = (0, 0),
    ) -> np.array:
        """
        Crops the image from arr as a rectangle with the given dimensions 
        (meaning, the new height and width for the image), whose top left corner
        is given by the position argument.
        """
        if (not isinstance(dimensions, Tuple)
                or not isinstance(dimensions[0], int)
                or not isinstance(dimensions[1], int)):
            raise TypeError("dimensions must be a tuple of int")
        if (not isinstance(position, Tuple)
                or not isinstance(position[0], int)
                or not isinstance(position[1], int)):
            raise TypeError("position must be a tuple of int")
        bottom_right = np.array(position) + np.array(dimensions)
        if (arr.shape[0] < bottom_right[0]) or (arr.shape[1] < bottom_right[1]):
            raise Exception(
                f"position out of range (arr shape is {arr.shape})")

        arr = arr[position[0]:bottom_right[0], position[1]:bottom_right[1]]
        return arr

    @staticmethod
    def thin(arr: np.array, n: int, axis: int) -> np.array:
        """
        Deletes every n-th pixel row along the specified axis
        (0 vertical, 1 horizontal) of arr.
        """
        indexes_to_delete_lst = list(filter(lambda x: (x+1) % n == 0, range(arr.shape[axis])))
        return np.delete(arr, indexes_to_delete_lst, axis)

    @staticmethod
    def juxtapose(arr: np.array, n: int, axis: int) -> np.array:
        """Juxtaposes n copies of the arr along the specified axis
        (0 vertical, 1 horizontal)."""
        arr_lst = [arr for __ in range(n)]
        return np.concatenate(arr_lst, axis)

    def mosaic(self, arr: np.array, dimensions: Tuple[int, int]) -> np.array:
        """
        Makes a grid with multiple copies of the array. 
        The dimensions argument specifies the dimensions (meaning the height
        and width) of the grid
        """
        arr = self.juxtapose(arr, dimensions[0], 0)
        arr = self.juxtapose(arr, dimensions[1], 1)
        return arr 
