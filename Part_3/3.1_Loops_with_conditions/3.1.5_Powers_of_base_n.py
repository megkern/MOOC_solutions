# Programming exercise: Powers of base n
# https://programming-24.mooc.fi/part-3/1-loops-with-conditions
#
# Please change the program from the previous exercise so that 
# the user gets to input also the base which is multiplied 
# (in the previous program the base was always 2).
#
# Sample output:
# Upper limit: 27
# Base: 3
# 1
# 3
# 9
# 27

ul = int(input("Upper limit: "))
base = int(input("Base: "))
num = 1

while ul > 0 and num <= ul:
    print(num)
    num = num*base
