import os
import shutil
from PIL import Image
from PIL import ImageOps

# Produces a flipped image of each image in the directory it's run in

try:
    os.mkdir("output")
except FileExistsError:
    pass

for file in os.listdir("./"):
    filename, file_extension = os.path.splitext(file)
    if file_extension == ".png":
        image = Image.open(file)
        image = ImageOps.mirror(image)
        image.save("./output/" + filename + "_flipped.png")
        try:
            shutil.copyfile("./" + filename + ".txt",
                            "./output/" + filename + "_flipped.txt")
        finally:
            pass
