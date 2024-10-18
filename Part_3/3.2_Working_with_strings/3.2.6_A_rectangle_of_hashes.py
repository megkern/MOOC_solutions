# Programming exercise: A rectangle of Hashes
# https://programming-24.mooc.fi/part-3/2-working-with-strings
#
# Please modify the previous program so that it also asks for the height, 
# and prints out a rectangle of hash characters accordingly. 
#
# Width: 10
# Height: 3
# #########
# #########
# #########

hash = ""
hash2 = ""
w = int(input("Width: "))
h = int(input("Height: "))
c = 1
while len(hash) < w:
    hash += "#"
while c <= h:
    hash2 += "\n" + hash
    c += 1

print(hash2)
