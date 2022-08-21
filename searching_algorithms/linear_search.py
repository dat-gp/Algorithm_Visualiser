# Imports
import pygame
import display
from essentials import WINDOW, COLOR, FPS

pygame.init()
pygame.font.init()

# clock object
clock = pygame.time.Clock()


def logic_loop(values, key):

    index = 0
    (x1,y1) = (4,600)

    running = True
    while running:
        clock.tick(FPS)
        display.draw("Linear Search", key, values)

        # Length of line representing number
        (x2,y2) = (x1, y1-values[index])

        pygame.draw.line(WINDOW, COLOR['BLUE'], (x1,y1), (x2,y2), 1)
        pygame.display.update()

        display.comparisons(index)

        # Sequential Search Logic
        if key == values[index]:
            display.comparisons(index)
            string = display.results_screen(key, index, x1,y1, x2,y2)
            break

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                string = 'quit'
                return string


        x1 += 3
        index += 1


    return string

def search(values, key):
    
    running = True
    while running:
        clock.tick(FPS)

        string = logic_loop(values,key)
        if string == "back":
            running = False
        if string == "quit":
            return string



    

        



        


