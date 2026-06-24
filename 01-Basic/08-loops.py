# for loop
print("for loop")
for i in range(1,6):
    print(i)

# while loop
print("while loop")
i = 1
while i <= 6:
    print(i)
    i += 1

# break
print("break")
i = 1
while i <= 10:
    if i == 3:
        break
    print(i)
    i += 1

# continue
print("continue")
for i in range(1,6):
    if i == 3:
        continue
    print(i)

