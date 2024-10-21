# Programming exercise: Find the first substring
# https://programming-24.mooc.fi/part-3/2-working-with-strings
#
# Please write a program which asks the user to type in a string and a single character. 
# The program then prints the first three character slice which begins with the character specified by the user. 
# You may assume the input string is at least three characters long. The program must print out three characters, 
# or else nothing. Pay special attention to when there are less than two characters left in the string after the 
# first occurrence of the character looked for. In that case nothing should be printed out, and there should not 
# be any indexing errors when executing the program.
# Sample output:
# Please type in a word: mammoth
# Please type in a character: m
# mam

text = input("Please type in a word: ")
subtext = input("Please type in a character:")

if subtext in text:
    index = text.find(subtext)
    if (index + 3) <= (len(text)-1):
        print(text[index:index+3])
    else:
        print("")
else:
    print("")
