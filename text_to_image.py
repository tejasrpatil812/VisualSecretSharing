from PIL import Image, ImageDraw, ImageFont

width, height = 128, 128

def handle(message: str):
    
    img = Image.new('L', (width, height), color='white')
    imgDraw = ImageDraw.Draw(img)
    textWidth, textHeight = imgDraw.textsize(message)
    xText = (width - textWidth) / 2
    yText = (height - textHeight) / 2

    imgDraw.text((xText, yText), message)

    img.save('secret.png')

if __name__ == '__main__':    
    handle("      Hello! \n|| CSE539 - ASU ||")
