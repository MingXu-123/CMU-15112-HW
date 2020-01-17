from tkinter import *

def init(data):
    data.level = 1
    data.depth = -1
    data.color = ['yellow', 'red', 'orange', '#FFE4C4', 'blue']
    data.lineColor = ['#F5FFFA', 'yellow', 'orange', 'purple', 'pink']
    data.smallCircleColor = ['#F5FFFA', 'red', 'orange', 'purple', 'pink']

def drawCircle(canvas, data, xc, yc, r, depth):
    canvas.create_oval(xc - r / 4, (yc - 2 * r) - r / 4,
                       xc + r / 4, (yc - 2 * r) + r / 4,
                       fill=data.smallCircleColor[depth])
    canvas.create_oval(xc - r / 4, (yc + 2 * r) - r / 4,
                       xc + r / 4, (yc + 2 * r) + r / 4,
                       fill=data.smallCircleColor[depth])
    canvas.create_oval((xc - 2 * r) - r / 4, yc - r / 4,
                       (xc - 2 * r) + r / 4, yc + r / 4,
                       fill=data.smallCircleColor[depth])
    canvas.create_oval((xc + 2 * r) - r / 4, yc - r / 4,
                       (xc + 2 * r) + r / 4, yc + r / 4,
                       fill=data.smallCircleColor[depth])
    canvas.create_oval(xc + 2 ** 0.5 * r - r / 4, yc - 2 ** 0.5 * r - r / 4,
                       xc + 2 ** 0.5 * r + r / 4, yc - 2 ** 0.5 * r + r / 4,
                       fill=data.smallCircleColor[depth])
    canvas.create_oval(xc - 2 ** 0.5 * r - r / 4, yc - 2 ** 0.5 * r - r / 4,
                       xc - 2 ** 0.5 * r + r / 4, yc - 2 ** 0.5 * r + r / 4,
                       fill=data.smallCircleColor[depth])
    canvas.create_oval(xc - 2 ** 0.5 * r - r / 4, yc + 2 ** 0.5 * r - r / 4,
                       xc - 2 ** 0.5 * r + r / 4, yc + 2 ** 0.5 * r + r / 4,
                       fill=data.smallCircleColor[depth])
    canvas.create_oval(xc + 2 ** 0.5 * r - r / 4, yc + 2 ** 0.5 * r - r / 4,
                       xc + 2 ** 0.5 * r + r / 4, yc + 2 ** 0.5 * r + r / 4,
                       fill=data.smallCircleColor[depth])


def drawLinesAndCircles(canvas, data, xc, yc, r, depth):
    canvas.create_line(xc, yc, xc, yc - 2 * r, fill=data.lineColor[depth])
    canvas.create_line(xc, yc, xc, yc + 2 * r, fill=data.lineColor[depth])
    canvas.create_line(xc + 2 * r, yc, xc, yc, fill=data.lineColor[depth])
    canvas.create_line(xc - 2 * r, yc, xc, yc, fill=data.lineColor[depth])
    canvas.create_line(xc, yc, xc + 2 ** 0.5 * r, yc - 2 ** 0.5 * r,
                       fill=data.lineColor[depth])
    canvas.create_line(xc, yc, xc - 2 ** 0.5 * r, yc - 2 ** 0.5 * r,
                       fill=data.lineColor[depth])
    canvas.create_line(xc, yc, xc - 2 ** 0.5 * r, yc + 2 ** 0.5 * r,
                       fill=data.lineColor[depth])
    canvas.create_line(xc, yc, xc + 2 ** 0.5 * r, yc + 2 ** 0.5 * r,
                       fill=data.lineColor[depth])
    drawCircle(canvas, data, xc, yc, r, depth)


