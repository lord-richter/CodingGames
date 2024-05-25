import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

class Digit(object):
    count = -1
    def __init__(self, name='root', children=None):
        type(self).count+=1
        self.name = name
        self.prev = None
        self.children = []
        if children is not None:
            for child in children:
                self.add_child(child)

    def __str__(self):
        return self.name

    def add_child(self,name):
        for child in range(0,len(self.children)):
            if(self.children[child].name==name):
                print(self,"Found:", name, file=sys.stderr, flush=True)
                return self.children[child]
        newnode=Digit(name)
        self.children.append(newnode)        
        print(self,"Added:", newnode, file=sys.stderr, flush=True)
        return newnode



n = int(input())
phonelist = Digit()

for i in range(n):
    telephone = input()
    print("Number:", telephone, file=sys.stderr, flush=True)
    next = phonelist
    for d in str(telephone):
        print("Digits:", d, file=sys.stderr, flush=True)
        next= next.add_child(d)
        print("      :", next, file=sys.stderr, flush=True)
        print("      :", Digit.count, file=sys.stderr, flush=True)
        


# The number of elements (referencing a number) stored in the structure.
print(Digit.count)
