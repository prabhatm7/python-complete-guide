from typing import Literal
def greet(name: str, type : Literal["Hello", "Hi"]):
    print(f"{type} {name}")

greet("Prabhat", "Hello")
greet("Prabhat", "Good Morning") # no error just type hinting