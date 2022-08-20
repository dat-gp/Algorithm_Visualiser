# Imports
import pygame
from essentials import WINDOW, COLOR, FPS, FONT

pygame.init()
pygame.font.init()

# Clock object
clock = pygame.time.Clock()

def header_txt(name, key):
    # Texts
    algo_name = FONT[25].render(f"Algo. Name: {name}", 1 , COLOR["WHITE"])
    searching = FONT[25].render(f"Searching for: {key}", 1, COLOR["WHITE"])
    comparisons = FONT[25].render("No of Comparions: ", 1, COLOR["WHITE"])
    
    # Rednering Texts
    WINDOW.blit(algo_name, (0,0))
    WINDOW.blit(searching, (0,30))
    WINDOW.blit(comparisons, (550,30))


def draw_lines(values):
    x = 4
    for value in values:
        (x1,y1) = (x,600)
        (x2,y2) = (x1, y1-value)
        pygame.draw.line(WINDOW, COLOR["RED"], (x1,y1), (x2,y2), 1)
        x+=3


click = False
def results_screen(key, index, x1,y1, x2,y2):

    running = True
    while running:
        clock.tick(FPS)
        
        result_txt = FONT[25].render(f"{key} found at index {index}", 1, COLOR['WHITE'], COLOR['BLACK'])
        WINDOW.blit(result_txt, (550, 650))
        
        # Rendering Green/Found Line
        pygame.draw.line(WINDOW, COLOR['GREEN'], (x1,y1), (x2,y2), 1)
        
        # Buttons
        back_button = pygame.Rect(0, 645, 75, 30)
        retry_button = pygame.Rect(1235, 645, 75, 30)
        pygame.draw.rect(WINDOW, COLOR['WHITE'], back_button)
        pygame.draw.rect(WINDOW, COLOR['WHITE'], retry_button)
        
        # Rendering Text on buttons
        back_txt = FONT[25].render(" Back ", 1, COLOR['BLACK'])
        retry_txt = FONT[25].render(" Redo ", 1, COLOR['BLACK'])
        WINDOW.blit(back_txt, (10,650))
        WINDOW.blit(retry_txt, (1245,650))
        
        pygame.display.update()
        
        (mx,my) = pygame.mouse.get_pos()
        
        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        if click:
            if back_button.collidepoint((mx,my)):
                return 'back'
            if retry_button.collidepoint((mx,my)):
                return "retry"

    return "quit"
        

def comparisons(index):
    comparisons_txt = FONT[25].render(f"{index}", 1, COLOR['BLUE'], COLOR['BLACK'])
    WINDOW.blit(comparisons_txt, (710,30))
    pygame.display.update()


def draw(name, key, values):
    WINDOW.fill(COLOR["BLACK"])
    header_txt(name, key)
    draw_lines(values)
    pygame.display.update()
