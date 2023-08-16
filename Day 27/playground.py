# multiple positional arguments --> converts arguments into a tuple

def add(*args):
    return sum([num for num in args])


print(add(2, 3, 4))


# multiple keyworded arguments --> converts arguments into a dictionary

def calculate(n, **kwargs):
    n += kwargs["add"]
    n *= kwargs["multiply"]

    return n


print(calculate(2, add=3, multiply=5))


# try creating a class as this
class Car:
    def __init__(self, **kwargs):
        # self.make = kwargs["make"]
        # self.model = kwargs["model"]

        # benefit of using get: all kwargs argument are optional
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")


