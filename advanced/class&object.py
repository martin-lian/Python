#class and objects

class human:
    def __init__(self,name,age):
        self.name   = name
        self.age    = age
    
    def xname(self):
        print("Hi, My Name is "+ self.name)
        
h1=human("Martin",29)
h2=human("Angelin",31)

h1.xname()
h2.xname()
