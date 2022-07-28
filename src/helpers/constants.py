'''
Constants
'''

# Imports
import pygame

# Initilisation
pygame.init()
pygame.font.init()

# Defining Window
WINDOW_HEIGHT, WINDOW_WIDTH = 700, 1300
WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# Set caption
pygame.display.set_caption("Algo. Visualiser")

# Colors
COLOR = {'BLACK':(0,0,0),
         'WHITE': (255,255,255),
         'RED': (255,0,0),
         'GREEN': (0,255,0),
         'BLUE': (0,0,255),
         'YELLOW': (255,255,0),
         'TEAL': (0,128,128),
         'GREY': (128,128,128),
         'DARK GREEN': (0,153,76),
         'DARK YELLOW': (153,153,0)}

# Font
FONT = {20: pygame.font.SysFont("cascadia code", 20),
        25: pygame.font.SysFont("cascadia code", 25),
        30: pygame.font.SysFont("cascadia code", 30),
        35: pygame.font.SysFont("cascadia code", 35),
        45: pygame.font.SysFont("cascadia code", 45, italic=True)}


# FRAMERATE
FPS = 60