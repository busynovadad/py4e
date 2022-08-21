import re
handle = open('regex_sum_1596276.txt')
mystr = handle.read()
print(mystr)
# s = mystr.split()
# print(s)
t = re.findall('[\d]+', mystr)
print(t)
summed = 0
for a in t:
    summed = summed + int(a)
    # if a.is_integer():
    #     print('yay')
    # sum
# z = sum(t)
# print(z)
print(summed)
