import numpy as np
from matplotlib import pyplot as plt


class ImageProcessor():
    @staticmethod
    def load(path):
        img_arr = plt.imread(path)
        row, col, __ = img_arr.shape
        print(f'Loading image of dimensions {col} x {row}')
        if img_arr.shape[2] == 4:
            img_arr = img_arr[:, :, :3]
        return img_arr

    @staticmethod
    def display(arr):
        plt.imshow(arr, interpolation='nearest')
        plt.axis('off')
