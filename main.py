'''
The main screen - It calls other categories of algo. for ex.: searching, sorting
Not working == Segmentation Fault
'''

# Imports
import pygame
from src.helpers.constants import WINDOW, COLOR, FONT, FPS
from src.searching_algorithms.main import main as searching_algos
# import src.sorting_algorithms.main

from src.helpers.button import Button

# Pygame Initialisations
pygame.init()

#clock object
clock = pygame.time.Clock()

# buttons obj. creation
button_1 = Button("Searching Algorithms", (550, 200), 200, 40)
button_2 = Button("Sorting Algorithms", (550, 260), 200, 40)
quit_button = Button("Quit", (575, 320), 150, 40)

# heading text
heading_txt = FONT[30].render("Algorithm Visualiser", 1, COLOR['WHITE'])

def main():
    running = True      # loop var.
    while running:      # main loop
        clock.tick(FPS)

        WINDOW.fill(COLOR['BLACK'])

        WINDOW.blit(heading_txt, (550,100))

        # call searching algorithms
        clicked = button_1.draw()
        if clicked:
            searching_algos()

        # call sorting algorithms
        clicked = button_2.draw()
        if clicked:
            # src.sorting_algorithms.main.main()
            pass

        # Close the window
        clicked = quit_button.draw()
        if clicked:
            running = False

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.quit()

if __name__ == "__main__":
    main()