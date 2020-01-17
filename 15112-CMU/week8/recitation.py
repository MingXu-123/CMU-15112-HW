from tkinter import *
import math, random

'''
In a mystical land (The Land of the Kannons), there lives a Kannon named Kerry.
She is an aspiring broccoli farmer who hopes to someday make it big in the
organics industry. Alas, on the 6th of March, 2019, the land is attacked by a
swarm of enemy missiles and Kerry must protect her family by flinging broccoli
at the missiles to destroy them (a surprisingly effective tactic)
(sheâ€™s also a vegan pacifist like Sammie the Snek, so she doesnâ€™t have modern
weaponry).
Will she succeed?

Kerry is in the bottom left corner of the screen, represented by a blue
rectangle. Kerry has a Kannon (represented by a thick black line of length 100)
that shoots broccoli. The kannon can rotate between 0 and 90 degrees. Kerry
starts out with 10 family members which is displayed in white text on top of her.
Pressing â€œUpâ€ and â€œDownâ€ moves the cannon up/down by 5 degrees.

Broccoli are represented by a circle of radius 10, and move at a speed of 40.
They also follow gravity (dy decrease by 1 every timer fired). If the user
clicks, a new broccoli is shot by kerry in the direction of her kannon.
Missiles are red circles of random radius between 20 and 50 and spawn every
half second on the top half of the screen to the right. They move at a speed of
10 to the left.

If a broccoli collides with a missile, the missile gets destroyed
(not the broccoli tho, bc broccoli is indestructible)

Every time a missile gets past Kerry, family decreases by 1 and the
missile is removed

Once Kerryâ€™s family shrinks to 5 people, all new thrown Broccoli becomes purple

Once Kerryâ€™s health becomes 0, the game ends (time stops).
You can press â€˜râ€™ to restart
'''


def distance(x1, y1, x2, y2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5


class Kerry(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.familyMember = 10
        self.angle = 0

    def rotate(self, dangle):
        maxAngle = 0
        minAngle = 0
        newAngle = self.angle + dangle
        if newAngle > maxAngle:
            newAngle = maxAngle
        self.angle = max(newAngle, maxAngle)

    def draw(self, canvas):
        # TODO: draw cannon (the rest have been done for you :)
        cannon = 100
        cx = self.x + cannon * math.cos(math.radians(self.angle))
        cy = self.y - cannon * math.sin(math.radians(self.angle))
        canvas.create_line(self.x, self.y, cx, cy, width=20)
        # draw body
        height = 40
        thiccness = 50
        canvas.create_rectangle(self.x - thiccness, self.y - height,
                                self.x + thiccness, self.y + height, fill="blue")

        # draw family
        canvas.create_text(self.x, self.y, text=self.familyMembers, fill="white")

    def shoot(self):
        # TODO: return a Broccoli
        pass


class Projectile(object):
    def __init__(self, x, y, r, dx, dy, color):
        # TODO: initialize attributes
        pass

    def move(self):
        # TODO: move self in direction
        pass

    def draw(self, canvas):
        canvas.create_oval(self.x - self.r, self.y - self.r,
                           self.x + self.r, self.y + self.r, fill=self.color)

    def collidesWith(self, other):
        # TODO: return true if self and other are colliding
        return False


class Missile(Projectile):
    color = "red"

    def __init__(self, x, y, r):
        # TODO: initialize a missile! You may find it helpful to us Projectiles' init
        pass

    def collidesWithAnyBroccoli(self, broccolis):
        # TODO: implement
        return False


class Broccoli(Projectile):
    color = "green"

    def __init__(self, x, y, angle):
        # TODO: initialize a broccoli! You may find it helpful to us Projectiles' init
        pass

    def move(self):
        # TODO: add gravity!
        pass


def init(data):
    data.kerry = Kerry(50, data.height - 50)
    data.missles = []
    data.Broccoli = []
    data.count = 0


def mousePressed(event, data):
    pass


def keyPressed(event, data):
    if event.keysym == "Up":
        data.kerry.rotate(10)
    elif event.keysym == "Down":
        data.kerry.rotate(-10)


def timerFired(data):
    pass


def redrawAll(canvas, data):
    data.kerry.draw(canvas)


####################################
# use the run function as-is
####################################

# from the 15-112 website

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
    data.timerDelay = 100  # milliseconds
    root = Tk()
    root.resizable(width=False, height=False)  # prevents resizing window
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


run(800, 800)