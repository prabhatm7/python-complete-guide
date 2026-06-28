import random

a= random.random()
print(a)

a = random.uniform(1, 10)
print(a)

a = random.randint(1, 10)
print(a)

a = random.choice([1, 2, 3, 4, 5])
print(a)

mylist = list("ABCDEFGH")
a = random.choice(mylist)
print(a)

a= random.sample(range(100), 10)
print(a)

a = random.shuffle(mylist)
print(mylist)

# reproduce with seed
random.seed(42)
print(random.random())
print(random.randint(1, 50))


# better use secrets 
import secrets
a = secrets.randbelow(10)
b = secrets.randbits(4)
c = secrets.choice([1, 2, 3, 4, 5])

print(a, b, c, sep=", ")


import numpy as np
a = np.random.randint(0,10,3)
print(a)

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
np.random.shuffle(arr)
print(arr)
