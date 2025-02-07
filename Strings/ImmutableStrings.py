'''
Strings are Immutable.
1. Once we declare the strings we cannot modify, 
If we try to modify then new string will be created.

2. If new string doesnot have any reference vriablethe it will be removed.

3. Python internally uses String Interning.

4. String Interning is the process of checking string interning pool
 before creating any new object.

5. Whenever we want to create new object python checks internal pool,
 whether that object already exists or not.

6. When the object already exists in the string intern records 
then address of existing object will be reused.
'''
# s1 = "Kodnest"
# s1 = s1.upper()
# print(s1)

# s1 = "K"
# print(s1, id(s1))

s1 = "Hello"
s2 = "World"
print(s1, id(s1))
print(s2, id(s2))

print("s1 Id of H:", id(s1[0])) #H
print("s2 Id of W:", id(s2[0]))

print("s1 Id of l:", id(s1[2]))
print("s1 Id of l:", id(s1[3]))
print("s2 Id of l:", id(s2[3]))

print("s1 Id of o:", id(s1[-1])) #o
print("s2 Id of o:", id(s2[1]))
