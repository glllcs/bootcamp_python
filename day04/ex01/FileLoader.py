import pandas as pd
from pandas import DataFrame

class FileLoader():
	@staticmethod
	def load(csv_path: str) -> DataFrame:
		"""
		Takes as an argument the file path of a csv to load, displays a message
		specifying the dimensions of the dataset and returns the dataset loaded
		as a pandas.DataFrame.
		"""
		df = pd.read_csv(csv_path)
		row, col = df.shape
		print(f'Loading dataset of dimensions {row} x {col}')
		return df

	@staticmethod
	def display(df: DataFrame, n: int):
		"""
		Takes a pandas.DataFrame and an integer as arguments, displays the first
		n rows of the dataset if n is positive, or the last n rows if n is
		negative.
		"""
		if n >= 0:
			print(df.head(n))
		else:
			print(df.tail(-n))
