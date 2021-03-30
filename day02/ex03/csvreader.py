import csv

class CsvReader():
	def __init__(
		self, 
		filename=None, 
		sep=',', 
		header=False, 
		skip_top=0, 
		skip_bottom=0,
	):
		self.filename = filename
		self.sep = sep
		self.header = header
		self.skip_top = skip_top
		self.skip_bottom = skip_bottom
		self.file = None

	def __enter__(self):
		try:
			self.file = open(self.filename)
			self.content = csv.reader(self.file, delimiter=self.sep)
			self.data_list = [' | '.join(row) for row in self.content]
		except FileNotFoundError:
			return None
		return self
	
	def __exit__(self, exc_type, exc_value, exc_traceback):
		try:
			self.file.close()
		except AttributeError:
			return

	def getheader(self):
		return self.data_list[0]

	def getdata(self):
		row_start = 1 + self.skip_top
		row_end =  len(self.data_list) - self.skip_bottom

		data = ''
		if self.header:
			data = self.getheader() + '\n'
		data += '\n'.join(self.data_list[row_start:row_end])

		return data


	
if __name__ == "__main__":
	with CsvReader('./day02/ex03/good.csv') as file:
		if file == None:
			print("File is corrupted")
		else:
			print(file.getdata())
			print()
			print(file.getheader())
		print()

	with CsvReader('./day02/ex03/bad.csv') as file:
		if file == None:
			print("File is corrupted")
		else:
			print(file.getdata())
			print()
			print(file.getheader())
		print()
