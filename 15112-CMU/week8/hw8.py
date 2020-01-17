#################################################################
# Hw8
# Your Name: Ming Xu
# Your Andrew ID:mxu2
# Your Section:2N
#################################################################

import random, math

#################################################
# Hw8 Bird Classes and Subclasses
#################################################

def birdClassCollaborators():
    return "nobody"


# This is the class of bird
class Bird(object):
    # init function in Bird class
    def __init__(self, name):
        self.name = name
        self.eggs = 0

    # str function in Bird class
    def __repr__(self):
        if self.eggs == 1:
            return self.name + " has 1 egg"
        else:
            return self.name + " has " + str(self.eggs) + " eggs"

    # This function compare whether two objects are equal
    def __eq__(self, other):
        return isinstance(other, Bird) and (self.name == other.name)

    # This is the hash function in Bird class
    def __hash__(self):
        return hash(self.name)

    # This is the fly function in Bird class
    def fly(self):
        return "I can fly!"

    # This is the count eggs function in Bird class
    def countEggs(self):
        return self.eggs

    # This is the lay egg function in Bird class
    def layEgg(self):
        self.eggs += 1


# This is the class of Penguin
class Penguin(Bird):
    # This is the fly function in subclass
    def fly(self):
        return "No flying for me."

    # This is the swim function in Penguin class
    def swim(self):
        return "I can swim!"


# This is the class of MessageBird
class MessengerBird(Bird):
    # init function in MessageBird class
    def __init__(self, name, message=""):
        super().__init__(name)
        self.message = message

    # return the information on MessageBird
    def deliverMessage(self):
        return self.message


#################################################
# Hw8 Asteroid Functions
# All graphics must go under here to avoid angering the autograder!
# ignore_rest
#################################################

def asteroidCollaborators():
    return "nobody"

#### OOP Classes ####

## Asteroid and its subclasses, ShrinkingAsteroid and SplittingAsteroid ##

class Asteroid(object):
    # Model
    def __init__(self, cx, cy, r, speed, direction):
        # An asteroid has a position, size, speed, and direction
        self.cx = cx
        self.cy = cy
        self.r = r
        self.speed = speed
        self.direction = direction

    # View
    def draw(self, canvas, color="purple"):
        canvas.create_oval(self.cx - self.r, self.cy - self.r,
                           self.cx + self.r, self.cy + self.r,
                           fill=color)
    
    # Controller
    def moveAsteroid(self):
        self.cx += self.speed * self.direction[0]
        self.cy += self.speed * self.direction[1]

    # this function is to check whether asteroids collide with wall
    def collidesWithWall(self, width, height):
        # Check if the asteroid hits the wall or overlaps it at all
        return self.cx - self.r <= 0 or self.cx + self.r >= width or \
            self.cy - self.r <= 0 or self.cy + self.r >= height

    # this function the reaction of asteroids collide with wall
    def reactToWallHit(self, screenWidth, screenHeight):
        if self.cx + self.r >= screenWidth:
            self.cx = self.r
        elif self.cx - self.r <= 0:
            self.cx = screenWidth - self.r
        elif self.cy - self.r <= 0:
            self.cy = screenHeight - self.r
        elif self.cy + self.r >= screenHeight:
            self.cy = self.r


class ShrinkingAsteroid(Asteroid):
    # Model
    def __init__(self, cx, cy, r, speed, direction):
        # Shrinking Asteroids also track how fast they shrink
        super().__init__(cx, cy, r, speed, direction)
        self.shrinkAmount = 5
    
    # View
    def draw(self, canvas):
        super().draw(canvas, color="pink")
    
    # Controller
    def reactToWallHit(self, screenWidth, screenHeight):
        # this function the reaction of asteroids collide with wall
        if self.cx + self.r >= screenWidth or\
                self.cx - self.r <= 0:
            self.direction[0] = - self.direction[0]
            self.direction[1] = - self.direction[1]
        if self.cy - self.r <= 0 or\
                self.cy + self.r >= screenHeight:
            self.direction[0] = - self.direction[0]
            self.direction[1] = - self.direction[1]

    # this function shrinks the radius of asteroids
    def AfterCollidesWithBullet(self):
        self.r = self.r - self.shrinkAmount


## Rocket class ##