def drawFractalSun(data, canvas, xc, yc, r, level, depth):
    if level == 0:
        # this following code is only for state level == 0
        margin = min(data.width, data.height) // 10
        canvas.create_oval(data.width // 2 - 0.6 * data.width // 5,
                           data.height // 2 - 0.6 * data.width // 5,
                           data.width // 2 + 0.6 * data.width // 5,
                           data.height // 2 + 0.6 * data.width // 5, fill= '#FFDAB9')
        canvas.create_text(data.width / 2, 0,
                           text="Level %d Fractal" % (data.level),
                           font="Arial " + str(int(margin / 3)) + " bold",
                           anchor="n", fill='white')
        canvas.create_text(data.width / 2, margin,
                           text="Use arrows to change level",
                           font="Arial " + str(int(margin / 4)),
                           anchor="s", fill='white')
    elif level == 1:
        drawLinesAndCircles(canvas, data, xc, yc, r, depth)
        canvas.create_oval(xc - r, yc - r, xc + r, yc + r, fill=data.color[depth])
    else:
        drawFractalSun(data, canvas, xc, yc, r, level - 1, depth + 1)
        drawFractalSun(data, canvas, xc, yc - 2 * r, r / 4, level - 1, depth - 1)
        drawFractalSun(data, canvas, xc, yc + 2 * r, r / 4, level - 1, depth - 1)
        drawFractalSun(data, canvas, xc - 2 * r, yc, r / 4, level - 1, depth - 1)
        drawFractalSun(data, canvas, xc + 2 * r, yc, r / 4, level - 1, depth - 1)
        drawFractalSun(data, canvas, xc + 2 ** 0.5 * r, yc - 2 ** 0.5 * r, r / 4, level - 1, depth - 1)
        drawFractalSun(data, canvas, xc - 2 ** 0.5 * r, yc - 2 ** 0.5 * r, r / 4, level - 1, depth - 1)
        drawFractalSun(data, canvas, xc - 2 ** 0.5 * r, yc + 2 ** 0.5 * r, r / 4, level - 1, depth - 1)
        drawFractalSun(data, canvas, xc + 2 ** 0.5 * r, yc + 2 ** 0.5 * r, r / 4, level - 1, depth - 1)



def keyPressed(event, data):
    if event.keysym in ["Up", "Right"]:
        data.level += 1
    elif (event.keysym in ["Down", "Left"]) and (data.level > 0):
        data.level -= 1


def drawCanvas(canvas, data):
    topX = 0
    topY = 0
    canvas.create_rectangle(topX, topY, data.width, data.height, fill= 'black')


def redrawAll(canvas, data):
    drawCanvas(canvas, data)
    margin = min(data.width, data.height)//10
    xc, yc = data.width // 2, data.height // 2
    r = 0.6*data.width // 5
    drawFractalSun(data, canvas, xc, yc, r, data.level, data.depth)
    canvas.create_text(data.width / 2, 0,
                       text="Level %d Fractal" % (data.level),
                       font="Arial " + str(int(margin / 3)) + " bold",
                       anchor="n", fill = 'white')
    canvas.create_text(data.width / 2, margin,
                       text="Use arrows to change level",
                       font="Arial " + str(int(margin / 4)),
                       anchor="s", fill = 'white')

def mousePressed(event, data): pass

def timerFired(data): pass

# Updated Animation Starter Code

####################################
# use the run function as-is
####################################

def run(width=500, height=500):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        canvas.create_rectangle(0, 0, data.width, data.height,
                                fill='white', width=0)
        redrawAll(canvas, data)
        canvas.update()

    def mousePressedWrapper(event, canvas, data):
        mousePressed(event, data)
        redrawAllWrapper(canvas, data)

    def keyPressedWrapper(event, canvas, data):
        keyPressed(event, data)
        redrawAllWrapper(canvas, data)

    def timerFiredWrapper(canvas, data):
        timerFired(data)
        redrawAllWrapper(canvas, data)
        # pause, then call timerFired again
        canvas.after(data.timerDelay, timerFiredWrapper, canvas, data)
    # Set up data and call init
    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    data.timerDelay = 100 # milliseconds
    root = Tk()
    root.resizable(width=False, height=False) # prevents resizing window
    init(data)
    # create the root and the canvas
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.configure(bd=0, highlightthickness=0)
    canvas.pack()
    # set up events
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    timerFiredWrapper(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed
    print("bye!")

run(500, 500)
