""""
Timing tools.
"""

import time

def timer(func, *args, **kwargs):
    "Times a function call and returns (result, time_elapsed)"
    start = time.time()
    result = func(*args, **kwargs)
    time_elapsed = time.time() - start
    
    return (result, time_elapsed)
