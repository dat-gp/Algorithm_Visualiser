# imports
import pygame
import random
import main_screen

# Initialisation
pygame.font.init()

# Search key, Value
key = random.randint(0,433)
values = [x for x in range (0,434)]

# Function Call
main_screen.main_screen(values,key)
