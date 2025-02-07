"""
Conditional : if-else, if-elif
Looping : for, while
Jumping : break, continue, pass
"""
# def checkAge(age):
#     if(age>=18):
#         print("Age is greater than 18")
#     else:
#         print("Age is not greater than 18")
# checkAge(16)

# WAP to display "Child" if the age is in between below 18, 
# display adult if age is above 18S
# and display senior citizen if age is above 65.
def displayAgeCategory(age):
    if (age< 18):
        print("Child")
    elif (age>18 and age<65):
        print("Adult")
    else:
        print("Senior citizen")
displayAgeCategory(int(input("Enter yor age:")))