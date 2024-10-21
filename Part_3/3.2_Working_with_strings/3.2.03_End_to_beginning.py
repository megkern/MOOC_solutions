# Programming exercise: End to beginning
# https://programming-24.mooc.fi/part-3/2-working-with-strings
#
# Please write a program which asks the user for a string. 
# The program then prints out the input string in reversed order, from end to beginning. 
# Each character should be on a separate line.
#
# An example of expected behaviour:
# Please type in a string: hiya
# a
# y
# i
# h

input_string = input("Please type in a string: ")
index = 1
while index <= len(input_string):
    print(input_string[-1*index])
    index += 1
