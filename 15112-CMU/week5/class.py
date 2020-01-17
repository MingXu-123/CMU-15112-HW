# oopyDotsDemo.py
# starts with betterDotsDemo and adds:
#   * a dotCounter that counts all the instances of Dot or its subclasses
#   * a MovingDot subclass of Dot that scrolls horizontally
#   * a FlashingMovingDot subclass of MovingDot that flashes and moves

import random
from tkinter import *

class Dot(object):
    dotCount = 0

    # Model
    def __init__(self, x, y):
        Dot.dotCount += 1
        self.x = x
        self.y = y
        self.r = random.randint(20,50)
        self.fill = random.choice(["pink","orange","yellow","green",
                                   "cyan","purple"])
        self.clickCount = 0

    # View
    def draw(self, canvas):
        canvas.create_oval(self.x-self.r, self.y-self.r,
                           self.x+self.r, self.y+self.r,
                           fill=self.fill)
        canvas.create_text(self.x, self.y, text=str(self.clickCount))

    # Controller
    def containsPoint(self, x, y):
        d = ((self.x - x)**2 + (self.y - y)**2)**0.5
        return (d <= self.r)

class MovingDot(Dot):
    # Model
    def __init__(self, x, y):
        super().__init__(x, y)
        self.speed = 5 # default initial speed

    # Controller
    def move(self, data):
        self.x += self.speed
        if (self.x > data.width):
            self.x = 0

class FlashingMovingDot(MovingDot):
    # Model
    def __init__(self, x, y):
        super().__init__(x, y)
        self.flashCounter = 0
        self.showFlash = True

    # View
    def draw(self, canvas):
        if (self.showFlash):
            canvas.create_rectangle(self.x-self.r, self.y-self.r,
                               self.x+self.r, self.y+self.r,
                               fill="black")
        super().draw(canvas)

    # Controller
    def move(self, data):
        super().move(data)
        self.flashCounter += 1
        if (self.flashCounter == 5):
            self.flashCounter = 0
            self.showFlash = not self.showFlash

# Core animation code

def init(data):
    data.dots = [ ]

def mousePressed(event, data):
    for dot in reversed(data.dots):
        if (dot.containsPoint(event.x, event.y)):
            dot.clickCount += 1
            return
    dotType = (len(data.dots) % 3)
    if (dotType == 0):
        data.dots.append(Dot(event.x, event.y))
    elif (dotType == 1):
        data.dots.append(MovingDot(event.x, event.y))
    else:
        data.dots.append(FlashingMovingDot(event.x, event.y))

def redrawAll(canvas, data):
    for dot in data.dots:
        dot.draw(canvas)
    canvas.create_text(data.width/2, 10, text="%d Dots" % Dot.dotCount)

def keyPressed(event, data):
    pass

def timerFired(data):
    for dot in data.dots:
        if type(dot) != Dot:
            dot.move(data)

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
    init(data)
    # create the root and the canvas
    root = Tk()
    root.resizable(width=False, height=False) # prevents resizing window
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

run(600, 400)