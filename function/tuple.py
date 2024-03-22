#ordered, UNCHANGEABLE and allow dupilicates
# Tuple Symbol - ()
x=("Bike",'Car',10,2,3.0,5j,True)
# print(len(x))
# print(type(x))

#UPDATE DATA IN TUPLE
y=list(x)
y[1]=['Orange']
x=tuple(y)
print(x)

