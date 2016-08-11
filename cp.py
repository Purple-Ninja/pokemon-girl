# encoding: utf8

from PIL import Image, ImageFont, ImageDraw
import os

text = u'My future girlfriend CP: 945'
text_color = (255,255,255)
fonts_path = 'fonts/MyanmarSangamMN.ttf'

shadowcolor = (128, 128, 128)

img = Image.open("girl.png")

# img = img.convert("RGBA")

draw = ImageDraw.Draw(img)

img_w, img_h = img.size

print img.size

## poke ball

pokeball = Image.open('pokeball.png')

pokeball = pokeball.convert('RGBA')

pokeball_w, pokeball_h = pokeball.size

pokeball_offset = (img_w - pokeball_w)/2, img_h-pokeball_h-25

# text

text_w, text_h = draw.textsize(text) # (42, 11)

print (text_w, text_h)

x, y = (img_w - text_w*2 + len(text))/2.0, round((img_h / 9.0)/2)

print (x,y)

font = ImageFont.truetype(font=fonts_path, size=26, index=0, encoding='')

# outline

draw.text((x-1, y), text, font=font, fill=shadowcolor)
draw.text((x+1, y), text, font=font, fill=shadowcolor)
draw.text((x, y-1), text, font=font, fill=shadowcolor)
draw.text((x, y+1), text, font=font, fill=shadowcolor)

draw.text((x, y), text, text_color, font=font)


# paste 

img.paste(pokeball, pokeball_offset, mask=pokeball) # the transparancy layer will be used as the mask

img.save('girl-cp.png')

img.close()