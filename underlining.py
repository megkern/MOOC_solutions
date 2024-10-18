# Programming exercise: Underlining
# https://programming-24.mooc.fi/part-3/2-working-with-strings
#
# Please write a program which asks the user for strings using a loop. 
# The program prints out each string underlined as shown in the examples below. 
# The execution ends when the user inputs an empty string - that is, just presses Enter at the prompt

while True:
    text = input("Please type in a string: ")
    num = len(text)
    underline = ""
    c = 1

    while c <= num:
        underline += "-" 
        c += 1

    print(f"{text}\n{underline}")
       
    if text == "":
        break
