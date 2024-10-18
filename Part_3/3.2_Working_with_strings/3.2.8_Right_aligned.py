# Programming exercise: Right-aligned
#
# Please write a program which asks the user for a string and then prints it out 
# so that exactly 20 characters are displayed. If the input is shorter than 20 characters, 
# the beginning of the line is filled in with * characters.
#
# You may assume the input string is at most 20 characters long.
# 
# Sample output:
# Please type in a string: python
# **************python

str0 = input("Please type in a string:")
filled = len(str0)
unfilled = 20-filled
c = 0
str1 = ""
str2 = ""

while c < unfilled: 
    str1 += "*"
    c += 1

str2 = str1 + str0
print(str2) 
