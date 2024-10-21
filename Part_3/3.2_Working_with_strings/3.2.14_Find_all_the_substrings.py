# Programming exercise: Find all the substrings
# https://programming-24.mooc.fi/part-3/2-working-with-strings
#
# Please make an extended version of the previous program, which prints out 
# all the substrings which are at least three characters long, and which begin 
# with the character specified by the user. You may assume the input string is 
# at least three characters long.
# Sample output:
# Please type in a word: mammoth
# Please type in a character: m
# mam
# mmo
# mot

text = input("Please type in a word: ")
subtext = input("Please type in a character:")

while True:
    if len(text) == 0: 
        break
    index = text.find(subtext)
    if index != -1 and index+3 <= len(text):
        print(text[index:index+3])
        text = text[index+1:]
    else:
        break
