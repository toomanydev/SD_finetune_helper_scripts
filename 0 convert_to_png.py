import os
from PIL import Image, ImageOps

# JPG to PNG

try:
    os.mkdir("output")
except(FileExistsError):
    pass

for file in os.listdir("./"):
    filename, file_extension = os.path.splitext(file)
    if file_extension == ".jpeg" or file_extension == ".jpg":
        image = Image.open(file)
        image.save("./output/" + filename + ".png")