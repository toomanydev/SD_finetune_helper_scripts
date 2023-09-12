import os
from PIL import Image, ImageOps

# PNG to WEB, for better storage than JPEG.

try:
    os.mkdir("output")
except(FileExistsError):
    pass

for file in os.listdir("./"):
    filename, file_extension = os.path.splitext(file)
    if file_extension == ".png":
        image = Image.open(file)
        image.save("./output/" + filename + ".webp", "WEBP", quality=95)