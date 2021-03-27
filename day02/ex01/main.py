def what_are_the_vars(*args, **kwargs): 
	"""Returns an object with the right attributes"""
	vars_list = ObjectC()
	for key in kwargs:
		setattr(vars_list, key, kwargs[key])
	for x in range(len(args)):
		key = f'var_{x}'
		if key in dir(vars_list):
			return None
		setattr(vars_list, key, args[x])
	return vars_list

class ObjectC(object): 
	def __init__(self):
		pass

def doom_printer(obj): 
	if obj is None:
		print("ERROR")
		print("end")
		return
	for attr in dir(obj): 
		if attr[0] != '_':
			value = getattr(obj, attr)
			print("{}: {}".format(attr, value))
	print("end")

if __name__ == "__main__":
	obj = what_are_the_vars(7)
	doom_printer(obj)
	obj = what_are_the_vars("ft_lol", "Hi")
	doom_printer(obj)
	obj = what_are_the_vars() #end
	doom_printer(obj)
	obj = what_are_the_vars(12, "Yes", [0, 0, 0], a=10, hello="world")
	doom_printer(obj)
	obj = what_are_the_vars(42, a=10, var_0="world")
	doom_printer(obj)
