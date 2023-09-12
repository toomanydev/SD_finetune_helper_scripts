import os, fnmatch

# Replaces text in the text files of the directory this is run in.
# "./", "dog", "", "*.txt" will replace "dog" with "", basically deleting it.
# Careful, doesn't make backups!

def findReplace(directory, find, replace, filePattern):
    for path, dirs, files in os.walk(os.path.abspath(directory)):
        for filename in fnmatch.filter(files, filePattern):
            filepath = os.path.join(path, filename)
            with open(filepath) as f:
                s = f.read()
            s = s.replace(find, replace)
            with open(filepath, "w") as f:
                f.write(s)

findReplace("./", "dog", "", "*.txt")
