# Side Scrolling Demo
from tkinter import *
def init(data):
    data.mapWidth = data.width * 3
    data.bushes = []
    data.bushSize = 50
    for bushX in range(0, data.mapWidth, data.bushSize):
        data.bushes.append([bushX, "green"])
    data.playerX = 40
    data.playerSize = 30

    data.scrollX = 0
    data.groundY = data.height*2/3

def mousePressed(event, data):
    # In mousePressed, we need to move the mouse from the VIEW to the MAP
    # We do this by adding the scroll position to the position clicked

    viewX = event.x
    x = data.scrollX + viewX
    y = event.y
    # Now check if there's a bush in there
    for bush in data.bushes:
        if bush[0] <= x <= (bush[0] + data.bushSize) and \
           (data.groundY - data.bushSize/2) <= y <= data.groundY:
            bush[1] = "purple"

def keyPressed(event, data):
    # We often choose to move the screen based on player input
    # In this example, we'll move when the player reaches a buffer
    # on either side of the screen.
    # We calculate this buffer based on the MAP and the SCROLL POSITION

    playerSpeed = 10
    if event.keysym == "Left":
        data.playerX -= playerSpeed
    elif event.keysym == "Right":
        data.playerX += playerSpeed

    # Move the window if the player is about to move off the screen
    buffer = 10
    # Need to compare player's map position to the
    # scroll position plus the screen size
    if (data.playerX + data.playerSize + buffer) >= (data.scrollX + data.width):
        data.scrollX += playerSpeed
    elif (data.playerX - buffer) <= data.scrollX:
        data.scrollX -= playerSpeed

def timerFired(data):
    pass

def redrawAll(canvas, data):
    # When drawing things, we need to move them from the MAP to the VIEW
    # We do this by subtracting the scroll position from the map position

    # draw the bushes
    for bush in data.bushes:
        [bushX, color] = bush
        # We'll draw some things offscreen, but that's okay!
        canvas.create_oval(bushX - data.scrollX,
                           data.groundY - data.bushSize/2,
                           bushX + data.bushSize - data.scrollX,
                           data.groundY + data.bushSize/2,
                           fill=color)
    # draw the ground
    canvas.create_rectangle(0 - data.scrollX,
                            data.groundY,
                            data.mapWidth - data.scrollX,
                            data.height,
                            fill="tan4")
    # draw the player
    canvas.create_oval(data.playerX - data.scrollX,
                       data.groundY - data.playerSize,
                       data.playerX + data.playerSize - data.scrollX,
                       data.groundY,
                       fill="red")
    canvas.create_text(10, 10, text="scrollX: " + str(data.scrollX),
                       font="Arial 25 bold", anchor="nw")




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

    # Set up data and call init
    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
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
    redrawAllWrapper(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed
    print("bye!")

run(400, 200)