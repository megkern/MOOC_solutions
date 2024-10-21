# Programming exercise: Multiplication
# https://programming-24.mooc.fi/part-3/3-more-loops
#
# Please write a program which asks the user for a positive integer number. The program then prints out a list of 
# multiplication operations until both operands reach the number given by the user. See the examples below for details:
# Sample output:
# Please type in a number: 2
# 1 x 1 = 1
# 1 x 2 = 2
# 2 x 1 = 2
# 2 x 2 = 4

max = int(input("Please type in a number: "))
a = 1
b = 1
while max >= a:
    while max >= b:
        c = a*b
        print(f"{a} x {b} = {c}")
        b += 1
    b = 1
    a += 1   
