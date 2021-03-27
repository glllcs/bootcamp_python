from ft_filter import ft_filter

def test_ft_filter():
	def is_even(number):
		if number % 2 == 0:
			return True
		else:
			return False

	numbers = list(range(20))

	my_filter = ft_filter(is_even, numbers)
	original_filter = filter(is_even, numbers)

	assert list(my_filter) == list(original_filter)
