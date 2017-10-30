# Code to calculate the hue and color differences 

a = ["#DC322F","#6C71C4","#2AA198","#859900"]
b = ["#A32523","#515594","#1C6B65","#AFC900"]
c = ["+",">",".","["]
d = ["-","<",",","]"]

white = "#FFFFFF"
black = "#000000"

def color_change(c1,c2):
    if (c1 in a and c2 in a):
        hue = 0
    elif (c1 in b and c2 in b):
        hue = 0
    else: 
        hue = 1
    if (hue == 0):
        if (c1 in a):
            i = a.index(c1)
            j = a.index(c2) + 4
            color = (j - i)%4
        else:
            i = b.index(c1)
            j = b.index(c2) + 4
            color = (j - i)%4
    else:
        if (c1 in a):
            i = a.index(c1)
            j = b.index(c2) + 4
            color = (j - i)%4
        else:
            i = b.index(c1)
            j = a.index(c2) + 4
            color = (j - i)%4
    return [color,hue]


def symbol_change(c1,c2):
    if (c1 in c and c2 in c):
        hue = 0
    elif (c1 in d and c2 in d):
        hue = 0
    else: 
        hue = 1
    if (hue == 0):
        if (c1 in c):
            i = c.index(c1)
            j = c.index(c2) + 4
            color = (j - i)%4
        else:
            i = d.index(c1)
            j = d.index(c2) + 4
            color = (j - i)%4
    else:
        if (c1 in c):
            i = c.index(c1)
            j = d.index(c2) + 4
            color = (j - i)%4
        else:
            i = d.index(c1)
            j = c.index(c2) + 4
            color = (j - i)%4
    return [color,hue]

def color_to_symbol(foo):
    color = "#DC322F"
    symbol = "+"
    zz = []
    yy = []
    for i in foo:
        zz.append(color_change(color,i))
        color = i
    for i in zz:
        for j in (c+d):
            if symbol_change(symbol,j) == i:
                yy.append(j)
                symbol = j
                break
    return yy

def symbol_to_color(foo):
    symbol = "+"
    color = "#DC322F"
    zz = []
    yy = []
    for i in foo:
        zz.append(symbol_change(symbol,i))
        symbol = i
    for i in zz:
        for j in (a+b):
            if color_change(color,j) == i:
                yy.append(j)
                color = j
                break
    return yy

