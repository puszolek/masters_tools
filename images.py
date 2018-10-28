from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 


def writeImage(x, y, name):

    img = Image.new('L', (4096,4096), 'black') # Create a new black image
    draw = ImageDraw.Draw(img)
    #draw.line((0,0, 0,4095), fill=256)
    #draw.line((0,0, 4095,0), fill=256)
    #draw.line((0,4095, 4095,4095), fill=256)
    #draw.line((4095,0, 4095,4095), fill=256)
    font = ImageFont.truetype("calibri.ttf", 800)
    draw.text((x, y), "ABCD", (255), font=font)
    #img.show()
    img.save(name)


def createImages():
    n = 1
    #for i in range(0, 500, 50):
    for i in range(-1800, 4500, 100):
        name = "img" + str(n) + ".bmp"
        writeImage(i, 1750, name)
        n = n+1
        print(name)
        print(i)

createImages();