import math
from PIL import Image, ImageDraw

sourcecode = "++++++++[>++++[>++>+++>+++>+<<<<-]>+>+>->>+[<]<-]>>.>---.+++++++..+++.>>.<-.<.+++.------.--------.>>+.>++."

length = len(sourcecode)
square = math.ceil(math.sqrt(length))

size = 50
hsize = size/2

height = square * size
width = square * size

img = Image.new('RGBA', (width,height), 'black')

draw = ImageDraw.Draw(img)

draw.rectangle([0,0,50,50], "#DC322F")

img.save('aa.png')

