from circle_draw import *
import math

class Ball:
    # Initiallize the ball
    def __init__(self, radius, initial_x, initial_y, speed_x, speed_y, color_r, color_g, color_b):
        self.radius = radius
        # Coordinates of the ball
        self.x = initial_x
        self.y = initial_y

        # Speed of the ball
        self.speed_x = speed_x
        self.speed_y = speed_y

        # Ball color (r,g,b)
        self.color_r = color_r
        self.color_g = color_g
        self.color_b = color_b


    # Draw_ball(Filled Circle)
    def draw_ball(self):
        for i in range(self.radius):
            drawCircle(i, self.x, self.y, 0, self.color_r, self.color_g, self.color_b)

    # Ball Move
    def update_position(self):
        self.x += self.speed_x
        self.y += self.speed_y

    # Change direction when collides with the border
    def border_collision(self, val):
        # Collides with vertical border
        if (self.y + self.radius) > (val.height / 2 - 5) or (self.y - self.radius) < (-val.height / 2 + 5):
            self.speed_y *= -1
        # Collides with horizontal border
        if (self.x + self.radius) > (val.width / 2 - 5) or (self.x - self.radius) < (-val.width / 2 + 5):
            self.speed_x *= -1

    # Reset Ball Position after goal
    def goal(self,playerx, val):
        # Check if ball_y is inside the goal post area Y
        if (self.y) > (-val.goalpost_y) and (self.y) < (val.goalpost_y):
            # Check if all_x is inside the goal post area X of player 2
            if playerx > 0 and self.x + self.radius > val.width/2-val.goalpost_x:
                # Reset the ball position to (0,0)
                self.x = 0
                self.y = 0
                # Reset ball speed to 0
                self.speed_x = 0
                self.speed_y = 0                
                return True
            
            # Check if all_x is inside the goal post area X of player 1
            if playerx < 0 and self.x - self.radius < -val.width/2+val.goalpost_x:
                # Reset the ball position to (0,0)
                self.x = 0
                self.y = 0
                # Reset ball speed to 0
                self.speed_x = 0
                self.speed_y = 0
                return True
        # Not a goal
        return False

    # Change direction after collision with player occurs
    def collision_with_player(self, player, val):
        # Check if collides with the player paddle
        if self.check_collision(player.paddle_x, player.paddle_y, val.player_paddle_radius):
            dx = self.x - player.paddle_x
            dy = self.y - player.paddle_y

            if self.x == 0: # To avoid division by 0
                self.x = 0.1

            theta = math.atan(self.y/self.x) # angle of velocity of the ball

            if abs(dx) > abs(dy): # Collision primarily in the x-direction
                # if ball is in the left of the player
                if self.x < player.paddle_x: 
                    self.speed_x = -abs(val.ball_speed_x) # Go left
                else: # if ball is in the right of the player
                    self.speed_x = abs(val.ball_speed_x) # go right
            elif abs(dx) < abs(dy): # Collision primarily in the y-direction
                # if ball is below the player
                if self.y < player.paddle_y: 
                    self.speed_y = -abs(val.ball_speed_y) # move down
                else: # if ball is above the player
                    self.speed_y = abs(val.ball_speed_y) # move up
            else: # Collision primarily in a diagonal
                # if ball is in the left of the player
                if self.x < player.paddle_x:
                    self.speed_x = -abs(val.ball_speed_x) # Go left
                else: # if ball is in the right of the player
                    self.speed_x = abs(val.ball_speed_x) # go right
                # if ball is below the player
                if self.y < player.paddle_y:
                    self.speed_y = -abs(val.ball_speed_y) # move down
                else: # if ball is above the player
                    self.speed_y = abs(val.ball_speed_y) # move up
            return True # collision occured
        return False # no collision

    # Check if collision occurs with another object
    def check_collision(self, object_x, object_y, object_radius):
        distance = ((self.x - object_x) ** 2 + (self.y - object_y) ** 2) ** 0.5
        return distance < (self.radius + object_radius)
