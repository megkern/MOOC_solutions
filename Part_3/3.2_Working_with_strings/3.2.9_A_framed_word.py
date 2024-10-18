# Programming exercise: A framed word
# https://programming-24.mooc.fi/part-3/2-working-with-strings
#
# Please write a program which asks the user for a string and 
# then prints out a frame of * characters with the word in the centre. 
# The width of the frame should be 30 characters. 
# You may assume the input string will always fit inside the frame.
#
# If the length of the input string is an odd number, you may print out the word 
# in either of the two possible centre locations.
#
# Sample output:
# Word: testing
# 
# ******************************
# *          testing           *
# ******************************

str0 = input("Word: ")
letters = len(str0)
spaces = 30-letters-2
c = 0
k = 0
str1 = ""
str2 = ""
str3 = ""

if letters % 2 == 0: #even number of letters
    while c < spaces/2: 
        str1 += " "
        c += 1
    str2 = "*" + str1 + str0 + str1 + "*"

else:     #odd number of letters
    while c < spaces//2: 
        str1 += " "
        c += 1
    str2 = "*" + str1 + " " + str0 + str1 + "*"



while k < 30:
    str3 += "*"
    k += 1



print(str3)
print(str2)
print(str3) 
