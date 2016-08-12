from flask import Flask, send_file
app = Flask(__name__)

import cp

@app.route("/")
def hello():

    text = u'hot chick CP: 520'
    text_color = (255,255,255)
    fonts_path = 'fonts/MyanmarSangamMN.ttf'
    # shadowcolor = (255, 255, 255)
    shadowcolor = None
    font_size = 24

    input_image = 'girl.png'
    output_image = '.'.join(input_image.split('.')[:-1]) + '-cp.png'

    img_io = cp.makeup(input_image, text, text_color, fonts_path, shadowcolor, font_size, save=False)

    return send_file(img_io, mimetype='image/jpeg')

if __name__ == "__main__":
    app.run()