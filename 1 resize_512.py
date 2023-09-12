import os
from PIL import Image

# Nothing special, just resize all to 512x512.
# Good if you manually 1:1'ed your images and don't want to play with aspect bucketing.

try:
    os.mkdir("output")
except(FileExistsError):
    pass

for file in os.listdir("./"):
    filename, file_extension = os.path.splitext(file)
    if file_extension == ".png":
        image = Image.open(file)
        image2 = image.resize([512,512], Image.Resampling.LANCZOS)
        image2.save("./output/" + file)