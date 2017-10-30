import math
from PIL import Image, ImageDraw
from sys import argv
import color
import path

size = 50

sourcecode = "++++++++[>++++[>++>+++>+++>+<<<<-]>+>+>->>+[<]<-]>>.>---.+++++++..+++.>>.<-.<.+++.------.--------.>>+.>++."
source = list(sourcecode)

zz = []
for i in source:
    zz.append(color.e[i])
print(zz)

yy = color.symbol_to_color(zz)

print(color.color_to_symbol(yy))

