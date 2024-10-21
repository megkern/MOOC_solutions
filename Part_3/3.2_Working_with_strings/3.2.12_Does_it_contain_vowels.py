# Programming exercise: Does it contain vowels
# https://programming-24.mooc.fi/part-3/2-working-with-strings
#
# Please write a program which asks the user to input a string. 
# The program then prints out different messages if the string contains any of the vowels a, e or o.
# You may assume the input will be in lowercase entirely. Have a look at the examples below.
#
# Please type in a string: hello there
# a not found
# e found
# o found

text = input("Please type in a string: ")
subtext = "aeo"
c = 0
while c < len(subtext):
    vowel = subtext[c]
    if vowel in text:
        print(f"{vowel} found")
    else:
        print(f"{vowel} not found")
    c +=1
