from OpenGL.GL import *
from circle_draw import*
from scores import *

class Table:
    # Initiallize table
    def __init__(self, height, width, bg_color_r, bg_color_g, bg_color_b, design_color_r, design_color_g, design_color_b):
        self.height = height
        self.width = width
        self.bg_color_r = bg_color_r
        self.bg_color_g = bg_color_g
        self.bg_color_b = bg_color_b
        self.design_color_r = design_color_r
        self.design_color_g = design_color_g
        self.design_color_b = design_color_b

    def draw_board(self, val):
        # Draw borders for each player sides
        val.player1.draw_player_side_border_colors(1, val) 
        val.player2.draw_player_side_border_colors(-1, val)

        glColor3f(self.design_color_r/255, self.design_color_g/255, self.design_color_b/255) 
        glLineWidth(val.line_width)
        glBegin(GL_LINES)
        # draw center white line
        glVertex2f(0.0, -self.height/2)
        glVertex2f(0.0, self.height/2)  

        # draw goalpost borders
        glVertex2f(self.width/2-val.goalpost_x, val.goalpost_y) 
        glVertex2f(self.width/2-val.goalpost_x, -val.goalpost_y)  
        glVertex2f(self.width/2-val.goalpost_x+1, val.goalpost_y)
        glVertex2f(self.width/2-5, val.goalpost_y)
        glVertex2f(self.width/2-val.goalpost_x+1, -val.goalpost_y)
        glVertex2f(self.width/2-5, -val.goalpost_y)

        glVertex2f(-(self.width/2)+val.goalpost_x, val.goalpost_y) 
        glVertex2f(-(self.width/2)+val.goalpost_x, -val.goalpost_y)  
        glVertex2f(-(self.width/2)+val.goalpost_x+1, val.goalpost_y)
        glVertex2f(-(self.width/2)+5, val.goalpost_y)
        glVertex2f(-(self.width/2)+val.goalpost_x+1, -val.goalpost_y)
        glVertex2f(-(self.width/2)+5, -val.goalpost_y) 
        glEnd()
        glFlush()
        
        self.draw_escape(val)

        glPointSize(val.point_size)
        glBegin(GL_POINTS)
        drawCircle(int(self.height/7.5), 0, 0, 0, self.design_color_r, self.design_color_g, self.design_color_b)
        drawCircle(int(self.height/6), self.width/2, 0, -1, self.design_color_r, self.design_color_g, self.design_color_b)
        drawCircle(int(self.height/6), -self.width/2, 0, 1, self.design_color_r, self.design_color_g, self.design_color_b)
    
    # Draw Exit code on the bottom of the display
    def draw_escape(self,val):
        x = -self.width/10 +5
        y = -self.height/2 + self.height/20
        s = "PRESS ESC TO CLOSE"
        # draw text
        for digit in str(s):
            draw_digit((digit), x, y, 0, 0, 0, val.width/8, val)
            x += self.width/80 # space between characters
