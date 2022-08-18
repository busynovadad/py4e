others = -1
for i in range(1, 3):
    print(i)
    for j in range(1, 2):
        print(j)
        if i == j:
            others += 1
    else:
        others += 1
print(others)
