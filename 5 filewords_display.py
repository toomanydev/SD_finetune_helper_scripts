import os, fnmatch

# Displays all the filewords in an SD training directory, so you can quickly see
# if any tags that are obviously mistakes. Can then use recursive_replace to fix.

fileword_tags = {}

def getFilewords(directory, filePattern):
    for path, dirs, files in os.walk(os.path.abspath(directory)):
        for filename in fnmatch.filter(files, filePattern):
            filepath = os.path.join(path, filename)
            with open(filepath) as f:
                text = f.read()
                add_to_dict(text.split(", "))

def add_to_dict(tags):
    for tag in tags:
        for entry in fileword_tags:
            if entry == tag:
                fileword_tags[tag] = fileword_tags[tag] + 1
        if tag not in fileword_tags:
            fileword_tags[tag] = 1


getFilewords("./", "*.txt")

for tag in fileword_tags:
    print(fileword_tags[tag], "\t", tag)