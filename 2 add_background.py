import os
import shutil
from PIL import Image

# Adds a white background to transparent images

try:
    os.mkdir("output")
except FileExistsError:
    pass

for file in os.listdir("./"):
    filename, file_extension = os.path.splitext(file)
    if file_extension == ".png":
        image = Image.open(file).convert("RGBA")
        new_image = Image.new("RGBA", image.size, "WHITE")
        new_image.paste(image, (0, 0), image)
        new_image.save("./output/" + filename + ".png")
