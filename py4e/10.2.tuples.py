# 10.2 Write a program to read through the mbox-short.txt and figure out the
# distribution by hour of the day for each of the messages. You can pull the
# hour out from the 'From ' line by finding the time and then splitting the
# string a second time using a colon.
#
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#
# Once you have accumulated the counts for each hour, print out the counts,
# sorted by hour as shown below.
#
# Desired Output
# 04 3
# 06 1
# 07 1
# 09 2
# 10 3
# 11 6
# 14 1
# 15 2
# 16 4
# 17 2
# 18 1
# 19 1

# name = input("Enter file:")
# if len(name) < 1:
name = "/home/brad/mbox-short.txt"
sender = dict()
hours_dict = dict()
handle = open(name)
count = 0
for line in handle:
    # print(line)
    if line.startswith("From "):
        words = line.split()
        # print(words[5])
        time = words[5].split(":")
        # print(time[0])
        # print(words[1])
        # s = words[1]
        # print(type(words[1]))
        # sender[s] = sender.get(s, 0) + 1
        hours_dict[time[0]] = hours_dict.get(time[0], 0) + 1
        sender[words[1]] = sender.get(words[1], 0) + 1
        count += 1

# print("There were", count, "lines in the file with From as the first word")
# print(sender)
bigcount = None
bigword = None
for key, value in sender.items():
    if bigcount is None or value > bigcount:
        bigword = key
        bigcount = value
print(bigword, bigcount)
hours_lst = {}
hours_lst = hours_dict
for k, v in sorted(hours_lst.items()):
    print(k, v)
handle.close()










