# Programming exercise: First letters of words
# https://programming-24.mooc.fi/part-3/3-more-loops
#
# Please write a program which asks the user to type in a sentence. 
# The program then prints out the first letter of each word in the sentence, each letter on a separate line.
# An example of expected behaviour:
# Please type in a sentence: Humpty Dumpty sat on a wall
# H
# D
# s
# o
# a
# w

text = input("Please type in a sentence: ")
print(text[0])
while text.find(" ") != -1:
   index = text.find(" ")
   punc = text.find(",") 
   if punc == index + 1:
      text = text[index + 2:]
      print(text[0]) 
   else:
      text = text[index + 1:]
      print(text[0])
