"""def my_decorator(func):
    def wrapper():
        print("Before the function runs")
        func()
        print("After the function runs")
    return wrapper

@my_decorator #@my_decorator` is just shorthand for `say_hello = my_decorator(say_hello)
def say_hello():
    print("Hello!")

say_hello()"""

import time


def timer(func):

    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Execution time: {end_time - start_time:.4f} seconds")
        return result

    return wrapper
@timer
def slow_function():
    time.sleep(2)

slow_function()