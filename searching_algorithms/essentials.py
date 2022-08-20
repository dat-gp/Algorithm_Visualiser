# IMPORTS
import pygame

pygame.init()
pygame.font.init()

# Window Definiton
WINDOW_HEIGHT, WINDOW_WIDTH = 700, 1310
WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))


# Colors
COLOR = {'BLACK' : (0,0,0),
         'WHITE' : (255,255,255),
         "RED"   : (255,0,0),
         "GREEN" : (0,255,0),
         "BLUE"  : (0,0,255),
         "YELLOW": (255,255,0)}

# FPS
FPS = 60

# Font
FONT = {25: pygame.font.SysFont("cascadia code", 25),
        30: pygame.font.SysFont("cascadia code", 30)}
