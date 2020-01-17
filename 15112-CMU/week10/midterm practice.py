def palindromepartition(s):
    sol = []
    return helper(s, sol)


def nonTrivialSol(sol):
    for item in sol:
        if len(item) > 1:
            return True
    return False


def helper(s, sol):
    if len(s) == 0 and nonTrivialSol(sol):
        return sol
    else:
        for i in range(len(s), 0, -1):
            currSubStr = s[0:i]
            if currSubStr == currSubStr[::-1]:
                sol.append(currSubStr)
                temp = helper(s[i:], sol)
                if temp != None:
                    return temp
                sol.pop() # undo the move sol.append
    return None



def visualizeRecursion(f):
    depth = 0
    def g(*args, **kwargs):
        nonlocal depth
        # global depth
        depth += 1
        res = f(*args, **kwargs)
        depth -= 1
        s = "\t" * depth + "recursion depth: " \
            + str(depth) + ', result: ' + str(res)
        print(s)
        return res
    return g


@visualizeRecursion
def fact(n):
    if n == 0: return 1
    return n * fact(n-1)
fact(4)


def findTriplets(arr):
    result = set()
    n = len(arr)
    for i in range(n-1):
        s = set()
        for j in range(i+1, n):
            x = - (arr[i] + arr[j]) # represent the
            # third num you're looking for
            if x in s: # if x has been "seen" before
                result.add((x, arr[i], arr[j]))
            else:
                s.add(arr[j])
    return result

print(findTriplets([1,0,-3,2,-1]))

from tkinter import *

class Circle(object):
    def __init__(self, **kwargs):
        self.x = kwargs['x']
        self.y = kwargs['y']
        self.radius = kwargs['r']
        self.color = kwargs['c']

    def __eq__(self, other):
        return isinstance(other, Circle) and self.color == other.color \
               and self.radius == other.radius

    def __repr__(self):
        return "%s circles of radius %d, at position (%d,%d)" % \
               (self.color, self.radius, self.x, self.y)

    def __hash__(self):
        return hash((self.radius, self.color))

    def draw(self, canvas):
        canvas.create_oval(.....)
        pass


class MC(Circle):
    def __init__(self, Vx, Vy, **kwargs):
        self.velocityX = Vx
        self.velocityY = Vy
        super().__init__(**kwargs)

    def move(self):
        self.x += self.velocityX
        self.y += self.velocityY

def init(data):
    data.circles = []


def timerFired(data):
    import random
    data.time += 1
    x = random.randInt(0, data.width)
    y = random.randInt(5, data.height)
    r = random.randInt(5, 40)
    c = random.Choice(["red","blue","green"])
    C = Circle(x= x, y= y, r=r,c=c)
    if (data.time % 100 == 0):
        data.add(createCircle(data))

    if (data.time % 500 == 0):
        createMovingCircle()

    for c in data.circles:
        if type((c) == MC):





def mousePressed(event, data): pass

def timerFired(data): pass



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