class Rocket(object):
    # Model
    def __init__(self, cx, cy):
        # A rocket has a position and a current angle it faces
        self.cx = cx
        self.cy = cy
        self.angle = 90

    # View
    def draw(self, canvas):
        # Draws a cool-looking triangle-ish shape
        size = 30
        angle = math.radians(self.angle)
        angleChange = 2*math.pi/3
        numPoints = 3
        points = []
        for point in range(numPoints):
            points.append((self.cx + size*math.cos(angle + point*angleChange),
                           self.cy - size*math.sin(angle + point*angleChange)))
        points.insert(numPoints-1, (self.cx, self.cy))
        canvas.create_polygon(points, fill="green2")

    # Controller
    def rotate(self, numDegrees):
        self.angle += numDegrees

    # this is make bullet function
    def makeBullet(self):
        # Generates a bullet heading in the direction the ship is facing
        offset = 35
        x = self.cx + offset*math.cos(math.radians(self.angle)) 
        y = self.cy - offset*math.sin(math.radians(self.angle))
        speedLow, speedHigh = 20, 40
        return Bullet(x, y, self.angle, random.randint(speedLow, speedHigh))

## Bullet Class ##

class Bullet(object):
    # Model
    def __init__(self, cx, cy, angle, speed):
        # A bullet has a position, a size, a direction, and a speed
        self.cx = cx
        self.cy = cy
        self.r = 5
        self.angle = angle
        self.speed = speed
    
    # View
    def draw(self, canvas):
        canvas.create_oval(self.cx - self.r, self.cy - self.r, 
                           self.cx + self.r, self.cy + self.r,
                           fill="white", outline=None)

    # Controller
    def moveBullet(self):
        # Move according to the original trajectory
        self.cx += math.cos(math.radians(self.angle))*self.speed
        self.cy -= math.sin(math.radians(self.angle))*self.speed

    # this is the function that bullets collides asteroids
    def collidesWithAsteroid(self, other):
        # Check if the bullet and asteroid overlap at all
        if(not isinstance(other, Asteroid)): # Other must be an Asteroid
            return False
        else:
            dist = ((other.cx - self.cx)**2 + (other.cy - self.cy)**2)**0.5
            return dist < self.r + other.r

    # this function is to check whether bullets are off screen
    def isOffscreen(self, width, height):
        # Check if the bullet has moved fully offscreen
        return (self.cx + self.r <= 0 or self.cx - self.r >= width) or \
               (self.cy + self.r <= 0 or self.cy - self.r >= height)

#### Graphics Functions ####

from tkinter import *

