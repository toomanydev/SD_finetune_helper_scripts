import os
from PIL import Image

# Changes images to jpg and with quality 95 to reduce file size.

try:
    os.mkdir("output")
except FileExistsError:
    pass

resize_ratio = 0.5
quality = 95

for file in os.listdir("./"):
    filename, file_extension = os.path.splitext(file)
    if file_extension == ".png":
        image = Image.open(file)
        image2 = image.resize(
            [int(image.size[0]*resize_ratio), int(image.size[1]*resize_ratio)],
            Image.Resampling.LANCZOS)
        image2.save("./output/" + filename + ".jpg", quality=quality)
