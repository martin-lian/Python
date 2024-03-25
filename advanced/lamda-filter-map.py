#LAMBDA

# x=lambda a,b: a*b
# print(x(5,5))

"""
def f(n):
    return lambda a: a*n
xname1=f(2)
xname2=f(3)
xname3=f(4)

print(xname1(11))
print(xname2(11))
print(xname3(11))
"""
#FILTER

"""
def primenum(x):
    for n in range(2,x):
        if x%n == 0:
            return False
        else:
            return True
        
xname=filter(primenum,range(30))
print("Prime Numbers are: ", list(xname))
"""

#MAP

def findsquare(x):
    return x*x

numbers=[1,2,3,4,5,6]

xname=map(findsquare,numbers)
print(list(xname))
    
