# Programming exercise: The second occurrence
# https://programming-24.mooc.fi/part-3/2-working-with-strings
#
# Please write a program which finds the second occurrence of a substring. 
# If there is no second (or first) occurrence, the program should print out a message accordingly. 
# In this exercise the occurrences cannot overlap. For example, in the string aaaa the second 
# occurrence of the substring aa is at index 2.
#
# Some examples of expected behaviour:
# Please type in a string: methodology
# Please type in a substring: o
# The second occurrence of the substring is at index 6.

text = input("Please type in a string: ")
subtext = input("Please type in a substring: ")

index1 = text.find(subtext)
stext = text[index1+len(subtext):]
index2 = stext.find(subtext)
sindex = index2 + index1 + len(subtext) 

if index2 != -1 and index1 != -1: 
    print(f"The second occurrence of the substring is at index {sindex}.")
else:
    print("The substring does not occur twice in the string.")
