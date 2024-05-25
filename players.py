from circle_draw import*
from scores import *

# Left one on the screen is player 1, and the other one is player 2

class Player:
    # Initialize player
    def __init__(self, paddle_x, paddle_y, color_primary, color_secondary, color_tertiary, score, score_x, score_y, right_border, left_border):
        # Coordinates of the players paddle
        self.paddle_x = paddle_x 
        self.paddle_y = paddle_y

        # 3 Colors of the players paddle
        self.color_primary = color_primary
        self.color_secondary = color_secondary
        self.color_tertiary = color_tertiary

        # Score of the player
        self.score = score

        # Coordinates of the score position on the screen
        self.score_x = score_x
        self.score_y = score_y

        # Right and left border are the horizontal ending points of the paddle. 
        # The paddles cannot go further beyond these boundaries.
        self.right_border = right_border
        self.left_border = left_border

    # Up movement
    def move_up(self, val):
        if(self.paddle_y + val.player_paddle_radius + val.line_width < val.height/2) and not val.ball.check_collision(self.paddle_x, self.paddle_y, val.player_paddle_radius):
            self.paddle_y += val.player_paddle_speed_y

    # down movement
    def move_down(self, val):
        if(self.paddle_y - val.player_paddle_radius - val.line_width > -val.height/2) and not val.ball.check_collision(self.paddle_x, self.paddle_y, val.player_paddle_radius):
            self.paddle_y -= val.player_paddle_speed_y

    # left movement
    def move_left(self, val):
        if(self.paddle_x - val.player_paddle_radius - val.line_width > self.left_border) and not val.ball.check_collision(self.paddle_x, self.paddle_y, val.player_paddle_radius):
            self.paddle_x -= val.player_paddle_speed_x

    # right movement
    def move_right(self, val):
        if(self.paddle_x + val.player_paddle_radius + val.line_width < self.right_border) and not val.ball.check_collision(self.paddle_x, self.paddle_y, val.player_paddle_radius):
            self.paddle_x += val.player_paddle_speed_x
    
    # Draw paddle (Filled Circle with 3 colors)
    def draw_paddle(self, val):
        for i in range(int(val.player_paddle_radius-val.point_size)):
            if(i%25<8):
                drawCircle(i, self.paddle_x, self.paddle_y, 0, self.color_tertiary[0], self.color_tertiary[1], self.color_tertiary[2])
            elif(i%25<15):
                drawCircle(i, self.paddle_x, self.paddle_y, 0, self.color_secondary[0], self.color_secondary[1], self.color_secondary[2])
            else:
                drawCircle(i, self.paddle_x, self.paddle_y, 0, self.color_primary[0], self.color_primary[1], self.color_primary[2])
        drawCircle(i, self.paddle_x, self.paddle_y, 0, 17, 5, 53) # Border of the paddle

    # Each player will have 3 borders of the same color of their paddle on their sides of table
    def draw_player_side_border_colors(self, value, val):
        glColor3f(self.color_primary[0]/255, self.color_primary[1]/255, self.color_primary[2]/255) 
        glLineWidth(val.line_width)
        glBegin(GL_LINES)

        # Top border
        glVertex2f(value * -val.width/2, val.height/2 - val.line_width/2) 
        glVertex2f(0.0, val.height/2-val.line_width/2)  

        # Side border
        glVertex2f(value * -val.width/2 + value * val.line_width/2, val.height/2) 
        glVertex2f(value * -val.width/2 + value * val.line_width/2, -val.height/2)  
        
        # bottom border
        glVertex2f(value * -val.width/2, -val.height/2 + val.line_width/2) 
        glVertex2f(0.0, -val.height/2 + val.line_width/2)  

        # Colorful Goalpost for players      
        x = value* (-val.width/2 + val.goalpost_x)
        x_end = value*(-val.width/2 + val.line_width)

        while (value < 0 and x < x_end) or (value > 0 and x > x_end):
            glVertex2f(x, val.goalpost_y)
            glVertex2f(x, -val.goalpost_y)
            x -= value
        glEnd()
        glFlush()

    # Draw score on display
    def draw_score(self, flag, val):
        x = self.score_x
        if flag==1 : s = 'TEAM X-'
        else: s = 'TEAM Y-'
        # draw team name
        for digit in str(s):
            draw_digit((digit), x, self.score_y, self.color_primary[0], self.color_primary[1], self.color_primary[2], val.width/20, val)
            x += val.width/30 # space between characters
            
        # draw score
        for digit in str(self.score):
            draw_digit(int(digit), x, self.score_y, self.color_primary[0], self.color_primary[1], self.color_primary[2], val.width/20, val)
            x += val.width/50 # space between characters

    # Reset Player Paddle
    def reset_paddle(self, flag, val):
        self.paddle_x = flag*val.player_paddle_x
        self.paddle_y = val.player_paddle_y