from itertools import accumulate
import operator

# running totals and other cumulative results
numbers = [1, 2, 3, 4]
print(list(accumulate(numbers)))
print(list(accumulate(numbers, operator.mul)))
