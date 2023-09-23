def logging_decorator(function):
    def wrapper(*args, **kwargs):
        print(f"You called {function.__name__}{args}")
        return f"It returned: {function(*args, **kwargs)}"
    return wrapper


@logging_decorator
def add_numbers(*args, **kwargs):
    return sum(args)


print(add_numbers(1, 2, 3))
