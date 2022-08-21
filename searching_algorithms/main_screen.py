# Importing Modules
import pygame
import random
import linear_search, binary_search, exp
from essentials import WINDOW, WINDOW_WIDTH, WINDOW_HEIGHT, COLOR, FPS, FONT

# Initialisation
pygame.init()
pygame.font.init()

# set caption
pygame.display.set_caption("Search Visualiser")

# Buttons
button_1 = pygame.Rect(WINDOW_WIDTH//2-105, 180, 210, 50)
button_2 = pygame.Rect(WINDOW_WIDTH//2-105, 250, 210, 50)
quit_button = pygame.Rect(WINDOW_WIDTH//2-105, 600, 210, 50)

# Texts Formats
heading_txt = FONT[30].render("Algorithm Visualiser", 1 , COLOR['WHITE'])
linear_search_txt = FONT[30].render("Linear Search", 1, COLOR['BLACK'])
binary_search_txt = FONT[30].render("Binary Search", 1, COLOR['BLACK'])
quit_txt = FONT[30].render("QUIT", 1,  COLOR['BLACK'])


def draw():
    WINDOW.fill(COLOR['BLACK'])      # background
    
    # Render Heading
    WINDOW.blit(heading_txt, (WINDOW_WIDTH//2-100,WINDOW_HEIGHT//2-250))

    # Rendering Buttons
    pygame.draw.rect(WINDOW, COLOR['WHITE'], button_1, border_radius=2)
    pygame.draw.rect(WINDOW, COLOR['WHITE'], button_2, border_radius=2)
    pygame.draw.rect(WINDOW, COLOR['WHITE'], quit_button, border_radius=2)
    
    # Rendering Text on buttons
    WINDOW.blit(linear_search_txt, (WINDOW_WIDTH//2-70, WINDOW_HEIGHT//2-155))
    WINDOW.blit(binary_search_txt, (WINDOW_WIDTH//2-70, 265))
    WINDOW.blit(quit_txt, (WINDOW_WIDTH//2-30, 615))

    # render general expanation
    exp.general()
     

click = False       # clicking variable

def main_screen(values, key):
    clock = pygame.time.Clock()

    running = True
    while running:
        clock.tick(FPS)

        draw()

        mx, my = pygame.mouse.get_pos()

        click = False                               # set to false before checking the input in every frame

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:                # check - if clicked
                if event.button == 1:
                    click = True

    
        if button_1.collidepoint((mx,my)):
            exp.linear_search()
            if click:
                random.shuffle(values)
                flow_var = linear_search.search(values, key)
                if flow_var == "quit":
                    running = False

        if button_2.collidepoint((mx,my)):
            exp.binary_search()
            if click:
                random.shuffle(values)
                flow_var = binary_search.search(values,key)
                if flow_var == "quit":
                    running = False

        if quit_button.collidepoint((mx, my)):
            if click:
                running = False                                     # quit

        
        pygame.display.update()
    pygame.quit()


