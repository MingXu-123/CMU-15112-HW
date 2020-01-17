from tkinter import *
import random
class Dot(object):
    def __init__(self, cx, cy):
        self.cx = cx
        self.cy = cy
        self.r = random.randint(5,20)
        self.color = random.choice(["red", "green", "blue"])

    def draw(self, canvas):
        canvas.create_oval(self.cx-self.r, self.cy-self.r,
            self.cx+self.r, self.cy+self.r, fill=self.color)


class MovingDot(Dot):
    def __init__(self, cx, cy):
        super().__init__(cx, cy)
        self.speed = random.randint(3, 15)

    def move(self):
        self.cx += self.speed


def init(data):
    # load data.xyz as appropriate
    data.dots = []
    data.isMoving = False


def mousePressed(event, data):
    # use event.x and event.y
    if data.isMoving:
        data.dots.append(Dot(event.x, event.y))
        data.isMoving = False
    else:
        data.dots.append(MovingDot(event.x, event.y))
        data.isMoving = True

    print(data.dots)


def keyPressed(event, data):
    # use event.char and event.keysym
    pass

def keyPressed(event, data):
    # use event.char and event.keysym
    pass

def timerFired(data):
    for dot in data.dots:
        if isinstance(dot, MovingDot):
            dot.move()

def redrawAll(canvas, data):
    # draw in canvas
    for dot in data.dots:
        dot.draw(canvas)

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

run(400, 200)
