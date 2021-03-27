from functools import reduce
from ft_reduce import ft_reduce


def test_ft_reduce__multiply():
	def multiply(a, b):
		return a*b

	numbers = list(range(1, 10))
	my_reduce = ft_reduce(multiply, numbers)
	original_reduce = reduce(multiply, numbers)
	assert my_reduce == original_reduce 


def test_ft_reduce__sum():
	numbers = list(range(10))
	sum_nbrs = lambda x, y: x+y
	my_reduce = ft_reduce(sum_nbrs, numbers)
	original_reduce = reduce(sum_nbrs, numbers)
	assert my_reduce == original_reduce 


def test_ft_reduce__one_item():
	numbers = [1] 
	sum_nbrs = lambda x, y: x+y
	my_reduce = ft_reduce(sum_nbrs, numbers)
	original_reduce = reduce(sum_nbrs, numbers)
	assert my_reduce == original_reduce 
