import time
from functools import wraps

def log(f):
    @wraps(f)
    def wrappper(*args, **kwargs):
        func_name = f.__name__.replace('_', ' ')
        func_name = func_name.title()
        start = time.time()
        result = f(*args, **kwargs)
        end = time.time()
        with open('./log_file.log', 'a') as opened_file:
            opened_file.write(f'(glllcs)Running: {func_name} \t\t' +
                              f'[ exec-time = {end - start:.3f} ms ]\n')
        return result
    return wrappper
