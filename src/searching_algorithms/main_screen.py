'''
This module is responsible for diplaying the main_screen
'''

# Importing Modules
import pygame
import src.searching_algorithms.algos.linear_search as linear_search
import src.searching_algorithms.algos.binary_search as binary_search
import src.searching_algorithms.explanations as expl
from src.helpers.button import Button
from src.helpers.constants import WINDOW, WINDOW_WIDTH, WINDOW_HEIGHT, COLOR, FPS, FONT


# Pygame Initialisations
pygame.init()
pygame.font.init()

# CLock Object
clock = pygame.time.Clock()

# Buttons
button_1 = Button("Linear Search", (545, 180), 210, 50, expl.linear_search)
button_2 = Button("Binary Search", (545, 250), 210, 50, expl.binary_search)
quit_button = Button("QUIT", (545, 600), 210, 50)

# Texts Formats
heading_txt = FONT[30].render("Algorithm Visualiser", 1 , COLOR['WHITE'])


def draw():
    WINDOW.fill(COLOR['BLACK'])      # background
    
    # Render Heading
    WINDOW.blit(heading_txt, (WINDOW_WIDTH//2-100,WINDOW_HEIGHT//2-250))

    # render general explanation
    expl.general()


def main_screen(values, key):

    running = True          # loop variable
    while running:          # main loop
        clock.tick(FPS)     # control fps

        draw()

        # Check if buttons clicked and perform resp. actions
        clicked = button_1.draw()
        if clicked:
            linear_search.search(values,key)


        clicked = button_2.draw()
        if clicked:
            binary_search.search(values,key)

        clicked = quit_button.draw()
        if clicked:
            running = False


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


        pygame.display.update()
    pygame.quit()
