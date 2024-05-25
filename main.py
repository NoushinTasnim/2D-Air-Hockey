# Group Members
# 1. Hasib Rayhan Dewan Akash (Roll-08)
# 2. Noushin Tasnim (Roll-14)

import glfw
from OpenGL.GL import *
from values import *
from players import *
from circle_draw import*
from scores import *

keys_pressed = set()

def display(val):
    glClear(GL_COLOR_BUFFER_BIT)

    # draw player scores
    val.player1.draw_score(1, val)
    val.player2.draw_score(2, val)

    # draw table
    val.table.draw_board(val)

    # draw player paddles
    val.player1.draw_paddle(val)
    val.player2.draw_paddle(val)

    # draw ball
    val.ball.draw_ball()

    glEnd()
    glFlush()

# Press and release key
def key_callback(window, key, scancode, action, mods):    
    if action == glfw.PRESS:
        keys_pressed.add(key)
    elif action == glfw.RELEASE:
        keys_pressed.remove(key) if key in keys_pressed else None

def main():
    global player1, player2, ball, WINDOW_WIDTH, WINDOW_HEIGHT

    if not glfw.init():
        return

     # Get the primary monitor
    monitor = glfw.get_primary_monitor()

    # Get the video mode of the monitor
    mode = glfw.get_video_mode(monitor)

    # get window height and width
    WINDOW_WIDTH = mode.size.width
    WINDOW_HEIGHT = mode.size.height
    print(WINDOW_WIDTH )

    val = Values(WINDOW_HEIGHT, WINDOW_WIDTH)

    # Create a window with full screen size
    window = glfw.create_window(WINDOW_WIDTH, WINDOW_HEIGHT, "Air Hockey", monitor, None)

    if not window:
        glfw.terminate()
        return

    glfw.make_context_current(window)

    glClearColor(val.table.bg_color_r/255, val.table.bg_color_g/255, val.table.bg_color_b/255, 1.0)  # Green background

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-WINDOW_WIDTH / 2, WINDOW_WIDTH / 2, -WINDOW_HEIGHT / 2, WINDOW_HEIGHT / 2, -1.0, 1.0)
    glfw.set_key_callback(window, key_callback)

     # The game has not yet started
    reset_flag = 1  
    
    while not glfw.window_should_close(window):
        glClear(GL_COLOR_BUFFER_BIT)

         # display all the elements: table, paddles, ball
        display(val)
        
        for key in keys_pressed:
            if key == glfw.KEY_W: # player 1 move up
                val.player1.move_up(val)
            elif key == glfw.KEY_S: # player 1 move down
                val.player1.move_down(val)
            elif key == glfw.KEY_A: # player 1 move left
                val.player1.move_left(val)
            elif key == glfw.KEY_D: # player 1 move right
                val.player1.move_right(val)
            elif key == glfw.KEY_UP: # player 2 move up
                val.player2.move_up(val)
            elif key == glfw.KEY_DOWN: # player 2 move down
                val.player2.move_down(val)
            elif key == glfw.KEY_LEFT: # player 2 move left
                val.player2.move_left(val)
            elif key == glfw.KEY_RIGHT: # player 2 move right
                val.player2.move_right(val)
            elif key == glfw.KEY_ESCAPE: # Close game
                glfw.set_window_should_close(window, True)

        # move ball
        val.ball.update_position() 
        # change direction if collides with border
        val.ball.border_collision(val) 
        
        # change direction if collides with player 1
        is_col1 = val.ball.collision_with_player(val.player1, val)
        # change direction if collides with player 2
        is_col2 = val.ball.collision_with_player(val.player2, val)

        # After goal, the ball is moved by any player
        if(reset_flag==1) and (is_col1 is True or is_col2 is True): 
            # Update ball speed from 0 to BALL_SPEED_X and Y
            val.ball.speed_x = val.ball_speed_x 
            val.ball.speed_y = val.ball_speed_y
            # Game has begun again
            reset_flag = 0

        # Player 1 scores a goal
        if val.ball.goal(WINDOW_WIDTH/2 - val.goalpost_x, val) is True : 
            # Player 1 score increases
            val.player1.score += 1
            # Reset ball: ball position and speed is set to 0
            reset_flag = 1 
            # Player positions are reset
            val.player1.reset_paddle(-1, val)
            val.player2.reset_paddle(1, val)

        # Player 2 scores a goal
        if val.ball.goal(-WINDOW_WIDTH/2 + val.goalpost_x, val) is True : 
            # Player 2 score increases
            val.player2.score += 1 
            # Reset ball: ball position and speed is set to 0
            reset_flag = 1 
            # Player positions are reset
            val.player1.reset_paddle(-1, val)
            val.player2.reset_paddle(1, val)

        glfw.swap_buffers(window)
        glfw.poll_events()

    glfw.terminate()

if __name__ == "__main__":
    main()