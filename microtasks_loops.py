for x in range(1,8):
    if x == 4:
        continue
    print(x)
print("end of loop microtask1")
for y in range(1,11):
    if y == 6:
        break
    print(y)
print("end of microtask2")
total = 0
for n in range(1,5):
    total += n
    print(total)
