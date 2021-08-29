from PIL import Image, ImageColor, ImageDraw, ImageFont
from pathlib import Path
import os

os.system('cls')
os.chdir(f'{Path.home()}\\small-projects-python\\image_projs\\drawings')

im = Image.new('RGBA', (200, 200), 'white')
draw = ImageDraw.Draw(im)

draw.text((20, 150), 'Hello', fill='purple')
fonts_folder = 'C:\\Windows\\Fonts'

arial_font = ImageFont.truetype(f'{fonts_folder}\\arial.ttf', 32)
draw.text((100, 150), 'Howdy', fill='gray', font=arial_font)
im.save('text.png') 