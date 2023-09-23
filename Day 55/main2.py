def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        print(f"wrapper executed before {original_function.__name__}")
        return original_function(*args, **kwargs)
    return wrapper_function


@decorator_function
def display(name, age):
    print(f"{name}:{age}")


# decorated_display = decorator_function(display)
# decorated_display()

display("John", 22)
