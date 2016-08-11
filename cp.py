# encoding: utf8

from PIL import Image, ImageFont, ImageDraw
import os

text = u'future girlfriend CP: 290'
text_color = (255,255,255)
fonts_path = 'fonts/MyanmarSangamMN.ttf'

# file io

input_image = 'girl.png'
output_image = '.'.join(input_image.split('.')[:-1]) + '-cp.png'

# text shadow
shadowcolor = (212, 212, 212)

font_size = 26

# prepare font

font = ImageFont.truetype(font=fonts_path, size=font_size, index=0, encoding='')


# input image

img = Image.open(input_image).convert('RGBA')

# image resize to h:675

img_w, img_h = img.size

img_ratio = img_w/float(img_h)

img = img.resize( ( int(675.0*img_ratio) ,675) )

img_w, img_h = img.size

# draw

draw = ImageDraw.Draw(img)

## poke ball

pokeball = Image.open('pokeball.png')

pokeball = pokeball.convert('RGBA')

pokeball_w, pokeball_h = pokeball.size

# pokeball = pokeball.resize( (184, 184), Image.ANTIALIAS)

pokeball_offset = (img_w - pokeball_w)/2, int(img_h - pokeball_h - img_h/625.0*25)

text_w, text_h = draw.textsize(text, font) # (42, 11)

# text

x, y = (img_w - text_w - len(text))/2.0, round((img_h / 9.0)/2)

# outline

draw.text((x-1, y), text, font=font, fill=shadowcolor)
draw.text((x+1, y), text, font=font, fill=shadowcolor)
draw.text((x, y-1), text, font=font, fill=shadowcolor)
draw.text((x, y+1), text, font=font, fill=shadowcolor)

draw.text((x, y), text, text_color, font=font)

# paste 

img.paste(pokeball, pokeball_offset, mask=pokeball) # the transparancy layer will be used as the mask

# save and close

img.save(output_image)

img.close()