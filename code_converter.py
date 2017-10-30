import math
from PIL import Image, ImageDraw
import path
import color
import sys

def cleanup(code):
  return ''.join(filter(lambda x: x in ['.', ',', '[', ']', '<', '>', '+', '-'], code))

f = open(sys.argv[1],'r')
sourcecode = f.read()
source = list(cleanup(sourcecode))


zz = []
for i in source:
    zz.append(color.e[i])
print(zz)

yy = color.symbol_to_color(zz)

length = len(sourcecode)
square = int(math.ceil(math.sqrt(length)))

loci = path.path(int(square))

size = 50
hsize = size/2

height = int(square * size)
width = int(square * size)

img = Image.new('RGBA', (width,height), 'black')

draw = ImageDraw.Draw(img)

print(len(yy))
print(len(loci))

for i in range(len(yy)):
    draw.rectangle([loci[i][1]*50,loci[i][0]*50,(loci[i][1]+1)*50,(loci[i][0]+1)*50], yy[i])

img.save('aa.png')

