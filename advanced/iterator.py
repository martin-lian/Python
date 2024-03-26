#ITERATOR SIMPLIFIES THE FOR-LOOP
'''
xname=("cycle","bike","car")
myite=iter(xname)

print(next(myite))
print(next(myite))
print(next(myite))

'''

#CREATE ITERATOR

class exname:
    def __iter__(self):
        self.a=2
        return self

    def __next__(self):
        x= self.a
        self.a += 2
        return x
myclass=exname()
myite=iter(myclass)

print(next(myite))
print(next(myite))
print(next(myite))