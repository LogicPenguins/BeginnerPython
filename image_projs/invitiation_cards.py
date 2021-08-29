#! python3
# invitation_cards.py - Creates custom invitation cards using Pillow Module features.

from PIL import Image, ImageDraw, ImageFont
from pathlib import Path
import pyinputplus as pyip
import random

def create_cards():
    try:
        general_path = f'{Path.home()}\\small-projects-python\\image_projs'
        # Adjust path as needed.
        filename = pyip.inputStr('File Name: ', timeout=60)
        filepath = f'{general_path}\\invitations\\{filename}.txt'
        file = open(filepath)
        names_list = file.readlines()

        # List for random card background color.
        color_list = ['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'pink', 'white']

        # Initialize flower png for each card
        FLOWER_NAME = 'flower.png'
        FLOWER_PATH = f'{general_path}\\invitations\\{FLOWER_NAME}'
        flower_image = Image.open(FLOWER_PATH)

        # Loop through each name, create a card and add items.
        for person in names_list:
            color = random.choice(color_list)
            if person.endswith('\n'):
                name = person[:-1]
            else:
                name = person
            print(f'Making a card for {name}...')
            card = Image.new('RGBA', (200, 200), color=color)
            card_width, card_height = card.size

            # Resize flower to fit card size.
            resized_flower = flower_image.resize((int(200 / 3), int(200 / 3)))
            resized_width, resized_height = resized_flower.size

            # Paste flower at bottom corner of card
            card.paste(resized_flower, (200 - resized_width, 200 - resized_height), resized_flower)

            # Setup drawing protocals
            draw = ImageDraw.Draw(card)
            fonts_folder = 'C:\\Windows\\Fonts'
            arial_font = ImageFont.truetype(f'{fonts_folder}\\arial.ttf', 12)

            # Write person's name
            draw.text((100 - len(name), 100), name, fill='Black', font=arial_font)

            # Draw some nice shapes
            draw.line([(0, 0), (200, 0), (200, 200), (0, 200), (0, 0)], fill='black', width=10)


            card.save(f'{general_path}\\invitations\\finished_cards\\{name}_invitation.png')


    except TimeoutError:
        print('You took too long to respond.')


if __name__ == '__main__':
    create_cards()
    print('Finished making cards.')