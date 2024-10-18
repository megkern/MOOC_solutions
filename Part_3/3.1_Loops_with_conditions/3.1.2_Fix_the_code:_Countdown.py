# Programming exercise: Fix the code: Countdown
# # https://programming-24.mooc.fi/part-3/1-loops-with-conditions
#
# The program below has some syntactic issues:
#
# print("Are you ready?")
# number = int(input("Please type in a number: "))
# while number = 0:
# print(number)
# print("Now!")
# Please fix it so that it prints out the following:
#
# Sample output
# Are you ready?
# Please type in a number: 5
# 5
# 4
# 3
# 2
# 1
# Now!

print("Are you ready?")
number = int(input("Please type in a number: "))
while number > 0:
    print(number)
    number -= 1
print("Now!")
