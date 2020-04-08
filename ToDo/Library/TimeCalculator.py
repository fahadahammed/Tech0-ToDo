import functools
import time
import logging


def TimeCalculator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()  # Alternatively, you can use time.process_time()
        func_return_val = func(*args, **kwargs)
        end = time.perf_counter()
        timeit_message = 'Time Took: {0:<10}.{1:<8} : {2:<8} Seconds'.format(func.__module__, func.__name__, end - start)
        logging.warning(timeit_message)
        return func_return_val
    return wrapper
