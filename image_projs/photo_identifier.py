#! python3
# photo_identifier.py - Searches through entire hard drive and searches for photos that mean criteria
# Criteria: Photos must end in .png or .jpg. Photos must also be minimum 500x500 pixels. 

from PIL import Image, UnidentifiedImageError
import os
import time

photo_files = []
num_photo_files = 0
num_non_photo_files = 0
start_time = time.time()

for foldername, subfolders, filenames in os.walk('C:\\'):
    for filename in filenames:
        try:

            # Make sure the file is a .png or .jpg file.
            if (filename.endswith('.png') or filename.endswith('.jpg')):
                # check to see if they're right dimensions
                im = Image.open(f'{foldername}\\{filename}')

                # Check if the file is atleast 500 pixels in width and height.
                width, height = im.size
                if (width >= 500 and height >= 500):
                    photo_files.append(filename)
                    num_photo_files += 1
                else:
                    pass
            else:
                num_non_photo_files += 1
                continue
        # Some image files can't be processed by Pillow so they will be skipped corresponding to these errors.
        except UnidentifiedImageError:
            pass
        except OSError:
            pass


end_time = time.time()

print(f'Number of photos: {num_photo_files}\nNumber of non-photos: {num_non_photo_files}\nProcess took {end_time - start_time} seconds.')