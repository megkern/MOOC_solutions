# Programming exercise: Extra space
# https://programming-24.mooc.fi/part-1/3-more-about-variables
#
# Your friend is working on an app for jobseekers. She sends you this bit of code:
# name = "Tim Tester"
# age = 20
# skill1 = "python"
# level1 = "beginner"
# skill2 = "java"
# level2 = "veteran"
# skill3 = "programming"
# level3 = "semiprofessional"
# lower = 2000
# upper = 3000
# 
# print("my name is ", name, " , I am ", age, "years old")
# print("my skills are")
# print("- ", skill1, " (", level1, ")")
# print("- ", skill2, " (", level2, ")")
# print("- ", skill3, " (", level3, " )")
# print("I am looking for a job with a salary of", lower, "-", upper, "euros per month")
#
# Please fix the code so that the printout looks right. Notice especially how the comma 
# notation in the print command automatically inserts a space around the different comma-separated parts.

name = "Tim Tester"
age = 20
skill1 = "python"
level1 = "beginner"
skill2 = "java"
level2 = "veteran"
skill3 = "programming"
level3 = "semiprofessional"
lower = 2000
upper = 3000

print(f"my name is {name}, I am {age} years old \n\nmy skills are \n - {skill1} ({level1}) \n - {skill2} ({level2}) \n - {skill3} ({level3}) \n\nI am looking for a job with a salary of {lower}-{upper} euros per month")
