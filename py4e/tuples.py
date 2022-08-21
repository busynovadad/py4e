# fhand = open('/home/brad/juliet.txt')
fhand = open('/home/brad/mbox-short.txt')
counts = {}
for line in fhand:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

lst = []
for key, val in counts.items():
    newtup = (val, key)
    lst.append(newtup)
# print(lst)
lst = sorted(lst, reverse=True)
# print(lst)
for val, key in lst[:10]:
    print(key, val)

print(sorted([(v, k) for k, v in counts.items()], reverse=True))
