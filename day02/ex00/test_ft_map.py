from ft_map import ft_map

def test_ft_map():
	def multiply_by_two(number):
		return number * 2	

	numbers = list(range(10))
	my_map = ft_map(multiply_by_two, numbers)
	original_map = map(multiply_by_two, numbers)

	assert list(my_map) == list(original_map)
