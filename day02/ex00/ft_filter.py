def ft_filter(function_to_apply, list_of_inputs):
	"""Returns an iterator were the items at list_of_inputs are filtered through 
	a function_to_apply """
	for item in list_of_inputs:
		if function_to_apply(item):
			yield item
