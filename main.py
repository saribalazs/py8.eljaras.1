'''
1. Feladat
Írj eljárást, amely egy tetszőleges szöveget, ill. alakzatot ír ki a képernyőre!
'''
import turtle

def eljaras():
    p = turtle.Turtle()
    for _ in range(4):
        p.fd(100)
        p.rt(90)
    return p

def masik():
    return"Marika volt a piacon" 

print(eljaras())
print(masik()) 