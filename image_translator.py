import math
from PIL import Image, ImageDraw
import path
import color
import sys
import brainfuck as brain

sourcecode = "++++++++[>++++[>++>+++>+++>+<<<<-]>+>+>->>+[<]<-]>>.>---.+++++++..+++.>>.<-.<.+++.------.--------.>>+.>++."
source = list(sourcecode)

img = Image.open(sys.argv[1])

size = 50
hsize = size/2
square = img.size[0]/size

loci = path.path(int(square))

colors = []

for i in loci:
    rgb = img.getpixel((i[1]*size+10,i[0]*size+10))
    if (rgb == (0,0,0,255)):
        break
    colors.append('#%02x%02x%02x' % (rgb[0], rgb[1], rgb[2]))

zz = list(map(str.upper,colors))

fin = []

for i in color.color_to_symbol(zz):
    fin.append(color.f[str(i)])

print(brain.evaluate(''.join(fin)))
