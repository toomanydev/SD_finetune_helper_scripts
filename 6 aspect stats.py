from fractions import Fraction
import os
from PIL import Image

# Tells you some stats about your aspect ratio'd dataset.

resolutions = []
total_images = 0
orientation_counts = [0, 0, 0]

log = []

for file in os.listdir("./"):
    filename, file_extension = os.path.splitext(file)
    if file_extension == ".png":
        image = Image.open(file)
        total_images = total_images + 1

        resolution_exists = False
        for resolution in resolutions:
            if resolution[0] == image.width and resolution[1] == image.height:
                resolution[2] = resolution[2] + 1
                resolution_exists = True

        if resolution_exists is False:
            resolutions.append([image.width, image.height, 1])

        if image.width < image.height:
            orientation_counts[0] = orientation_counts[0] + 1
        elif image.width == image.height:
            orientation_counts[1] = orientation_counts[1] + 1
        else:
            orientation_counts[2] = orientation_counts[2] + 1

for resolution in resolutions:
    dataset_percent = round((resolution[2] / total_images) * 100, 2)

    orientation_percent = 0
    if resolution[0] < resolution[1]:
        orientation_percent = resolution[2] / orientation_counts[0]
    elif resolution[0] == resolution[1]:
        orientation_percent = resolution[2] / orientation_counts[1]
    else:
        orientation_percent = resolution[2] / orientation_counts[2]
    orientation_percent = round(orientation_percent * 100, 2)

    aspect_ratio = round(resolution[0] / resolution[1],2)

    log_line = f"{resolution[0]} x {resolution[1]}: {resolution[2]}.\t\tAspect: {aspect_ratio}\t{Fraction(resolution[0], resolution[1])}\t\tPercent of dataset: {dataset_percent}%\t\tPercent of orientation: {orientation_percent}%"
    print(log_line)
    log.append(log_line)

log_line = f"Total images: {total_images}\tTotal portrait: {orientation_counts[0]}\tTotal square: {orientation_counts[1]}\t\t\tTotal landscape: {orientation_counts[2]}"
print(log_line)
log.append(log_line)

with open('.aspect_stats.txt', 'w', encoding="utf8") as log_file:
    for line in log:
        log_file.write("".join(line) + "\n")
