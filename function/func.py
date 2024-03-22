# FUNCTION EXAMPLE PROGRAM
"""
def examplename(x,y):
    print(x,"",y)
examplename("Hello","World")
"""
# FUNCTIOIN INTO FUNCTION WITH LIST EXAMPLE



list=['car ','bike ','cycle ']

#function-statement-1
def func_1stname(x):
     print(x*3)

#function-statement-2
def func_2ndname(a,list):
    #loop-statement
    for items in list:
        a(items)
func_2ndname(func_1stname,list)  
        
    



    