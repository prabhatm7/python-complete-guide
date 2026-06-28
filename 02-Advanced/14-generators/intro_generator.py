def mygenerator():
    yield 1
    yield 2
    yield 3 

g = mygenerator()

# print(sum(g))

value = next(g)
print(value)

value = next(g)
print(value)

value = next(g)
print(value)

# value = next(g) # error StopIteration

import sys

def firstn(n):
    nums = []
    num = 0
    while num < n:
        nums.append(num)
        num += 1
    return nums

def firstn_generator(n): # memory efficient
    num = 0
    while num < n:
        yield num
        num +=1


print(sys.getsizeof(firstn(1000000))) # 8448728
print(sys.getsizeof(firstn_generator(1000000))) # 112


def fibbonacci(limit):
    a, b = 0,1
    while a < limit:
        yield a 
        a , b = b , a + b

fib = fibbonacci(5)
for i in fib:
    print(i)


mylist = [i for i in range(100000) if i %2 == 0]
print(sys.getsizeof(mylist))

mygenerator = (i for i in range(100000) if i%2 == 0)
print(sys.getsizeof(mygenerator))
# print(list(mygenerator))