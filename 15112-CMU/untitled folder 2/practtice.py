import os

def readFile(path):
    with open(path, "rt") as f:
        return f.read()

def writeFile(path, contents):
    with open(path, "wt") as f:
        f.write(contents)

def bestNameFileHelper(path, name):
    if os.path.isfile(path):
        contents = readFile(path).lower()
        occurance = contents.count(name)
        return path, occurance
    else:
        current = (path, 0)
        for filename in os.listdir(path):
            newPath = path + os.sep + filename
            temp = bestNameFileHelper(newPath, name)
            if current[1] <= temp[1]:
                current = temp
        return current


def bestNameFile(path, name):
    name = name.lower()
    return bestNameFileHelper(path, name)[0]


class Circle(object):
    numCircles = 0
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r
        Circle.numCircles += 1

    def __eq__(self, other):
        if not isinstance(other, Circle):
            return False
        return self.r == other.r


    def __repr__(self):
        return "Circle at(%d, %d) with radius %s" % (self.x, self.y, self.r)


    def move(self):
        self.y += 10


    def __hash__(self):
        return hash(self.r) # unchange self.r


    def draw(self, canvas):
        canvas.create__oval()


class Bullseye(Circle):
    def __init__(self, x, y, r, numRings):
        super().__init__(x, y, r)
        self.numRings = numRings

    def __eq__(self, other):
        return self.r == other.r and self.numRings == other.Rings

    def __repr__(self):
        return "Bullseye at (%d, %d)"

    def draw(self, canvas):
        radius = self.r
        for i in range(self.numRings):
            canvas.create__rectangle()
            radius -= 2


    #
    # def __hash__(self):
    #     return hash((self.x, self.y))

import random
def init(data):
    data.circles = set()
    data.timer = 0

def keyPressed(event, data):
    newX, newY = (random.randint(0, data.width), random.randint(0, data.height))
    r = random.randint(10, 30)
    circle = Circle(newX, newY, r)
    data.circles.add(circle)

def mousePressed(event , data):
    r = random.randint(15, 30)
    rings = random.randint(2, 5)
    x, y = event.x, event.y
    data.circles.add(Bullseye(x, y, r, rings))

def timerFired(data):
    data.timer += 1
    data.circles = set()
    newCircles = set()
    for circle in data.circles:
        if isinstance(circle, Bullseye):
            newCircles.add(circle)
    data.circles = newCircles
    

def redrawAll(canvas, data):
    for circle in data.circles:
        circle.draw(canvas)
