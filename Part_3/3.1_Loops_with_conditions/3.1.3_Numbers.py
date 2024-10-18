# Programming exercise: Numbers
# https://programming-24.mooc.fi/part-3/1-loops-with-conditions
#
# Please write a program which asks the user for a number. 
# The program then prints out all integer numbers greater than zero but smaller than the input.
#
# Sample output:
# Upper limit: 5
# 1
# 2
# 3
# 4

ul = int(input("Upper limit: "))
num = 1

while ul > 0 and num < ul:
    print(num)
    num += 1
