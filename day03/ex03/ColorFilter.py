import numpy as np


class ColorFilter():
    @staticmethod
    def invert(arr: np.array) -> np.array:
        """
        Takes a NumPy array of an image as an argument and returns an array with
        inverted color.
        """
        return 1 - arr

    @staticmethod
    def to_blue(arr: np.array) -> np.array:
        """
        Takes a NumPy array of an image as an argument and returns an array
        with a blue filter.
        """
        blue_arr = np.zeros(arr.shape, dtype=arr.dtype)
        blue_arr[:, :, 2] = arr[:, :, 2]
        return blue_arr

    @staticmethod
    def to_green(arr: np.array) -> np.array:
        """
        Takes a NumPy array of an image as an argument and returns an array 
        with a green filter.
        """
        green_arr = arr * [0, 1, 0]
        return green_arr

    def to_red(self, arr: np.array) -> np.array:
        """
        Takes a NumPy array of an image as an argument and returns an array
        with a red filter.
        """
        red_arr = arr - self.to_green(arr) - self.to_blue(arr)
        return red_arr

    @staticmethod
    def to_celluloid(arr: np.array, thresholds: int = 4) -> np.array:
        """
        Takes a NumPy array of an image as an argument, and returns an array
        with a celluloid shade filter. 
        """
        original_arr = np.copy(arr)
        celluloid_arr = np.copy(arr)
        if original_arr.dtype == 'uint8':
            celluloid_filter = np.linspace(
                0,
                255,
                num=thresholds,
                endpoint=False,
                dtype='uint8',
            )
        elif original_arr.dtype == 'float32':
            celluloid_filter = np.linspace(
                0.0,
                1.0,
                num=thresholds,
                endpoint=False,
                dtype='float32',
            )
        else:
            return arr
        print(celluloid_filter)
        for value in celluloid_filter:
            print(value)
            indexes = original_arr < value
            celluloid_arr[indexes] = value
            original_arr[indexes] = 255
        return celluloid_arr

    @staticmethod
    def to_grayscale(arr: np.array, filter: str = 'w') -> np.array:
        """
        Takes a NumPy array of an image as an argument and returns an array 
        in grayscale. 
        The method takes another argument to select between two possible 
        grayscale filters:
            – ‘mean’ or ‘m’ : array created from the mean of the RBG channels.
            – ‘weighted’ or ‘w’ : array in weighted grayscale.
        """
        if filter == 'mean' or filter == 'm':
            mean = np.sum(arr, 2, keepdims=True) / 3
            gray_mean = np.broadcast_to(mean, (arr.shape))
            return gray_mean.astype(arr.dtype)
        elif filter == 'weighted' or filter == 'w':
            w_mean = np.sum(
                arr * [0.299, 0.587, 0.114],
                2,
                dtype=arr.dtype,
                keepdims=True,
            )
            weighted = np.tile(w_mean, (1, 1, 3))
            return weighted
        return arr
