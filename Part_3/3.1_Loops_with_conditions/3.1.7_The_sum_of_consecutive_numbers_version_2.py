# Programming exercise: The sum of consecutive numbers, version 2
# https://programming-24.mooc.fi/part-3/1-loops-with-conditions
#
# Please write a new version of the program in the previous exercise. 
# In addition to the result it should also print out the calculation performed:
# Limit: 2
# The consecutive sum: 1 + 2 = 3

up = int(input("Limit: "))
x1 = 1
sum = 1
text = f"The consecutive sum: {x1} "
while sum < up:
    x1 += 1 # put this line before the sum line if you initialize sum at 1
    text += f"+ {x1} "
    sum += x1 # or sum = sum + x1
    
    

text += f"= {sum}"
print(text)
