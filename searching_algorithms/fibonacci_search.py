# Imports
import pygame
import display
from essentials import WINDOW

# Initialisation
pygame.init()

def logic_loop(values, key):
    pass

# main
def search(values, key):
    running = True
    while running:

        display.draw("Fibonacci Search", key, values)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.quit()

if __name__ == "__main__":
    key = 20
    values = [x for x in range(0,434)]
    search(values,key)
