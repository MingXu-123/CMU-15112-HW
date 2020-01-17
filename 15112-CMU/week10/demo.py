import os
def printFiles(path):
    # Base Case: a file. Print the path name directly.
    if os.path.isfile(path):
        print(path)
    else:
        # Recursive Case: a directory. Iterate through its files and directories.
        # Note that we have to update the path name to access the inner files!
        for filename in os.listdir(path):
            printFiles(path + "/" + filename)

printFiles("sampleFiles")

# Note: if you see .DS_Store files in the sampleFiles folders, or in the
# output of your function (as often happens with Macs, in particular),
# don't worry; this is just a metadata file and can be safely ignored.


import os
def listFiles(path):
    if os.path.isfile(path):
        # Base Case: return a list of just this file
        return [ path ]
    else:
        # Recursive Case: create a list of all the recursive results from the files in the folder
        files = [ ]
        for filename in os.listdir(path):
            files += listFiles(path + "/" + filename)
        return files

print(listFiles("sampleFiles"))


import os
def removeTmpFiles(path):
    if path.split("/")[-1] == '.DS_Store':
        os.remove(path)
    elif os.path.isdir(path):
        for filename in os.listdir(path):
            removeTmpFiles(path + "/" + filename)


