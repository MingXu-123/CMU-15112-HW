## flappyKim: A basic flappybird-type game
# Code from CMU 15-112 Lecture 2, 03/07/2019, 11/09/2018
# mdtaylor

##Press space to make Kimchee swim!
# This is a very simple OOPy implementation so...
# ...if you want some OOPy animation practice, add some features!
#       1. Add a score count
#       2. Add treats for Kimchee to eat  :)
#       3. Stop the game if Kimchee hits too many obstacles
#       4. Add some difficulty levels
#       5. Add a start/splash screen
#       6. Add a pause screen
#       7. Improve the graphics and/or draw a background
#       8. Smooth out the motion and/or delete offscreen obstacles
#       9. Make the up/down motion velocity-based like the real game

## Note: Lec1 took a sidescrolling approach, while this code moves the pipes!
# You can approach this problem many different ways!  No one solution is 
#      correct, so it's a matter of organization and preference.
# What are the pros and cons of moving the pipes (this code), 
#      versus Kimchee moving forward with the view while the pipes stay still?

from tkinter import *
import random

####################################
# Define classes
####################################

##Define Kimchee, Prof. Taylor's axolotl
class Kimchee(object):
    #Establish Kimchee's initial position and radius
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.r = 40
        
    #Draw Kimchee as an oval with a face made of text
    def draw(self, canvas):
        canvas.create_oval(self.x-self.r, self.y-self.r, self.x+self.r, self.y+self.r, fill="grey")
        canvas.create_text(self.x, self.y,text=">>o u o<<",font="arial 30 bold")
        
    #Move Kimchee up and down by vSpeed pixels
    def move(self, vSpeed):
        self.y-=vSpeed  #Positive vSpeed moves him up
        
    #Return True if Kimchee collides with the input obstacle
    def collidesWithObs(self, other):
        if (other.hPos<=self.x<=other.hPos+other.width and
                (other.top<=self.y+self.r<=other.bottom or 
                 other.top<=self.y-self.r<=other.bottom)):
            return True



##Define the obstacle class, a series of moving boxes to avoid
class Obstacle(object):
    #Establish the obstacle's dimensions and location
    def __init__(self,top, bottom, hPos, width):
        self.top=top
        self.bottom=bottom
        self.width=width
        self.hPos=hPos  #This is the left edge of the obstacle
        self.color="green"

    #Move the obstacle to the left by hSpeed pixels
    def move(self, hSpeed):
        self.hPos-=hSpeed
    
    #Draw the obstacle as a rectangle
    def draw(self, canvas):
        canvas.create_rectangle(self.hPos, self.top, self.hPos+self.width, self.bottom, fill=self.color)
    
    
    
####################################
# customize these functions
####################################    

##Set up our animation
def init(data):
    data.timerDelay = 100 # Tweak this to change game speed
    data.kc=Kimchee(data.width/4, data.height/2)  #Make our Kimchee object
    data.tCount=0        #Start our timer at 0
    data.obstacles=[]    #We'll store obstacles as an empty list



##Can you do something cool with mousePressed?
def mousePressed(event, data):
    pass



##Move Kimchee up when any key is pressed.
#How might you make the motion smoother / less jerky?
def keyPressed(event, data):
    upSpeed=30
    data.kc.move(upSpeed)



##Lower Kimchee, move obstacles left, and check for collisions
def timerFired(data):
    data.tCount+=1
    
    #Move Kimchee down
    downSpeed=-10
    data.kc.move(downSpeed)
    
    #Make a new obstacle pair at a set interval
    obsInterval=20
    gapSize=6
    if data.tCount%obsInterval==0:
        randHeight=random.randint(0,data.height//2)
        gap=gapSize*data.kc.r
        
        #Our obstacles are added to the obstacle list
        data.obstacles+=[Obstacle(0, randHeight, data.width, 50)]
        data.obstacles+=[Obstacle(randHeight+gap,data.height, data.width, 50)]
        #Note: We aren't deleting them once they leave the screen.
        #This might slow down the game after a long time (but you can fix it!)
        
    #Move every obstacle in our list and then check for Kimchee collisions
    obsSpeed=20
    for obs in data.obstacles:
        obs.move(obsSpeed)
        if data.kc.collidesWithObs(obs):
            print("Oop!")
            obs.color="red"  #Change hit obstacles red. What else could we do?



##Call methods to draw Kimchee and all the obstacles in our list
def redrawAll(canvas, data):
    data.kc.draw(canvas)
    
    for obs in data.obstacles:
        obs.draw(canvas)



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
    data.timerDelay = 50 # milliseconds
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

run(600, 600)