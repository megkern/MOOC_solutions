# Programmiing Exercise: A line of hases
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
