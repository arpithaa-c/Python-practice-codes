rows = 4
col = 5

for i in range(rows):
    for j in range(col):
        print("*",end="")
    print()

print()

#Increasing Triangle
for i  in range(rows):
    for j in range(i+1):
        print("*",end="")
    print()

print()

#Decreasing Triangle
for i  in range(rows):
    for j in range(i,rows):
        print("*",end="")
    print()
print()

#Right half Pyramid
for i  in range(rows):
    for j in range(i+1):
        print("*",end="")
    print()
for i  in range(rows):
    for j in range(i,rows-1):
        print("*",end="")
    print()
print()

#Butterfly pattern
for i in range(rows):
    for j in range(i+1):
        print("*",end="")
    for j in range(i,rows-1):
        print(" ",end="")
    for j in range(i,rows-1):
        print(" ",end="")
    for j in range(i+1):
        print("*",end="")
    print()
for i in range(rows):
    for j in range(i,rows-1):
        print("*",end="")
    for j in range(i+1):
        print(" ",end="")
    for j in range(i+1):
        print(" ",end="")
    for j in range(i,rows-1):
        print("*",end="")
    print()
print()

#Diamond
for i in range(rows):
    for j in range(i,rows):
        print(" ",end="")
    for j in range(i+1):
        print("*",end="")
    for j in range(i):
        print("*",end="")
    print()
for i in range(rows):
    for j in range(i+1):
        print(" ",end="")
    for j in range(i,rows-1):
        print("*",end="")
    for j in range(i,rows):
        print("*",end="")
    print()
print()

