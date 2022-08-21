# 9.4 Write a program to read through the mbox-short.txt and figure out
# who has sent the greatest number of mail messages. The program looks
# for 'From ' lines and takes the second word of those lines as the
# person who sent the mail. The program creates a Python dictionary
# that maps the sender's mail address to a count of the number of times
# they appear in the file. After the dictionary is produced, the program
# reads through the dictionary using a maximum loop to find the most
# prolific committer.

# Desired Output
# cwen@iupui.edu 5
sender = dict()
# name = input("Enter file:")
# if len(name) < 1:
name = "/home/brad/mbox-short.txt"
handle = open(name)
count = 0
for line in handle:
    # print(line)
    if line.startswith("From "):
        words = line.split()
        # print(words[1])
        # s = words[1]
        # print(type(words[1]))
        # sender[s] = sender.get(s, 0) + 1
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
handle.close()




