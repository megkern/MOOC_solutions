# Programming exercise: Second and second to last characters
#
# Please write a program which asks the user for a string. 
# The program then prints out a message based on whether the 
# second character and the second to last character are the same or not. 
# See the examples below.
#
# Sample output
# Please type in a string: python
# The second and the second to last characters are different

string = input("Please type in a string: ")
c1 = string[1]
c2 = string[len(string)-2]
if c1 != c2:
    print("The second and the second to last characters are different")
if c1 == c2:
    print(f"The second and the second to last characters are {c1}")
