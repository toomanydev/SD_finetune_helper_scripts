import os

# Renames grid samples, when training, so they're easier to compare by name in explorer
# Do not recall exact function of script, good luck! :)

def rename_grid_samples(name, steps, zero_pad):
    files = os.listdir()
    count = 0

    for file in files:
        if file.startswith("grid-"):
            filename, file_extension = os.path.splitext(file)
            os.rename(file, f"{name}_{str(steps*count).zfill(zero_pad)}{file_extension}")
            count = count + 1


rename_grid_samples("Name", 150, 6)

# In the event of an accident, can batch rename starting with "grid-".
