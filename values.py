from entities import *
from ball import Ball
from players import Player
from table import Table

class Values:
    def __init__(self, height, width):
        self.height = height
        self.width = width
        
        self.line_width = (height/150)
        self.point_size = (height/150)

        # A variable to check player
        self.player_1 = 1
        self.player_2 = -1

        # ball
        self.ball_radius = int(height/45)
        self.ball_speed_x = width/60
        self.ball_speed_y = height/70

        # player
        self.player_paddle_radius = int(height/15)
        self.player_paddle_x=width/2 - self.player_paddle_radius * 3
        self.player_paddle_y=0

        # player speed
        self.player_paddle_speed_x = width/90
        self.player_paddle_speed_y = height/80

        # Goalpost
        self.goalpost_x = width/30
        self.goalpost_y = height/10

        self.ball = Ball(
            self.ball_radius, 
            0, 
            0, 
            0,
            0,
            ball_color_r, 
            ball_color_g, 
            ball_color_b
        )

        # Initialize the table
        self.table = Table(
            self.height, 
            self.width, 
            bg_color_r, 
            bg_color_g, 
            bg_color_b, 
            table_design_color_r, 
            table_design_color_g, 
            table_design_color_b
        )

        # Initialize player1
        self.player1 = Player(
            paddle_x = -self.player_paddle_x,
            paddle_y = self.player_paddle_y,
            color_primary = (player1_color1_r, player1_color1_g, player1_color1_b),
            color_secondary = (player1_color2_r, player1_color2_g, player1_color2_b),
            color_tertiary = (player1_color3_r, player1_color3_g, player1_color3_b), 
            score = 0,
            score_x = -self.width/2.75,
            score_y = self.height/2 - self.height/10,
            right_border = 0 - self.line_width,
            left_border = - self.width/2
        )

        # Initialize Player 2
        self.player2 = Player(
            paddle_x = self.player_paddle_x,
            paddle_y = self.player_paddle_y,
            color_primary = (player2_color1_r, player2_color1_g, player2_color1_b),
            color_secondary = (player2_color2_r, player2_color2_g, player2_color2_b),
            color_tertiary = (player2_color3_r, player2_color3_g, player2_color3_b), 
            score = 0,
            score_x = self.width/6.5,  
            score_y = self.height/2 - self.height/10,
            right_border = self.width/2,
            left_border = 0 +self.line_width
        )