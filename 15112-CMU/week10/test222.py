import os

def findLargestFile(path):
    if os.path.isfile(path):
        return path
    else:
        largestFile = 0
        largestFilePath = ""
        for filename in os.listdir(path):
            if filename.startswith('.'):
                continue
            tempPath = findLargestFile(path + "/" + filename)
            if os.path.isfile(tempPath):
                temp = os.path.getsize(tempPath)
                if largestFile < temp:
                    largestFile = temp
                    largestFilePath = tempPath
        return largestFilePath






