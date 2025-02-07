"""
1.In list we can store Homogenous as well as Heterogenous data.
2.In list we can store Duplicate values.
3.List is an ordered collection of data: order of insertion will remain
 as it is in the output.
4.Lists are Mutable : Once we declare the list we can modify it. 
"""

li1 = [10,20,44.45,True,"Kodnest",20]
print(li1, type(li1))

#append(): Will add element at the end of the list
li1.append(300)
print(li1)      #[10, 20, 44.45, True, 'Kodnest', 20, 300]

#insert(index,element): Inserts an element at specified index
li1.insert(1,15)
print(li1)     #[10, 15, 20, 44.45, True, 'Kodnest', 20, 300]

#remove(el): Removes the first occurance of the specified element.
li1.remove(20)
print(li1)    #[10, 15, 44.45, True, 'Kodnest', 20, 300]

#in and not in operator:
print(2000 in li1)      #False
print("Kodnest" in li1) #True

#pop():without argument it will delete and return the last element in the list
removed_ele=li1.pop()
print(removed_ele)  #300
print(li1)    #[10, 15, 44.45, True, 'Kodnest', 20]

#pop(index):with argument it will delete the element at specified index
removed_ele = li1.pop(4)
print(removed_ele) #Kodnest
print(li1)   #[10, 15, 44.45, True, 20]

#del keyword:
del li1[1]
print(li1) #[10, 44.45, True, 20]

del li1
print(li1) #name 'li1' is not defined