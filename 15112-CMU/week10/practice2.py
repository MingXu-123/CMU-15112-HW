from tkinter import *

class Circle(object):
    def __init__(self, **kwargs):
        self.x = kwargs["x"]
        self.y = kwargs["y"]
        self.r = kwargs["r"]
        self.color = kwargs["c"]

    def hash(self):
        return hash((self.r, self.color))

    def __eq__(self, other):
        return isinstance(other, Circle) and \
               self.r == other.r

    def __repr__(self):
        return "%s circle of radius %d, at position(%d, %d)"\
               % (self.color, self.r, self.x, self.y)

    def draw(self, canvas):
        canvas.create_oval(self.x - self.r, self.y - self.r,
                           self.x + self.r, self.y + self.r, fill = self.color)


class MC(Circle):
    def __init__(self, *args, **kwargs):
        super.__init__(**kwargs)
        self.velocityX = args[0]
        self.velocityY = args[1]

    def move(self):
        self.x += self.velocityX
        self.y += self.velocityY


####################################
# customize these functions
####################################
def generateCircle(data):
    import random
    x = random.randint(0, data.width)
    y = random.randint(0, data.height)
    r = random.randint(5, 40)
    color = random.choice(["red","green","blue"])
    c = Circle(x = x, y =y, r =r, c = color)
    if c not in data.circles:
        return c

def movingCircle(data):
    import random
    x = random.randint(0, data.width)
    y = random.randint(0, data.height)
    r = random.randint(5, 40)
    color = random.choice(["red", "green", "blue"])
    vx = random.randint(5, 10)
    vy = random.randint(5, 10)
    c = MC(vx, vy, x=x, y=y, r=r, c=color)
    if c not in data.circles:
        return c

def init(data):
    data.circles = set()
    data.timer = 0


def mousePressed(event, data):
    # use event.x and event.y
    pass

def keyPressed(event, data):
    # use event.char and event.keysym
    pass

def timerFired(data):
    data.timer += data.timerDelay
    if data.timer % 1000 == 0:
        data.circles.add(generateCircle(data))
    if data.timer % 5000 == 0:
        data.circles.add(movingCircle(data))


def redrawAll(canvas, data):
    # draw in canvas
    pass

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




