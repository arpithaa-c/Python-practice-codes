"""
1.In Tuple we can store Homogenous as well as Heterogenous data.
2.In Tuple we can store Duplicate values.
3.Tuples are ordered collection of data: order of insertion will remain
 as it is in the output.
4.Tuples are Immutable : Once we declare the tuple we cannot modify it. 
"""

tup1 = (10,22.55,"Kodnest",True,10)
print(tup1) #(10, 22.55, 'Kodnest', True, 10)

# tup1.append(300)
# tup1.remove(10)
# tup1.pop()
# del tup1[2]

#Accessing tuple
print(tup1[2]) #Kodnest

#Deletes the tuple
del tup1
# print(tup1) #Error

#Concatenation of tuples
t1 = (1,2,3)
t2 = (9,4,1)
t3 = t1 + t2
print(t3)  #(1, 2, 3, 9, 4, 1)