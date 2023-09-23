import time


def speed_calc_decorator(function):
    def wrapper_function():
        start = time.time()
        function()
        end = time.time()

        duration = end - start

        print(f"{function.__name__} run speed: {duration}")

    return wrapper_function


@speed_calc_decorator
def fast_function():
    time.sleep(3)


fast_function()


# @speed_calc_decorator
def slow_function():
    time.sleep(6)


# slow_function()

wrapper = speed_calc_decorator(slow_function)
wrapper()
