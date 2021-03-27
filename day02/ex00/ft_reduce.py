def ft_reduce(function_to_apply, list_of_inputs):
	"""Apply a function_to_apply to all of the list_of_inputs and returns a \
	single value"""
	first = list_of_inputs[0]	
	for item in list_of_inputs[1:]:
		first = function_to_apply(first, item)
	return first
