import pygame
import display
from essentials import WINDOW, FONT, COLOR

pygame.init()


def sort(arr):
    running = True
    while running:
        
        result = display.disp_under_construction("Bucket Sort")
        if result == -1:
            return -1
        if result == 0:
            running = False
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return -1

    return 0

if __name__ == "__main__":
    values = [1,24,564,213,133]
    sort(values)