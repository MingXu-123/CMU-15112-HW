from tkinter import *


def almostEqual(x, y):
    return abs(x - y) < 10**-9

def drawThreadPattern(canvas, size, numSpokes, startSpoke, numSkips):
    #print("I am here")
    import math
    (cx, cy, r) = (size/2, size/2, size/2 * 0.9)
    canvas.create_oval(cx - r, cy - r, cx + r, cy + r, outline='black', width=r/30)
    for i in range(numSpokes):
        iAngle = math.pi / 2 - (2 * math.pi) * (i / numSpokes) - math.pi  # !!!!!!!!!!!!!
        ix = cx + r * math.cos(iAngle)
        iy = cy - r * math.sin(iAngle)
        ixt = cx + 0.85 * r * math.cos(iAngle)
        iyt = cy - 0.85 * r * math.sin(iAngle)

        canvas.create_line(ixold, iyold, ixnew, iynew, width=1)
        canvas.create_text(ixt, iyt, text= str(i), font="Arial 16 bold", width=10)
        if i == startSpoke:
            canvas.create_oval(ix - (r/20)*1.2, iy - (r/20)*1.1, ix + (r/20)*1.1, iy + (r/20)*1.1,
                           fill='green', outline='black', width=1)
        else:
            canvas.create_oval(ix - (r / 20) * 1.2, iy - (r / 20) * 1.1, ix + (r / 20) * 1.1, iy + (r / 20) * 1.1,
                               fill='red', outline='black', width=1)

    for n in range(numSpokes):
        if n == startSpoke:
            begin = True
            fixAngle = math.pi / 2 - (2 * math.pi) * (n / numSpokes) - math.pi
            xfix = cx + 0.95 * r * math.cos(fixAngle)
            yfix = cy - 0.95 * r * math.sin(fixAngle)
            print(xfix, yfix)
            nAngle = math.pi / 2 - (2 * math.pi) * (n / numSpokes) - math.pi
            nxold = cx + 0.95 * r * math.cos(nAngle)
            nyold = cy - 0.95 * r * math.sin(nAngle)
            while begin:
                # nAngle = math.pi / 2 - (2 * math.pi) * (n / numSpokes) - math.pi
                # nxold = cx + 0.95 * r * math.cos(nAngle)
                # nyold = cy - 0.95 * r * math.sin(nAngle)
                nAnglenew = nAngle - (2 * math.pi) * (numSkips/numSpokes)
                nxnew = cx + 0.95 * r * math.cos(nAnglenew)
                nynew = cy - 0.95 * r * math.sin(nAnglenew)
                canvas.create_line(nxold, nyold, nxnew, nynew, width=1)
                nAngle = nAnglenew
                #print(nxnew, nynew)
                if abs(nxnew - xfix) < 0.0001 and abs(nynew - yfix) < 0.0001:
                    break
                nxold, nyold = nxnew, nynew





def runDrawThreadPattern(width, height, numSpokes, startSpoke, numSkips):
    root = Tk()
    root.resizable(width=False, height=False) # prevents resizing window
    canvas = Canvas(root, width=width, height=height)
    canvas.configure(bd=0, highlightthickness=0)
    canvas.pack()
    # width must equal height
    assert(width == height)
    drawThreadPattern(canvas, width, numSpokes, startSpoke, numSkips)
    root.mainloop()


def testDrawThreadPattern():
    print("Testing drawThreadPattern...", end="")
    runDrawThreadPattern(400, 400, 12, 0, 5)
    runDrawThreadPattern(200, 200, 10, 3, 4)
    runDrawThreadPattern(500, 500, 19, 8, 15)
    print("Done.")

testDrawThreadPattern()
