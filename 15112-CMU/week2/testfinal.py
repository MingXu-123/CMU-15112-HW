from tkinter import *


def almostEqual(x, y):
    return abs(x - y) < 10**-9

def drawThreadPattern(canvas, size, numSpokes, startSpoke, numSkips):
    import math
    (cx, cy, r) = (size/2, size/2, size/2 * 0.9)
    canvas.create_oval(cx - r, cy - r, cx + r, cy + r, outline='black', width=r/30)
    for i in range(numSpokes):
        iAngle = math.pi / 2 - (2 * math.pi) * (i / numSpokes) + math.pi #!!!!!!!!!!!!!
        ix = cx + r * math.cos(iAngle)
        iy = cy - r * math.sin(iAngle)
        ixold = cx + 0.95 * r * math.cos(iAngle)
        iyold = cy - 0.95 * r * math.sin(iAngle)

        iAnglenew = math.pi / 2 - (2 * math.pi) * ((i + numSkips) / numSpokes) + math.pi
        ixnew = cx + 0.95 * r * math.cos(iAnglenew)
        iynew = cy - 0.95 * r * math.sin(iAnglenew)
        ixt = cx + 0.85 * r * math.cos(iAngle)
        iyt = cy - 0.85 * r * math.sin(iAngle)

        # canvas.create_line(ixold, iyold, ixnew, iynew, width=1)
        canvas.create_text(ixt, iyt, text= str(i), font="Arial 16 bold", width=10)
        if i == startSpoke:
            canvas.create_oval(ix - (r/20)*1.2, iy - (r/20)*1.1, ix + (r/20)*1.1, iy + (r/20)*1.1,
                           fill='green', outline='black', width=1)
            ixfix = ixold
            iyfix = iyold
            begin = True
            # while ixnew != ixfix and iynew != iyfix:
            while begin:
                canvas.create_line(ixold, iyold, ixnew, iynew, width=1)
                ixold = ixnew
                iyold = iynew
                # iAnglenew = math.pi / 2 - (2 * math.pi) * ((i + numSkips) / numSpokes) + math.pi
                iAnglenew = iAnglenew - (2 * math.pi) * (numSkips / numSpokes)
                ixnew = cx + r * math.cos(iAnglenew)
                iynew = cy - r * math.sin(iAnglenew)

                if almostEqual(ixnew, ixfix) and almostEqual(iynew, iyfix):
                    begin = False
                #     break
                print(ixold, iyold, ixnew, iynew)
        else:
            canvas.create_oval(ix - (r / 20) * 1.2, iy - (r / 20) * 1.1, ix + (r / 20) * 1.1, iy + (r / 20) * 1.1,
                               fill='red', outline='black', width=1)
        # canvas.create_line(ixold, iyold, ixnew, iynew, width = 1)
        # print(ix, iy, ixnew, iynew)
        #!!!!!!!!!!!用index试试




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