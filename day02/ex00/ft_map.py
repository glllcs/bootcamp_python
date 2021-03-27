def ft_map(function_to_apply, list_of_inputs):
	"""Executes a specified function_to_apply for each item in list_of_inputs. 
	The item is sent to the function as a parameter."""
	for item in list_of_inputs:
		yield function_to_apply(item)
