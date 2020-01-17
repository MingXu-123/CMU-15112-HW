from tkinter import *

def makeUpString(text):
    lines = text.split("\n")
    maxLenOfLine = len(max(lines, key=len))
    result = ""
    for line in lines:
        blanks = maxLenOfLine - len(line)
        result += (line + blanks * " " + "\n")
    result = result[:-1]
    result = "".join(result)
    return result

def findRowOfCanvas(text):
    text = makeUpString(text)
    height = 0
    for c in text:
        if c == "\n":
            height += 1
    height += 1
    return height

def findColOfcanvas(text):
    text = makeUpString(text)
    column = 0
    for line in text.split("\n"):
        column = len(line)
        break
    return column


def asciiDraw(canvas, artStr, width, height):
    newText = makeUpString(artStr)
    rowOfCanvas = findRowOfCanvas(newText)
    colOfCanvas = findColOfcanvas(newText)
    heightOfRectangle = height / rowOfCanvas
    widthOfRectangle = width / colOfCanvas
    j = 0
    for line in newText.split("\n"):
        for i in range(len(line)):
            left = 0 + i * widthOfRectangle
            top = 0 + j * heightOfRectangle
            right = left + widthOfRectangle
            bottom = top + heightOfRectangle
            color = ""
            if line[i] == "0":color = "#000"
            elif line[i] == "1": color = "#00F"
            elif line[i] == "2": color = "#0F0"
            elif line[i] == "3": color = "#0FF"
            elif line[i] == "4": color = "#F00"
            elif line[i] == "5": color = "#F0F"
            elif line[i] == "6": color = "#FF0"
            elif line[i] == "7": color = "#FFF"
            canvas.create_rectangle(left, top, right, bottom, fill=color, width=0)
        j += 1


def runAsciiDraw(artStr, width, height):
    root = Tk()
    root.resizable(width=False, height=False) # prevents resizing window
    canvas = Canvas(root, width=width, height=height)
    canvas.configure(bd=0, highlightthickness=0)
    canvas.pack()
    asciiDraw(canvas, artStr, width, height)
    root.mainloop()


artStr = ''' 
  1     2     4
 111   222   444
11111 22222 44444
 111   222   444
  1     2     4
 '''


facePattern = ''' 
                          0022222222222222222
                      02222222222222222222222220
                   02222222222222222222222222222220         02   02 02
   0 0 0        02222222222222222222222222222222222220       02 22 2202
0 2 2 02      0222222222    2222222222222    2222222220       02202202
022222202     0222222222      22222222222      22222222220    02222222
  0222222    02222222222      22222222222      22222222222222222222222
  02222222222222222222222    2222222222222    22222222222222  0222
   022202222222222222222222222222222222222222222222222222222    0222
    022   022222222222222222222222222222222222222222222222222     02220
   0220   222222222222222222222222222222222222222222222222222       2220
   022    222222222222222222222222222222222222222222222000222222022220
  0222022222  2222222222222222222222222222222222222   022222222222222222
  0222   202222   2222222222222222222222222222222222     02220
 0222       0222    022222222222222222222222222220      0222
            02220     02222222222222222220220           022
              0220          02202222220              0222
               02220                                02220
                022220      02222220022220        02222
                  0222220     022222222220   022220
                     0222220  022222222222220
                        02222222022222222222
                                022222222222
                                   022222222222
                                     02222222220
                                      02220

 '''



print(repr(artStr))
print(artStr)
print(artStr.split("\n"))
print("hhh")
print(makeUpString(artStr))
# print(makeUpString(artStr).split("\n"))
print("hhhhhhhh")
print(makeUpString(facePattern))

# print(findRowOfCanvas(artStr))
# print(findRowOfCanvas("0123\n4567"))
# print(repr(makeUpString("0123\n4567")))
print("hhhhhh")
# print(findColOfcanvas(artStr))
# asciiDraw(artStr, 600, 300)

runAsciiDraw(facePattern, 800, 600)