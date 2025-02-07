#  If string is holding int then it can be converted into int.
a = 30
print(a, type(a))
b = int(a)
print(b, type(b))

# String to Int conversion is not allowed.
x = "kod"
print(x, type(x))
y = int(x)
print(y, type(y))

# string to float
p = float(input("enter float type data:")) #12.22
print(p, type(p))

bool()
q = ""
print(q, type(q))
q = bool(q)
print(q, type(q))

"""
1. While converting int to bool for all Non Zero values we will get 'True'.
2. While converting int to bool for 0 and empty strings we will get 'false'.
"""

print(bool("Kodnest"))