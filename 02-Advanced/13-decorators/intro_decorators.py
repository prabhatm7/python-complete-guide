# Types 
# 1. function decorators
# 2. class decorators

import functools
# function decorators
def my_decorator(func):

    @functools.wraps(func) # preserves the identity of the original function
    def wrapper(*args, **kwargs):
        print("Something is happening before the function is called.")
        func(*args, **kwargs)
        total_sum = 0
        if isinstance(args[1], list):
            total_sum += sum(args[1])
        
        print("Something is happening after the function is called.")
        return total_sum
    return wrapper

@my_decorator
def say_hello(name:str, scores: list[int]= None, cities:list[str]=None):
    print(f"Hello! {name}")
    print(f"Cities: {cities}")

function = say_hello("Alice", [95, 88, 76], ['New York', 'Los Angeles'])
print(function)

# A decorator takes a function, wraps it inside another function, and returns the new function. 
# The returned function replaces the original one.

# class decorators
class CountCalls:
    def __init__(self, func):
        self.func = func
        self.num_calls = 0

    def __call__(self, *args, **kwargs):
        self.num_calls += 1
        print(f"This is executed {self.num_calls} times")
        return self.func(*args, **kwargs)

@CountCalls
def say_hello(name):
    print(f"Hello {name}")


say_hello("Alice")
say_hello("Bob")
say_hello("Charlie")
