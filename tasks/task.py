import time

def log(fn):
    def wrapper(*args, **kwargs):
        start = time.time()
        fn(*args, **kwargs)
        end = time.time()
        a = end - start
        b = str(fn.__name__)
        log_text = str(f'{b}; args: {args} ; kwargs: {kwargs}; execution time: {a:.2f} sec')
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