from collections import namedtuple

# lightweight tuple with named fields
Point = namedtuple("Point", ["x", "y"])
p = Point(3, 4)
print(p.x, p.y)
print(p._asdict())

# create a new value with one field changed
p2 = p._replace(x=10)
print(p2)

x, y = p
print(x, y)

for i in p:
    print(i)