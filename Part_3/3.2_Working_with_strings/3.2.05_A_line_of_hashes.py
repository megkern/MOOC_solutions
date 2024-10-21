# Programming exercise: A line of hases
# https://programming-24.mooc.fi/part-3/2-working-with-strings
#
# Please write a program which prints out a line of hash characters, 
# the width of which is chosen by the user.
#
# Sample output
# Width: 3
# ##

hash = ""
w = int(input("Width: "))
while len(hash) < w:
    hash += "#"

print(hash)
