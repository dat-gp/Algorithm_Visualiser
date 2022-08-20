# Imports
import pygame

# Initilisation
pygame.init()
pygame.font.init()

# Defining Window
WIN_HEIGHT, WIN_WIDTH = 700, 1300
WINDOW = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

# Set caption
pygame.display.set_caption("Sort Visualiser")

# Colors
COLOR = {'BLACK':(0,0,0),
         'WHITE': (255,255,255),
         'RED': (255,0,0),
         'GREEN': (0,255,0),
         'BLUE': (0,0,255),
         'YELLOW': (255,255,0)}

# Font
FONT = {20: pygame.font.SysFont("cascadia code", 20),
        25: pygame.font.SysFont("cascadia code", 25),
        30: pygame.font.SysFont("cascadia code", 30),
        35: pygame.font.SysFont("cascadia code", 35),
        45: pygame.font.SysFont("cascadia code", 45, italic=True)}


# FRAMERATE
FPS = 60