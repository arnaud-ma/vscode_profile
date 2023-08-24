# This is a comment
"""
This is a docstring
"""

from abc import abstractmethod
import math as m

def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before function")
        result = func(*args, **kwargs)
        print("After function")
        return result
    return wrapper

@my_decorator
def my_func(parameter: int) -> float:
    """This is a function with a docstring"""
    return parameter * m.pi

async def async_func():
    pass

def a_non_async_func():
    pass

def my_generator():
    yield 1
    yield 2
    yield 3

class Foo:
    def __init__(self, bar):
        self.bar = bar
    @abstractmethod
    def abstract_method(self):
        pass

    def non_abstract_method(self):
        pass

try:
    foo = Foo()
except TypeError as e:
    print(f"Error: {e}")

assert my_func(2) == 6.28, "Wrong result"

my_list = [1, 2, 3]
my_dict = {"a": 1, "b": 2, "c": 3}
my_set = {1, 2, 3}

print(my_list[0])
print(my_dict["a"])
print(1 in my_set)

print(my_list + [4])
print(my_dict.update({"d": 4}))
print(my_set.union({4}))

name = "Alice"
age = 25

print("Hello, %s. You are %d years old." % (name, age))
print("Hello, {}. You are {} years old.".format(name, age))
print(f"Hello, {name}. You are {age} years old.")

def greet(name: str) -> None:
    """Greets a person by name"""
    print(f"Hello, {name}.")

greet("Bob")
