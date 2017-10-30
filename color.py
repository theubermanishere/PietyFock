# Code to calculate the hue and color differences 

a = ["#DC322F","#6C71C4","#2AA198","#859900"]
b = ["#A32523","#515594","#1C6B65","#AFC900"]

white = "#FFFFFF"
black = "#000000"

arr = []

def change(c1,c2):
    if (c1 in a and c2 in a):
        hue = 0
    elif (c1 in b and c2 in b):
        hue = 0
    else: 
        hue = 1
    if (hue == 0):
        i = a.index(c1)
        j = a.index(c2) + 4
        color = (j - i)%4
    else:
        if (c1 in a):
            i = a.index(c1)
            j = b.index(c2) + 4
            color = (j - i)%4
        else:
            i = b.index(c2)
            j = a.index(c1) + 4
            color = (j - i)%4
    return [color,hue]

