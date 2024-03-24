import random

def gen_random(upper):
    r=random.randint(1,upper)
    return r

def mainmatter():
    program= True
    num1=gen_random(10)
    num2=gen_random(10)
    result= num1+num2
    
    while program:
        ans=input("what is "+ str(num1) + "+" + str(num2) +" = ")
        
        if ans.isdigit():
            if int(ans)==result:
                print("Correct")
                program=False
            else:
                print("Incorrct")
        else:
            print("Answer must be positive")
            
x=10
for x in range(x):
    mainmatter()    