import os
from PIL import Image

# Buckets towards a ratio of 1.0. So if manually cropping then running this, use a ratio that is larger, then just swap the width/height.
# e.g. bucket is 832x640, 1.30 ratio. Crop to 1.30+
#
# Notes on Print Output
#
# % Pixels of Square = how large the image is in total.
# Each image should be as close to 100% as possible, otherwise effectively training at lower resolution for that aspect ratio.
# If over 100% then more VRAM would be needed, potentially causing OOM where otherwise Aspect Bucketing would be free memory-wise.
#
# Crop Lost Dim %:
# The vertical/horizontal % that was lost to cropping, meaning the detail in that part of the image is lost.
# Needs to be limited to prevent cutting off important parts, but a small crop shouldn't hurt most images.

output_dir = "./768_aspected"

buckets_input = [  # Resolutions will also be done flipped, so only need one (landscape/portrait) of each aspect ratio
    (768, 768),  # Make sure first bucket is your 1:1 resolution, such as 512x512.
    (832, 640),
]

buckets = []
log = []

for bucket in buckets_input:
    buckets.append((bucket[0], bucket[1]))
    buckets.append((bucket[1], bucket[0]))

print(buckets)

bucket_ratios = []
square_pixels = buckets[0][0] * buckets[0][1]

try:
    os.mkdir(output_dir)
except FileExistsError:
    pass

for i, bucket in enumerate(buckets):
    bucket_ratios.append(bucket[0] / bucket[1])

print(" images ")

for file in os.listdir("./"):
    filename, file_extension = os.path.splitext(file)
    if file_extension == ".png":
        image = Image.open(file)
        aspect_ratio = image.width / image.height

        chosen_bucket_ratio = 1
        chosen_resolution = buckets[0]

        smaller_dim = min(image.width, image.height)
        longer_dim = max(image.width, image.height)

        for bucket_ratio in bucket_ratios:
            if aspect_ratio < 1:
                if bucket_ratio > aspect_ratio and bucket_ratio < chosen_bucket_ratio:
                    chosen_bucket_ratio = bucket_ratio
                
            elif aspect_ratio > 1:
                if bucket_ratio < aspect_ratio and bucket_ratio > chosen_bucket_ratio:
                    chosen_bucket_ratio = bucket_ratio
        
        for bucket in buckets:
            bucket_ratio = bucket[0] / bucket[1]
            if bucket_ratio == chosen_bucket_ratio:
                chosen_resolution = bucket
        
        bucket_pixels = chosen_resolution[0] * chosen_resolution[1]

        resized_smaller_dim = 0
        resized_longer_dim = 0

        if aspect_ratio < 1:
            # Portrait
            shrink_ratio = smaller_dim / chosen_resolution[0]
            resized_smaller_dim = chosen_resolution[0]
            resized_longer_dim = int(longer_dim / shrink_ratio)
            image = image.resize([resized_smaller_dim, resized_longer_dim],  Image.Resampling.LANCZOS)
        else:
            shrink_ratio = smaller_dim / chosen_resolution[1]
            resized_smaller_dim = chosen_resolution[1]
            resized_longer_dim = int(longer_dim / shrink_ratio)
            image = image.resize([resized_longer_dim, resized_smaller_dim],  Image.Resampling.LANCZOS)
    
        resized_pixels = resized_smaller_dim * resized_longer_dim
        crop_pixels = resized_longer_dim - max(chosen_resolution[0],chosen_resolution[1])

        if aspect_ratio < 1:
            crop_pixels_first = int(crop_pixels - (crop_pixels / 2))
            crop_pixels_second = crop_pixels - crop_pixels_first
            image = image.crop((0,crop_pixels_first,image.width,image.height-crop_pixels_second))
        else:
            crop_pixels_first = int(crop_pixels - (crop_pixels / 2))
            crop_pixels_second = crop_pixels - crop_pixels_first
            image = image.crop((crop_pixels_first,0,image.width-crop_pixels_second,image.height))

        lost_dim_percent = 0
        if chosen_resolution != bucket[0]:
            lost_dim_percent = resized_longer_dim / max(image.width, image.height)
        

        image.save(f"{output_dir}/{file}")

        log_line = "aspect: " + str(round(aspect_ratio,2)) + " \t\tbucket: " + str(round(chosen_bucket_ratio,2)) + " \t\t chosen: " + str(chosen_resolution) + " \t\t Pixels: " + str(bucket_pixels) + \
                   " \t\t % Pixels of Square: " + str(round((bucket_pixels/square_pixels)*100,1)) + "%" + " \t\t Crop Lost Dim %: " + str(round((lost_dim_percent-1)*100,1)) + "%"
        print(log_line)
        log.append(log_line)

with open(f'{output_dir}/.aspect_bucket_crop.txt', 'w', encoding="utf8") as log_file:
    for line in log:
        log_file.write("".join(line) + "\n")
