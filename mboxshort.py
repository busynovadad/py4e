#  7.2 Write a program that prompts for a file name, then opens that file
#  and reads through the file, looking for lines of the form:
#
# X-DSPAM-Confidence:    0.8475
#
# Count these lines and extract the floating point values from each of the
# lines and compute the average of those values and produce an output as
# shown below. Do not use the sum() function or a variable named sum in your solution.
#
# You can download the sample data at http://www.py4e.com/code3/mbox-short.txt
# when you are testing below enter mbox-short.txt as the file name.
# Average spam confidence: 0.7507185185185187

# Use the file name mbox-short.txt as the file name
# fname = input("Enter file name: ")
fname = '/home/brad/mbox-short.txt'
fh = open(fname)
line_count = 0
line_match_count = 0
line_sums = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        line_count += 1
        continue
    else:
        loc1 = line.find(":") + 1
        text2 = line[loc1:]
        i = float(text2.strip())
        # print(i)
        line_sums += i
        line_match_count += 1
        # print(line)
# print("Done")
# print('count:', line_count)
# print('matched count:', line_match_count)
# print('line sums:', line_sums)
line_avg = line_sums / line_match_count
print('Average spam confidence:', line_avg)







