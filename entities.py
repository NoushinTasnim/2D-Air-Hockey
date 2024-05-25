# Segments for drawing score and texts
digit_segments = {
    0: [(0, 0), (1, 0), (1, 2), (0, 2), (0, 0)],
    1: [(0.5,1.5),(1, 2), (1, 0),(0.5,0),(1.5,0)],
    2: [(1, 0), (0, 0), (0, 1), (1, 1), (1, 2), (0, 2)],
    3: [(0, 0), (1, 0), (1, 1), (0, 1), (1, 1), (1, 2), (0, 2)],
    4: [(0, 2), (0, 1), (1, 1), (1, 2), (1, 1), (1, 0)],
    5: [(0, 0), (1, 0), (1, 1), (0, 1), (0, 2), (1, 2)],
    6: [(1, 2), (0, 2), (0, 0), (1, 0), (1, 1), (0, 1)],
    7: [(0, 2), (1, 2), (1, 0)],
    8: [(0, 0), (1, 0), (1, 2), (0, 2), (0, 0), (0, 1), (1, 1)],
    9: [(1, 1), (0, 1), (0, 2), (1, 2), (1, 1), (1, 0), (0,0)],
    'T':[(0, 2), (2, 2), (1, 2), (1, 0)],
    'E':[(2, 2), (0, 2), (0, 1), (2, 1), (0, 1), (0, 0), (2,0)],  
    'A':[(0, 0), (0, 2), (2, 2), (2,0),(2,1),(0,1)],
    'M':[(0, 0), (0, 2), (1, 1), (2, 2), (2, 0)],
    'X':[(0, 2), (2, 0),(1,1),(2,2),(0,0)],
    'Y':[(0, 2), (1, 1), (2, 2), (1, 1), (1, 0)],
    '-':[(0,1),(2,1)],
    'P':[(0, 0), (0, 2), (2, 2), (2, 1), (0, 1)],
    'R':[(0, 0), (0, 2), (2, 2), (2, 1), (0, 1),(2,0)],
    'S':[(0, 0), (1, 0), (1, 1), (0, 1), (0, 2), (1, 2)],
    'C':[(2, 2), (0, 2), (0, 0), (2, 0)],
    'O':[(0, 2), (2, 2),(2,0),(0,0),(0,2)],
    'L': [(0, 2), (0, 0), (2, 0)],
}

# HSB to RGB Conversion
def hsb_to_rgb(h, s, b):
    """
    Convert HSB (Hue, Saturation, Brightness) color to RGB (Red, Green, Blue).
    h: Hue (0-360)
    s: Saturation (0-1)
    b: Brightness (0-1)
    Returns a tuple (r, g, b) where each component is in the range 0-1.
    """
    if s == 0:
        return (int(b*255), int(b*255), int(b*255))  # Achromatic (gray)
    h /= 60  # sector 0 to 5
    i = int(h)
    f = h - i  # factorial part of h
    p = b * (1 - s)
    q = b * (1 - s * f)
    t = b * (1 - s * (1 - f))
    if i == 0:
        return (int(b*255), int(t*255), int(p*255))
    elif i == 1:
        return (int(q*255), int(b*255), int(p*255))
    elif i == 2:
        return (int(p*255), int(b*255), int(t*255))
    elif i == 3:
        return (int(p*255), int(q*255), int(b*255))
    elif i == 4:
        return (int(t*255), int(p*255), int(b*255))
    else:
        return (int(b*255), int(p*255), int(q*255))

# Table background color
bg_color_r, bg_color_g, bg_color_b = hsb_to_rgb(200, 0.7, 0.8) # Sky Blue

# Ball Color
ball_color_r, ball_color_g, ball_color_b = hsb_to_rgb(35, 1, .5) # Brown

# Color of the borders and circles on the table
table_design_color_r, table_design_color_g, table_design_color_b = hsb_to_rgb(210, 0, 1)

# Each player will have 3 colors
# player 1 colors
player1_color1_r, player1_color1_g, player1_color1_b = hsb_to_rgb(320, 1, .5)
player1_color2_r, player1_color2_g, player1_color2_b = hsb_to_rgb(320, 1, .75)
player1_color3_r, player1_color3_g, player1_color3_b = hsb_to_rgb(320, 1, 1)

# player2 colors
player2_color1_r, player2_color1_g, player2_color1_b = hsb_to_rgb(100, 1, .5)
player2_color2_r, player2_color2_g, player2_color2_b = hsb_to_rgb(100, 1, .75)
player2_color3_r, player2_color3_g, player2_color3_b = hsb_to_rgb(100, 1, 1)