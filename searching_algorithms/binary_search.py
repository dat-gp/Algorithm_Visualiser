# Imports
import pygame
import random
import time

import display
from essentials import WINDOW, COLOR, FONT

pygame.init()
pygame.font.init()

# FrameRate
FPS = 1

# clock object
clock = pygame.time.Clock()

# x coordinates
x = [x for x in range(4,1305,3)]

def disp_line(values, i=None,c=None,j=None):
    # During the highlighting of the section the 
    # starting point of section (i) and ending point of section (j) are highlighted in yellow
    # while the middle point (j) is highlighted in Green
    WINDOW.blit(FONT[25].render(f"Indexes: ", 1, COLOR['WHITE'], COLOR['BLACK']), (280, 70))
    if i != None:
        pygame.draw.rect(WINDOW, COLOR['BLACK'], pygame.Rect(400,65, 80,30))                # clear surface by blacking screen
        WINDOW.blit(FONT[25].render(f"i = {i}", 1, COLOR['YELLOW']),(410, 70))
        pygame.draw.line(WINDOW, COLOR['YELLOW'], (x[i],600), (x[i],600-values[i]))
    if c != None:
        pygame.draw.rect(WINDOW, COLOR['BLACK'], pygame.Rect(595,65, 80,30))                # clear surface by blacking screen
        WINDOW.blit(FONT[25].render(f"c = {c}", 1, COLOR['GREEN']), (600, 70))
        pygame.draw.line(WINDOW, COLOR['GREEN'], (x[c],600), (x[c],600-values[c]))
    if j != None:
        pygame.draw.rect(WINDOW, COLOR['BLACK'], pygame.Rect(805,65, 80,30))                # clear surface by blacking screen
        WINDOW.blit(FONT[25].render(f"j = {j}", 1, COLOR['YELLOW']), (810, 70))
        pygame.draw.line(WINDOW, COLOR['YELLOW'], (x[j],600), (x[j],600-values[j]))

    pygame.display.update()


def highlight_section(i,c,j, values):
    # Highlight the section with blue color
    for point in range(i,j):
        pygame.draw.line(WINDOW, COLOR['BLUE'], (x[point],600), (x[point], 600-point))

    pygame.display.update()
    display.draw_lines(values)
    time.sleep(0.2)


def disp_condition(condition, c, key, values):
    pygame.draw.rect(WINDOW, COLOR['BLACK'], pygame.Rect(590,100, 90, 30))
    if condition == 1:
        WINDOW.blit(FONT[25].render(f"{values[c]} != {key}", 1, COLOR['WHITE']),(590,100))
    if condition == 2:
        WINDOW.blit(FONT[25].render(f"{key} > {values[c]}", 1, COLOR['WHITE']),(590,100))
    if condition == 3:
        WINDOW.blit(FONT[25].render(f"{key} < {values[c]}", 1, COLOR['WHITE']),(590,100))
    if condition == 4:
        WINDOW.blit(FONT[25].render(f"{key} = {values[c]}", 1, COLOR['WHITE']),(590,100))

    pygame.display.update()


def logic_loop(values, key):
    index = 0

    i = 0
    j = len(values)-1
    c = int((i+j)/2)
    disp_line(values, i=i,c=c,j=j)

    while values[c] != key and i<=j:
        disp_condition(1, c, key, values)
        
        clock.tick(FPS)
        display.draw_lines(values)
        
        display.comparisons(index)

        # If the key is greater than the value checked
        if key > values[c]:
            disp_condition(2, c, key, values)
            # Select the right part
            i = c+1
            highlight_section(i,c,j,values)
            disp_line(values, i=i, j=j)

        # else the key is lesser than the value being checked
        else: 
            disp_condition(3,c,key, values)
            # Select the left part
            j = c-1
            highlight_section(i,c,j,values)
            disp_line(values, i=i,j=j)
        
        # calculate new center 
        c = int((i+j)/2)
        disp_line(values, c=c)
        index += 1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                string = 'quit'
                return string

    # Once the value is found
    # check if i is less than or equal to j
    if i<=j:
        display.draw_lines(values)
        disp_condition(4, c, key, values)
        string = display.results_screen(key, c, x[c],600, x[c],600-values[c])
        
    return string


def search(values, key):
    once = True

    running = True
    while running:
        clock.tick(FPS)
        display.draw("Binary Search", key, values)

        WINDOW.blit(FONT[25].render("Sorting...", 1, COLOR['GREEN'], COLOR['BLACK']), (10,110))
        pygame.display.update()

        time.sleep(0.5)
        if once:
            values.sort()
            once = False
        
        display.draw("Binary Search", key, values)

        # Logic Loop Function
        string = logic_loop(values, key)
        
        if string == 'quit':
            running = False
        if string == 'back':
            running = False
        if string == 'retry':
            continue

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.update()

    return string


if __name__ == "__main__":
    values = [x for x in range(0,434)]
    random.shuffle(values)
    search(values, 20)
