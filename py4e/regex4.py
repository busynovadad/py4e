import re
h = open('/home/brad/mbox-short.txt')
for line in h:
    line = line.rstrip()
    if re.findall('All', line):
        print(line)
h.close()




