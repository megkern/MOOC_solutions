# Programming exercise: String multiplied
# https://programming-24.mooc.fi/part-3/2-working-with-strings
#
# Please write a program which asks the user for a string and an amount. 
# The program then prints out the string as many times as specified by the amount. 
# The printout should all be on one line, with no extra spaces or symbols added.
#
# An example of expected behaviour:
# Please type in a string: hiya
# Please type in an amount: 4
# hiyahiyahiyahiya

text0 = input("Please type in a string: ") 
text = ""
n = int(input("Please type in an amount: "))
tic = 1

while n > 0 and tic <= n :
    text += text0
    tic +=1

print(text)
