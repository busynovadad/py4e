# 5.2 Write a program that repeatedly prompts a user for integer numbers
# until the user enters 'done'. Once 'done' is entered, print out the largest
# and smallest of the numbers. If the user enters anything other than a valid
# number catch it with a try/except and put out an appropriate message and
# ignore the number. Enter 7, 2, bob, 10, and 4 and match the output below.
# Invalid input
# Maximum is 10
# Minimum is 2

largest = 0
smallest = 0
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try:
        inum = int(num)
        if largest == 0 and smallest == 0:
            largest = inum
            smallest = inum
        elif inum > largest:
            largest = inum
        elif inum < smallest:
            smallest = inum
        # print(inum)
    except ValueError:
        print("Invalid input")

print("Maximum is", largest)
print("Minimum is", smallest)
