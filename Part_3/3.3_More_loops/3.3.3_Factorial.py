# Programming exercise: Factorial
# https://programming-24.mooc.fi/part-3/3-more-loops
#
# Please write a program which asks the user to type in an integer number. 
# If the user types in a number equal to or below 0, the execution ends. 
# Otherwise the program prints out the factorial of the number.
#
# Some examples of expected behaviour:
# Please type in a number: 3
# The factorial of the number 3 is 6
# Please type in a number: 4
# The factorial of the number 4 is 24
# Please type in a number: -1
# Thanks and bye!

while True:
    fac = 1
    c = 0
    num = int(input("Please type in a number: "))
    while c < num:
        fac = fac*(num-c)
        c += 1
    if num <= 0:
        break
    else:
        print(f"The factorial of the number {num} is {fac}")
    
print("Thanks and bye!")
