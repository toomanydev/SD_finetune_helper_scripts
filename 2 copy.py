import os
import shutil
from PIL import Image
from PIL import ImageOps

# Copies files into an output directory, then adds "_copy" to the name.
# You can then batch process these with other scripts, such as one to make greyscale images.
# After, you can copy those images back into the main training directory.

try:
    os.mkdir("output")
except FileExistsError:
    pass

for file in os.listdir("./"):
    filename, file_extension = os.path.splitext(file)
    if file_extension == ".png":
        image = Image.open(file)
        image = ImageOps.mirror(image)
        image.save("./output/" + filename + "_copy.png")
        try:
            shutil.copyfile("./" + filename + ".txt",
                            "./output/" + filename + "_copy.txt")
        finally:
            pass
