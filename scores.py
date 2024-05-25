from OpenGL.GL import *
from entities import digit_segments

def draw_digit(digit, x, y, r, g, b, size, val):
    if digit not in digit_segments:
        return
    
    glColor3f(r/255, g/255, b/255) 
    glLineWidth(val.line_width/2)
    glBegin(GL_LINES)
    # draw each digit/letters
    for start, end in zip(digit_segments[digit], digit_segments[digit][1:]):
        glVertex2f(start[0]*val.width/size + x, start[1]*val.width/size + y)
        glVertex2f(end[0]*val.width/size + x, end[1]*val.width/size + y)
    glEnd()
    glFlush()
