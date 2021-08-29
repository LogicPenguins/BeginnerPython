import os
from PIL import Image
from pathlib import Path

general_path = f"{Path.home()}\\small-projects-python\\image_projs"

LOGO_FILENAME = "catlogo.png"
LOGO_FILEPATH = f"{general_path}\\images\\{LOGO_FILENAME}"
logo_im = Image.open(LOGO_FILEPATH)

os.makedirs(f"{general_path}\\withLogo", exist_ok=True)

# Loop over all files in the working directory.
for filename in os.listdir(f"{general_path}\\images"):
    if (
        not (filename.endswith(".png") or filename.endswith(".jpg") or filename.endswith(".gif"))
        or filename == LOGO_FILENAME
    ):
        continue 

    im = Image.open(f"{general_path}\\images\\{filename}")
    width, height = im.size

    # Resize the logo.
    print(f"Resizing logo to fit {filename}...")
    sLogo = logo_im.resize((int(width / 3), int(height / 4)))
    sLogo_width, sLogo_height = sLogo.size

    # Add the logo.
    print(f"Adding logo to {filename}...")
    im.paste(sLogo, (width - sLogo_width, height - sLogo_height), sLogo)

    # Save changes.
    im.save(f"{general_path}\\withLogo\\withLogo_{filename}")
