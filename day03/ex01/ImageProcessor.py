import numpy as np
from matplotlib import pyplot as plt

class ImageProcessor():
	@staticmethod
	def load(path):
		img_arr = plt.imread(path)
		print(f'Loading image of dimensions {img_arr.shape[1]} x {img_arr.shape[0]}')
		return img_arr

	@staticmethod
	def display(arr):
		plt.imshow(arr)
