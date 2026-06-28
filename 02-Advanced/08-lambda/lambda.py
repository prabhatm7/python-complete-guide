# lambda arguments: expression
add = lambda x, y : x + y
print(add(2, 3))  # 5

points = [(1, 2), (3, 1), (5, 4), (2, 3), [2,2]]
sorted_points = sorted(points, key=lambda point: point[1])  # sort by y-coordinate

print(sorted_points)

points.sort(key=lambda point: point[0], reverse=True)  # sort by x-coordinate
print(points)

# filter points with 5 as sum
five_sum = list(filter(lambda point : point[0] + point[1] == 4, points))
print(five_sum)

# map points to their sum
sums = list(map(lambda point : point[0] + point[1], points))
print(sums)

# reduce points to their total sum
from functools import reduce
total_sum = reduce(lambda acc, point : acc + point[0] + point[1], points, 0)
print(total_sum)