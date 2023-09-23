import time


def func_speed_calc(function):
    def wrapper():
        start = time.time()
        function()
        end = time.time()

        print(f"{function.__name__} function speed: {end - start} seconds")
    return wrapper


@func_speed_calc
def slow_function():
    time.sleep(4)


slow_function()


@func_speed_calc
def fast_function():
    time.sleep(2)


fast_function()
