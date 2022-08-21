others = -1
for i in range(1, 3):
    print('i', i)
    for j in range(1, 2):
        print('j', j)
        if i == j:
            print('i==j')
            others += 1
    else:
        print('else')
        others += 1
    print('i loop')
print(others)
