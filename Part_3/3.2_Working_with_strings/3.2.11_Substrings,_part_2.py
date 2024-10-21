# Programming exercise: Substrings, part 2
#
# Please write a program which asks the user to type in a string. 
# The program then prints out all the substrings which end with the last character, 
# from the shortest to the longest. Have a look at the example below.
#
# Please type in a string: test
# t
# st
# est
# test

text = input("Please type in a strong: ")
ntext = ""
otext = ""
num = len(text)-1
c = 0
while c <= num:
    ntext = text[num-c]
    c += 1
    otext = ntext + otext
    print(otext)
