import os
def printFiles(path):
    # Base Case: a file. Print the path name directly.
    if os.path.isfile(path):
        print(path)
    else:
        # Recursive Case: a directory. Iterate through its files and directories.
        # Note that we have to update the path name to access the inner files!
        print(os.listdir(path))
        for filename in os.listdir(path):
            printFiles(path + "/" + filename)

printFiles("sampleFiles")

# Note: if you see .DS_Store files in the sampleFiles folders, or in the
# output of your function (as often happens with Macs, in particular),
# don't worry; this is just a metadata file and can be safely ignored.
print("###########################")

def listFiles(path):
    if os.path.isfile(path):
        # Base Case: return a list of just this file
        return [ path ]
    else:
        # Recursive Case: create a list of all the recursive results from the files in the folder
        files = [ ]
        for filename in os.listdir(path):
            # print(filename)
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


# def findLargestFile(path):
#     if os.path.isfile(path):
#         return path
#     else:
#         largestFile = 0
#         largestFilePath = ""
#         for filename in os.listdir(path):
#             if filename.startswith('.'):
#                 continue
#             tempPath = findLargestFile(path + "/" + filename)
#             if os.path.isfile(tempPath):
#                 temp = os.path.getsize(tempPath)
#                 if largestFile < temp:
#                     largestFile = temp
#                     largestFilePath = tempPath
#         return largestFilePath


# print(removeTmpFiles("sampleFiles"))
print("")

def findLargestFileHelper(path, res, largestFilePath):
    if os.path.isfile(path):
        return path
    else:
        for filename in os.listdir(path):
            if filename == '.DS_Store':
                continue
            tmpPath = findLargestFileHelper(path + "/" + filename,
                                            res, largestFilePath)
            if not os.path.isfile(tmpPath):
                continue
            tmpValue = os.path.getsize(tmpPath)
            if tmpValue >= largestFilePath:
                largestFilePath = tmpValue
                res = tmpPath
        return res


def findLargestFile(path):
    largestFilePath = 0
    res = ""
    return findLargestFileHelper(path, res, largestFilePath)



print(findLargestFile("sampleFiles/folderA"))
print(findLargestFile("sampleFiles/folderB"))
print(findLargestFile("sampleFiles/folderB/folderF"))
