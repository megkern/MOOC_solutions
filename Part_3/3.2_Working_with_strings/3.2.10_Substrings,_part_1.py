# Programming exercise: Substrings, part 1
# https://programming-24.mooc.fi/part-3/2-working-with-strings
#
# Please write a program which asks the user to type in a string. 
# The program then prints out all the substrings which begin with the first character, 
# from the shortest to the longest. Have a look at the example below.
# Sample output:
# Please type in a string: test
# t
# te
# tes
# test

text = input("Please type in a strong: ")
itext = ""
num = len(text)
c = 0
while num > c:
    itext += text[c]
    print(itext)
    c += 1