# this is the model init function
def init(data):
    data.rocket = Rocket(data.width//2, data.height//2)
    data.score = 0
    data.counter = 0
    data.bullets = []
    data.asteroids = []


# this is the mouse event handler
def mousePressed(event, data):
    pass


# this is the keyboard handler
def keyPressed(event, data):
    if event.keysym == "Right":
        data.rocket.rotate(-5)
    elif event.keysym == "Left":
        data.rocket.rotate(5)
    elif event.keysym == "space":
        data.bullets += [data.rocket.makeBullet()]
    elif event.char == "r":
        init(data)


# get random element of asteroid
def getRandomElement(data):
    r = random.randint(15, 30)
    cx = random.randint(r, data.width - r)
    cy = random.randint(r, data.height - r)
    speed = random.randint(5, 10)
    direction = random.choice([[1, 0], [-1, 0], [0, 1], [0, -1]])
    return cx, cy, r, speed, direction


# this function generate normal asteroid
def getAsteroidNormal(randomElement):
    return Asteroid(randomElement[0], randomElement[1],
                                   randomElement[2], randomElement[3],
                                   randomElement[4])


# this function generate shrink asteroid
def getAsteroidShrink(randomElement):
    return ShrinkingAsteroid(randomElement[0], randomElement[1],
                                   randomElement[2], randomElement[3],
                                   randomElement[4])


# this is the time handler
def timerFired(data):
    data.counter += data.timerDelay
    for bullet in data.bullets:
        bullet.moveBullet()
        if bullet.isOffscreen(data.width, data.height):
            data.bullets.remove(bullet)
        for asteroid in data.asteroids:
            if bullet.collidesWithAsteroid(asteroid):
                data.bullets.remove(bullet)
                if type(asteroid) == Asteroid:
                    data.asteroids.remove(asteroid)
                    data.score += 1
                elif type(asteroid) == ShrinkingAsteroid:
                    if asteroid.r <= 15:
                        data.asteroids.remove(asteroid)
                        data.score += 1
                    else:
                        asteroid.AfterCollidesWithBullet()
    if data.counter % 2000 == 0:
        randomElement = getRandomElement(data)
        asteroidNormal = getAsteroidNormal(randomElement)
        asteroidShrink = getAsteroidShrink(randomElement)
        data.asteroids += [random.choice([asteroidNormal, asteroidShrink])]
    for asteroid in data.asteroids:
        asteroid.moveAsteroid()
        if asteroid.collidesWithWall(data.width, data.height):
            asteroid.reactToWallHit(data.width, data.height)


# this is the main draw function
def redrawAll(canvas, data):
    canvas.create_rectangle(0, 0, data.width, data.height, fill="gray3")
    data.rocket.draw(canvas)
    for bullet in data.bullets:
        bullet.draw(canvas)
    for asteroid in data.asteroids:
        asteroid.draw(canvas)
    canvas.create_text(data.width/2, data.height, anchor="s", fill="yellow",
                       font="Arial 24 bold", text="Score: " + str(data.score))

#################################################################
# use the run function as-is
#################################################################

def runAsteroids(width=300, height=300):
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



#################################################
# Hw8 Test Functions
#################################################

def getLocalMethods(clss):
    import types
    # This is a helper function for the test function below.
    # It returns a sorted list of the names of the methods
    # defined in a class. It's okay if you don't fully understand it!
    result = [ ]
    for var in clss.__dict__:
        val = clss.__dict__[var]
        if (isinstance(val, types.FunctionType)):
            result.append(var)
    return sorted(result)

def testBirdClasses():
    print("Testing Bird classes...", end="")
    # A basic Bird has a species name, can fly, and can lay eggs
    bird1 = Bird("Parrot")
    assert(type(bird1) == Bird)
    assert(isinstance(bird1, Bird))
    assert(bird1.fly() == "I can fly!")
    assert(bird1.countEggs() == 0)
    assert(str(bird1) == "Parrot has 0 eggs")
    bird1.layEgg()
    assert(bird1.countEggs() == 1)
    assert(str(bird1) == "Parrot has 1 egg")
    bird1.layEgg()
    assert(bird1.countEggs() == 2)
    assert(str(bird1) == "Parrot has 2 eggs")
    tempBird = Bird("Parrot")
    assert(bird1 == tempBird)
    tempBird = Bird("Wren")
    assert(bird1 != tempBird)
    nest = set()
    assert(bird1 not in nest)
    assert(tempBird not in nest)
    nest.add(bird1)
    assert(bird1 in nest)
    assert(tempBird not in nest)
    nest.remove(bird1)
    assert(bird1 not in nest)
    assert(getLocalMethods(Bird) == ['__eq__','__hash__','__init__', 
                                     '__repr__', 'countEggs', 
                                     'fly', 'layEgg'])
    
    # A Penguin is a Bird that cannot fly, but can swim
    bird2 = Penguin("Emperor Penguin")
    assert(type(bird2) == Penguin)
    assert(isinstance(bird2, Penguin))
    assert(isinstance(bird2, Bird))
    assert(not isinstance(bird1, Penguin))
    assert(bird2.fly() == "No flying for me.")
    assert(bird2.swim() == "I can swim!")
    bird2.layEgg()
    assert(bird2.countEggs() == 1)
    assert(str(bird2) == "Emperor Penguin has 1 egg")
    assert(getLocalMethods(Penguin) == ['fly', 'swim'])
    
    # A MessengerBird is a Bird that can optionally carry a message
    bird3 = MessengerBird("War Pigeon", message="Top-Secret Message!")
    assert(type(bird3) == MessengerBird)
    assert(isinstance(bird3, MessengerBird))
    assert(isinstance(bird3, Bird))
    assert(not isinstance(bird3, Penguin))
    assert(not isinstance(bird2, MessengerBird))
    assert(not isinstance(bird1, MessengerBird))
    assert(bird3.deliverMessage() == "Top-Secret Message!")
    assert(str(bird3) == "War Pigeon has 0 eggs")
    assert(bird3.fly() == "I can fly!")

    bird4 = MessengerBird("Homing Pigeon")
    assert(bird4.deliverMessage() == "")
    bird4.layEgg()
    assert(bird4.countEggs() == 1)
    assert(getLocalMethods(MessengerBird) == ['__init__', 'deliverMessage'])
    print("Done!")




#################################################
# Hw4 Main
#################################################

def testAll():
    testBirdClasses()
    # runAsteroids(600, 600)


def main():
    testAll()

if __name__ == '__main__':
    main()

