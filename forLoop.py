# '''for control_variable in iterable_object'''

for i in "kodnest":
    print(i)

for j in [10,20,30]:
    print(j+5)

for num in range(1, 11):
    print(num)

for num in range(11, 21, 2):
    print(num, end=" ")

for i in range(5):
    print(i, end=" ")



# #WAP to print all the even numbers from 1 to 10
for i in range(2, 11, 2):
    print(i)

# '''While loop'''

i = 0
while(i<10):
    print(i+100)
    i += 1

#Jumping control constructs
#WAP to print numbers from 1 to 10, if numner is 6 then skip printing
for i in range(1,11):
    if (i == 6):
        continue
    print(i)

#WAP to print numbers from 1 to 10, if numner is 5 then stop printing
for i in range(1,11):
    if (i == 5):
        break
    print(i)

def disp():
    pass

class demo:
    pass
