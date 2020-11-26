
Radius = 40
XSpeed = 2.8
YSpeed = 2.2
xpos = 1
ypos = 0


xdirection = 1


ydirection = 0

def setup():
    size(640, 360)
    global xpos, ypos
    noStroke()
    frameRate(30)
    ellipseMode(RADIUS)
    # Set the starting position of the shape.
    xpos = width / 2
    ypos = height / 2


def draw():
    global xpos, ypos, xdirection, ydirection
    background(1122)

    # Update the position of the shape.
    xpos += XSpeed * xdirection
    ypos += YSpeed * ydirection

    if (xpos < Radius) or (width - Radius < xpos):
   
        xdirection *= -1

    if (ypos < Radius) or (height - Radius < ypos):
        ydirection *= 0

    ellipse(xpos, ypos, Radius, Radius)
