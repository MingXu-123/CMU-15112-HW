from tkinter import *
# transfer orginal string to string with the same length of each line
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
    newtext = makeUpString(artStr)

    return






def runAsciiDraw(artStr, width, height):
    root = Tk()
    root.resizable(width=False, height=False) # prevents resizing window
    canvas = Canvas(root, width=width, height=height)
    canvas.configure(bd=0, highlightthickness=0)
    canvas.pack()
    asciiDraw(canvas, artStr, width, height)
    root.mainloop()


def testAsciiDraw():
    testPattern = "0123\n4567"
    print("Testing asciiDraw with color pattern:\n", testPattern, end="")
    runAsciiDraw(testPattern, 600, 300)

    diamondPattern = ''' 
  1     2     4
 111   222   444
11111 22222 44444
 111   222   444
  1     2     4
 '''

    print("Testing asciiDraw with diamond pattern:\n", diamondPattern, end="")
    runAsciiDraw(diamondPattern, 600, 300)

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
    print("Testing asciiDraw with face pattern:\n", facePattern, end="")
    runAsciiDraw(facePattern, 800, 600)

    hourglassPattern = ''' 
                            0000
        00000000000000000000    00
00000000            0000000000000 00
0 000000000000000000         000000 00
0000                11111    0 0   00 00
00 0        111111111111111110 0   0000 0
 0 000000111111111111111111110 00000 0000
 0 0   0 111111111111111111110 0   0 0
 0 0   0 111111111111111555550 0   0 0
 0 0   0 111111111555644644640 0   0 0
 0 0   0 111115546446446446440 0   0 0
 0 0   0 111546464464464464460 0   0 0
 0 0   0 154644644644644646660 0   0 0
 0 0   0 056446446446666666660 0   0 0
 0 0   0 0 5666666666666666650 0   0 0
 0 0   0 0  566666666666666510 0   0 0
 0 0   0 0   16666666666661  0 0   0 0
 0 0   0 0    116666666651   0 0   0 0
 0 0   0 0       1156111     0 0   0 0
 0 0   0 0         55        0 0   0 0
 0 0   0 0      11165111     0 0   0 0
 0 0   0 0    1111156111111  0 0   0 0
 0 0   0 0   111111551111111 0 0   0 0
 0 0   0 0  111111165111111110 0   0 0
 0 0   0 0 1111111155111111110 0   0 0
 0 0   0 011111111161111111110 0   0 0
 0 0   0 011111111161111111110 0   0 0
 0 0   0 111111115666511111110 0   0 0
 0 0   0 111111156666651111110 0   0 0
 0 0   0 111111566666665111110 0   0 0
 0 0   01111115666666666511110 0   0 0
 0 0 0001111156666666666651110 00000 0000
 0 00   1111566666666666665110 0   000 00
 0 0    1111566666666666666510 0     00 0
00000   0115666666666666666510 0   00  00
0    00000000006666660000    000 00  00
0000000000000  111111  0000000000  00
            00000000000000000000000
 '''
    print("Testing asciiDraw with hourglass pattern:\n", hourglassPattern, end="")
    runAsciiDraw(hourglassPattern, 400, 600)
    print("Done testing asciiDraw!")


testAsciiDraw()