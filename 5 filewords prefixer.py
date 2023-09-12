import os, fnmatch

# Adds a prefix to all the filewords text files in the directory

def findReplace(directory, prefixString, filePattern):
    for path, dirs, files in os.walk(os.path.abspath(directory)):
        for filename in fnmatch.filter(files, filePattern):
            filepath = os.path.join(path, filename)
            with open(filepath, "r+") as f:
                text = f.read()
                text = prefixString + text
                f.seek(0)
                f.write(text)


findReplace("./", "name, ", "*.txt")
