from tkinter import *


def drawCircle(canvas, x0, y0, x1, y1, r, color):
    (cx, cy, r) = (x0 + (x1 - x0)/2, y0 + (y1 - y0)/2, r)
    while r >= 1:
        canvas.create_oval(cx - r, cy - r, cx + r, cy + r, fill=color, outline='black')
        r = (2/3) * r


def drawButtonPattern(canvas, size, n):
    canvas.create_rectangle(0, 0, size, size, fill="purple")
    width = size / n
    r = width / 2
    for col in range(n):
        for row in range(n):
            print('col',col,'row', row)
            left = 0 + width * col
            top = 0 + width * row
            right = width * (col + 1)
            bottom = width * (row + 1)
            # print(left, top, right, bottom)
            # color = 'green'
            if (col + row) % 4 == 0:
                color = 'red'
                drawCircle(canvas, left, top, right, bottom, r, color)
            if row % 3 == 0:
                if (col + row) % 4 != 0:
                    color = 'green'
                    drawCircle(canvas, left, top, right, bottom, r, color)

            if col % 2 == 1:
                if ((row - 1) % 12) == 0 or ((row - 5) % 12 == 0):
                    if (col - 1) % 4 == 0:
                        color = 'yellow'
                        drawCircle(canvas, left, top, right, bottom, r, color)

                if ((row - 7) % 12) == 0 or ((row - 11) % 12 == 0):
                    if (col - 3) % 4 == 0:
                        color = 'yellow'
                        drawCircle(canvas, left, top, right, bottom, r, color)

                if ((row - 2) % 6 == 0) or ((row - 4) % 6 == 0):
                    if col % 2 == 1:
                        color = 'yellow'
                        drawCircle(canvas, left, top, right, bottom, r, color)
            if (row - 1) % 6 == 0 or (row - 5) % 6 == 0:
                if col % 2 == 0:
                    color = 'blue'
                    drawCircle(canvas, left, top, right, bottom, r, color)
            if (row - 2) % 12 == 0 or (row - 10) % 12 == 0:
                if (col - 4) % 4 == 0:
                    color = 'blue'
                    drawCircle(canvas, left, top, right, bottom, r, color)
            if (row - 4) % 12 == 0 or (row - 8) % 12 == 0:
                if (col - 2) % 4 == 0:
                    color = 'blue'
                    drawCircle(canvas, left, top, right, bottom, r, color)







            # else:
            #     color = 'green'
            # drawCircle(canvas, left, top, right, bottom, r, color)




def runDrawButtonPattern(width, height, n):
    root = Tk()
    root.resizable(width=False, height=False) # prevents resizing window
    canvas = Canvas(root, width=width, height=height)
    canvas.configure(bd=0, highlightthickness=0)
    canvas.pack()
    # width must equal height
    assert(width == height)
    drawButtonPattern(canvas, width, n)
    root.mainloop()


def testDrawButtonPattern():
    print("Testing drawButtonPattern()...", end="")
    runDrawButtonPattern(400, 400, 10)
    runDrawButtonPattern(300, 300, 5)
    runDrawButtonPattern(250, 250, 25)
    print("Done.")

testDrawButtonPattern()