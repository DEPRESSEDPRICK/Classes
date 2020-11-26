speed=8
x=700
y=700
x1=x/2
y1=y/2
def setup():
    size(700,700) 
    background(0)
def keyReleased():
    global x,y,x1,y1
    if key == ' ':
       x1 = random (0,width)
       y1 = random (0,height)
       background(0)
       ellipse(x1,y1,100,100)
       fill(5555,0,0)
       stroke (1000,3600,5555)
       fill(random(0,555),random(0,555),random(0,555))
def keyPressed():
    global x1,y1,x,y
    if key == 'w':
        y1 = y1-speed
    if key == 's':
        y1 = y1+speed
    if key == 'a':
        x1 = x1-speed
    if key == 'd':
        x1 = x1+speed
def draw():
    q=0
    background(1111)
    ellipse(x1,y1,70,70)
