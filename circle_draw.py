from OpenGL.GL import *

def setPixel(x, y, r, g, b):
    glColor3ub(r, g, b)
    glVertex2i(int(x), int(y))

def draw8way(xc, yc, x, y, if_full, r, g, b):
    if(if_full==0):
        setPixel(xc+x, yc+y, r,g,b) #R2
        setPixel(xc+y, yc+x, r,g,b) #R1

        setPixel(xc-y, yc+x, r,g,b) #R3
        setPixel(xc-x, yc+y, r,g,b) #R4

        setPixel(xc-x, yc-y, r,g,b) #R6
        setPixel(xc-y, yc-x, r,g,b) #R5

        setPixel(xc+y, yc-x, r,g,b) #R7
        setPixel(xc+x, yc-y, r,g,b) #R8
    if(if_full==1):
        setPixel(xc+x, yc+y, r,g,b) #R2
        setPixel(xc+y, yc+x, r,g,b) #R1
        
        setPixel(xc+y, yc-x, r,g,b) #R7
        setPixel(xc+x, yc-y, r,g,b) #R8
    if(if_full==-1):
        setPixel(xc-y, yc+x, r,g,b) #R3
        setPixel(xc-x, yc+y, r,g,b) #R4

        setPixel(xc-x, yc-y, r,g,b) #R6
        setPixel(xc-y, yc-x, r,g,b) #R5

def drawCircle(rad, xc, yc, if_full, r, g, b):
    x = rad
    y = 0
    d = rad + 5/4
    draw8way(xc, yc, x, y, if_full, r, g, b)

    while abs(y) < abs(x):
        if d < 0:
            d += 2*y + 3
        else:
            d += 2*y - 2*x + 5
            x = x - 1
        y = y + 1
        draw8way(xc, yc, x, y, if_full, r, g, b)
