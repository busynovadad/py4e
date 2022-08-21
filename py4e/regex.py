## one way
h = open('/home/brad/mbox-short.txt')
for line in h:
    line = line.rstrip()
    if line.find('From:') >= 0:
        print(line)
h.close()

import re
h = open('/home/brad/mbox-short.txt')
for line in h:
    line = line.rstrip()
    if re.search('From:', line):
        print(line)
h.close()

