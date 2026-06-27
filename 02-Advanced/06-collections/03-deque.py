from collections import deque

# fast operations on both ends
d = deque([1, 2, 3])
d.append(4)
d.appendleft(0)
print(d)

d.pop()
d.popleft()
print(d)

# keep only the last few items
recent = deque(maxlen=3)
for i in range(6):
    recent.append(i)

print(recent)
