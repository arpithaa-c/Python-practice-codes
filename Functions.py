#Without input and without Return statement:
def add():
    a = 10
    b = 20
    print("Addition is:", a+b)


#With input and without Return statement:
def sub(a,b):
    print("Subtraction is:", a-b)


#Without input and with Return statement:
def mul():
    return 10*20


#With input and with Return statement:
def div(a,b):
    return a/b


add()
sub(100,50)
print(mul())
print(div(200,10))