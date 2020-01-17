#################################################
# Hw5
# Your andrewID:mxu2
# Your section: 2N
#################################################

import random

#################################################
# Hw5 Ball Problem
#################################################
from tkinter import *


# This is the model of the animation
def init(data):
    data.score = 0
    data.rx0 = 0
    data.ry0 = 0
    data.rcSpeedX = 20
    data.rcSpeedY = 20
    data.ballSpeedX = 2
    data.ballSpeedY = 2
    data.timerDelay = 10
    data.isPaused = False
    data.ballPosition = [random.randrange(data.rx0, data.rx0 + 1.5 * data.width),
                         random.randrange(data.ry0, data.ry0 + 1.5 * data.height)]
    data.ballSize = data.width / 10


# This is the mouse press handler
def mousePressed(event, data):
    if data.ballPosition[0] < event.x < data.ballPosition[0] + data.ballSize \
            and data.ballPosition[1] < event.y < data.ballPosition[1] + data.ballSize:
        data.isPaused = not data.isPaused


# This function is the keyboard handler
def keyPressed(event, data):
    if event.keysym == "Left":
        data.rx0 += data.rcSpeedX
        data.ballPosition[0] += data.rcSpeedX
    elif event.keysym == "Right":
        data.rx0 -= data.rcSpeedX
        data.ballPosition[0] -= data.rcSpeedX
    elif event.keysym == "Up":
        data.ry0 += data.rcSpeedY
        data.ballPosition[1] += data.rcSpeedY
    elif event.keysym == "Down":
        data.ry0 -= data.rcSpeedY
        data.ballPosition[1] -= data.rcSpeedY


# This is the timer function
def timerFired(data):
    if not data.isPaused:
        doStep(data)
        if data.ballPosition[0] + data.ballSize < 0 \
                or data.ballPosition[0] > data.width \
                or data.ballPosition[1] + data.ballSize < 0 \
                or data.ballPosition[1] > data.height:
            data.score += 0
        else:
            data.score += 1


# This is the do step function the will be called regularly according to the timer
def doStep(data):
    data.ballPosition[0] += data.ballSpeedX
    if data.ballPosition[0] < data.rx0 or\
            data.ballPosition[0] + data.ballSize > data.rx0 + 1.5 * data.width:
        data.ballSpeedX = - data.ballSpeedX
        data.ballPosition[0] += data.ballSpeedX

    data.ballPosition[1] += data.ballSpeedY
    if data.ballPosition[1] < data.ry0 or\
            data.ballPosition[1] + data.ballSize > data.ry0 + 1.5 * data.height:
        data.ballSpeedY = - data.ballSpeedY
        data.ballPosition[1] += data.ballSpeedY


# This function draws the prompt's background
def drawBackground(canvas, data):
    left = 0
    top = 0
    right = data.width
    bottom = data.height
    canvas.create_rectangle(left, top, right, bottom, fill = "violet")


# This function draws the score of the game
def drawScore(canvas, data):
    canvas.create_text(data.width/15, data.height/15,
                       text = data.score, font = ("Helvetica", 20))


# This function draw the large rectangle
def drawRectangle(canvas, data):
    x0 = data.rx0
    y0 = data.ry0
    x1 = data.rx0 + 1.5 * data.width
    y1 = data.ry0 + 1.5 * data.height
    canvas.create_rectangle(x0, y0, x1, y1, fill="violet", width = 5)


# This is the function that draws the ball
def drawBall(canvas, data):
    canvas.create_oval(data.ballPosition[0], data.ballPosition[1],
                       data.ballPosition[0] + data.ballSize,
                       data.ballPosition[1] + data.ballSize,
                       fill = "Blue")


# This is main drawing function
def redrawAll(canvas, data):
    drawBackground(canvas, data)
    drawRectangle(canvas, data)
    drawScore(canvas, data)
    drawBall(canvas, data)


####################################
# use the run function as-is
####################################

def run(width=300, height=300):
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

run(400, 400)