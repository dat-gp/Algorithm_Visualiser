# Imports
import pygame
import random
import time
from src.sorting_algorithms.constants import WINDOW, COLOR, FONT

# Initialization
pygame.init()

# frame in which lines are displayed
FRAME = pygame.Rect(0, 170, 1300, 430)

def header_txt(name):
    # rendering headers
    WINDOW.blit(FONT[25].render(f"Algo. Name: {name}", 1, COLOR['WHITE']), (0,0))
    WINDOW.blit(FONT[25].render(f"No. of comparisons: ", 1, COLOR['WHITE']), (0,30))


def comparisons(num):
    pygame.draw.rect(WINDOW, COLOR['BLACK'], pygame.Rect(180,30, 50,25))
    WINDOW.blit(FONT[25].render(f"{num}", 1, COLOR['WHITE']), (180,30))


def iterations(num):
    pygame.draw.rect(WINDOW, COLOR['BLACK'], pygame.Rect(0, 60, 250,21))
    WINDOW.blit(FONT[25].render(f"Number of iterations: {num}", 1, COLOR['WHITE']), (0,60))

def draw_lines(values, y1=600):
    if y1!=600:
        pygame.draw.rect(WINDOW, COLOR['BLACK'], pygame.Rect(0,y1-430,1300,430))
    else:
        pygame.draw.rect(WINDOW, COLOR['BLACK'], FRAME)

    x1 = 4
    for value in values:
        (x2,y2) = (x1,y1-value)
        pygame.draw.line(WINDOW, COLOR['RED'], (x1,y1), (x2,y2))
        x1+=3


def draw(name, values, y1=600):
    WINDOW.fill(COLOR['BLACK'])
    header_txt(name)
    draw_lines(values, y1)

    pygame.display.update()


def underline_sec(i, x, delay=0):
    # Rendering black background for text
    pygame.draw.rect(WINDOW, COLOR['BLACK'],pygame.Rect(0,605,1300,20))                     # background
    
    # texts
    sorted_txt = FONT[20].render("Sorted", 1, COLOR['GREEN'])
    unsorted_txt = FONT[20].render("Unsorted", 1, COLOR['RED'])


    x1,y1 = (4,605)

    # Drawing Lines
    pygame.draw.line(WINDOW, COLOR['GREEN'],(x1,y1),(x[i],y1))              # for sorted
    pygame.draw.line(WINDOW, COLOR['RED'],(x[i],y1),(1300,y1))              # for unsorted
    
    sorted_dist = (x[i]-4)
    WINDOW.blit(sorted_txt, (sorted_dist//2,610))                  # rendering sorted text
    
    unsorted_dist = (1300+x[i])
    WINDOW.blit(unsorted_txt, (unsorted_dist//2,610))              # rendering unsorted text
    
    pygame.display.update()
    time.sleep(delay)



# button dimensions
back_button = pygame.Rect(0,650, 60,30)
# redo_button = pygame.Rect(1240,650, 60,30)


click = False

def result_screen():
    running = True
    while running:
        # Background frame
        pygame.draw.rect(WINDOW, COLOR['BLACK'], pygame.Rect(0,650, 1300, 100))

        # Rendering result
        pygame.draw.rect(WINDOW, COLOR['BLACK'], pygame.Rect(0,100, 1305,30))    
        WINDOW.blit(FONT[30].render("List Sorted", 1, COLOR['GREEN']), (600,100))

        # Rendering Buttons
        pygame.draw.rect(WINDOW,COLOR['WHITE'],back_button)
        # pygame.draw.rect(WINDOW,COLOR['WHITE'],redo_button)

        # Rendering texts
        WINDOW.blit(FONT[25].render("Back", 1, COLOR['BLACK']), (10,657))
        # WINDOW.blit(FONT[25].render("Redo", 1, COLOR['BLACK']), (1249,657))

        pygame.display.update()

        mx,my = pygame.mouse.get_pos()
        
        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return -1
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        if click:
            if back_button.collidepoint((mx,my)):
                print("clicked back")
                return 0
            # if redo_button.collidepoint((mx,my)):
            #     print("clicked redo")
            #     return 1


def disp_under_construction(name):
    running = True
    while running:
        WINDOW.fill(COLOR['BLACK'])
        WINDOW.blit(FONT[45].render("Under Contruction", 1, COLOR['WHITE']), (525,80))

        WINDOW.blit(FONT[25].render(f"- This is {name} visualiser.", 1, COLOR['WHITE']), (100,200))
        WINDOW.blit(FONT[25].render("- In Development Phase.", 1, COLOR['WHITE']), (100,230))
        
        for x in range(0,1300,10):
            WINDOW.blit(FONT[25].render(f"-", 1, COLOR['YELLOW']), (x, 50))
            WINDOW.blit(FONT[25].render(f"-", 1, COLOR['YELLOW']), (x, 120))

        # Rendering Buttons
        pygame.draw.rect(WINDOW,COLOR['WHITE'],back_button)

        # Rendering texts
        WINDOW.blit(FONT[25].render("Back", 1, COLOR['BLACK']), (10,657))

        pygame.display.update()

        mx,my = pygame.mouse.get_pos()
        
        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return -1
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        if click:
            if back_button.collidepoint((mx,my)):
                print("clicked back")
                return 0
            


def main(name, values):
    running = True
    while running:

        draw(name, values)

        mx,my = pygame.mouse.get_pos()

        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
       
        if click:
            print(mx,my)

    pygame.quit()


if __name__ == "__main__":
    arr = [x for x in range(1,430)]
    random.shuffle(arr)
    main("Algorithm",arr)
