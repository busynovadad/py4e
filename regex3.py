## one way
h = open('/home/brad/mbox-short.txt')
for line in h:
    line = line.rstrip()
    if line.startswith('From:'):
        print(line)
h.close()

import re
h = open('/home/brad/mbox-short.txt')
for line in h:
    line = line.rstrip()
    if re.search('^X-\S+', line):
        print(line)
h.close()

