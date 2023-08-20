import time

def log(fn):
    def wrapper(*args, **kwargs):
        start = time.time()
        fn(*args, **kwargs)
        end = time.time()
        a = end - start
        b = str(fn.__name__)
        arg_str = ', '.join(f'{k}={v}' for k,v in zip(fn.__code__.co_varnames, args))
        kwarg_str = ', '.join(f'{k}={v}' for k,v in kwargs.items())
        if len(kwarg_str) > 0:
            log_text = str(f'{b}; args: {arg_str}; kwargs: {kwarg_str}; execution time: {a:.2f} sec')
        else:
            log_text = str(f'{b}; args: {arg_str}; execution time: {a:.2f} sec')
        # print(log_text)
        with open('log.txt', 'w') as log_file:
            log_file.write(log_text)
        return fn(*args, **kwargs)
    return wrapper
    pass

# @log
# def foo(a, b, c):
#     return a+b+c
#
# foo(1, 2, c=3)