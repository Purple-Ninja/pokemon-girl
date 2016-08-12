# encoding: utf8

from PIL import Image, ImageFont, ImageDraw

text = u'hot chick CP: 520'
text_color = (255,255,255)
fonts_path = 'fonts/MyanmarSangamMN.ttf'
# shadowcolor = (255, 255, 255)
shadowcolor = None
font_size = 24

input_image = 'girl.png'
output_image = '.'.join(input_image.split('.')[:-1]) + '-cp.png'

def load_image(input_image):
    return Image.open(input_image).convert('RGBA')

def draw(img):
    return ImageDraw.Draw(img)

def resize_image(img):
    img_w, img_h = img.size
    img_ratio = img_w/float(img_h)
    return img.resize( ( int(675.0*img_ratio) ,675) )

def load_pokeball():
    return Image.open('pokeball.png').convert('RGBA')

def get_pokeball_offset(image_size, pokeball_size):
    img_w, img_h = image_size
    pokeball_w, pokeball_h = pokeball_size
    # pokeball = pokeball.resize( (184, 184), Image.ANTIALIAS)
    return (img_w - pokeball_w)/2, int(img_h - pokeball_h - img_h/625.0*25)

def get_font(fonts_path, font_size):
    return ImageFont.truetype(font=fonts_path, size=font_size, index=0, encoding='')

def get_text_size(draw, text, font):
    return draw.textsize(text, font) # (42, 11)

def get_text_position(img, text, text_size):
    text_w, text_h = text_size
    img_w, img_h = img.size
    return (img_w - text_w - len(text))/2.0, round((img_h / 9.0)/2)

def draw_text(draw, text_position, text, text_color, font):
    draw.text(text_position, text, text_color, font=font)

def draw_text_outline(text, text_position, font, shadowcolor):
    if shadowcolor:
        x, y = text_position
        draw.text((x-1, y), text, font=font, fill=shadowcolor)
        draw.text((x+1, y), text, font=font, fill=shadowcolor)
        draw.text((x, y-1), text, font=font, fill=shadowcolor)
        draw.text((x, y+1), text, font=font, fill=shadowcolor)

def paste_pokeball(img, pokeball, pokeball_offset):
    img.paste(pokeball, pokeball_offset, mask=pokeball)

def save_image(img, output_image):
    img.save(output_image)
    img.close()

if __name__ == '__main__':

    print '> load image'
    img = load_image(input_image)

    img = resize_image(img)

    draw = draw(img)

    pokeball = load_pokeball()

    pokeball_offset = get_pokeball_offset(img.size, pokeball.size)

    print '> drawing text'
    font = get_font(fonts_path, font_size)

    text_size = get_text_size(draw, text, font)

    text_position = get_text_position(img, text, text_size)

    draw_text(draw, text_position, text, text_color, font)

    draw_text_outline(text, text_position, font, shadowcolor)

    print '> paste pokeball'
    paste_pokeball(img, pokeball, pokeball_offset)

    save_image(img, output_image)

    print '> done'
