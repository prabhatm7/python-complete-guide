from typing import Optional
class Person:
    name : str = "Unknown"
    age : Optional[float] = 0.0

    def __init__(self, name : str = "Rahul"):
        self.name = name
    
    def greet(self):
        print(f"Hello, I am {self.name}")

p = Person("Prabhat")
p.greet()

p1 = Person()
p1.greet()