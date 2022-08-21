stuff = dict()
# print(stuff['thing'])
print(stuff.get('thing', -1))
print(stuff.get('thing2', -1))
print(stuff.get('thing3', -1))
for s in stuff:
    print(s)

j = {'chuck': 11, 'fred': 22, 'george': 33}
print(j.keys())
print(j.values())
k = {}
print(k.keys())
print(j.items())

for a, b in j.items():
    print(a, 'is', b)

name = input('Enter file:')
if len(name) < 1:
    name = '/home/brad/testfile.txt'
handle = open(name)

counts = dict()
for line in handle:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
print(counts.items())
bigcount = None
bigword = None
for word, count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count

print(bigword, bigcount)



