'''
Performs and displays the working of linear search
'''

# Imports
import pygame
import random
import time
import src.searching_algorithms.display as display
from src.helpers.constants import WINDOW, COLOR, FONT

# Pygame Initialisations
pygame.init()
pygame.font.init()

# FrameRate
FPS = 1

# clock object
clock = pygame.time.Clock()

# x coordinates: list of x co-ordinates [4, 7, 10, ............,1300, 1303] 
x = [x for x in range(4,1305,3)]


# =============== helper display functions of binary search ===============
def disp_line(values, i=None,c=None,j=None):
    '''
    Displays the indexes (i,c,j values) in the top section as well as highlights the i, c, j lines
    - i value and line = Yellow 
    - c value and line = Green  
    - j value and line = Yellow  
    '''
    # Render Indexes: text
    WINDOW.blit(FONT[25].render(f"Indexes: ", 1, COLOR['WHITE'], COLOR['BLACK']), (280, 70))

    if i != None:
        pygame.draw.rect(WINDOW, COLOR['BLACK'], pygame.Rect(400,65, 80,30))            # background for i value text
        WINDOW.blit(FONT[25].render(f"i = {i}", 1, COLOR['YELLOW']),(410, 70))          # i = i_value
        pygame.draw.line(WINDOW, COLOR['YELLOW'], (x[i],600), (x[i],600-values[i]))     # highlight i line with yellow
    if c != None:
        pygame.draw.rect(WINDOW, COLOR['BLACK'], pygame.Rect(595,65, 80,30))            # background for c value text
        WINDOW.blit(FONT[25].render(f"c = {c}", 1, COLOR['GREEN']), (600, 70))          # c = c_value
        pygame.draw.line(WINDOW, COLOR['GREEN'], (x[c],600), (x[c],600-values[c]))      # highlight i line with yellow
    if j != None:
        pygame.draw.rect(WINDOW, COLOR['BLACK'], pygame.Rect(805,65, 80,30))            # background for j value text
        WINDOW.blit(FONT[25].render(f"j = {j}", 1, COLOR['YELLOW']), (810, 70))         # j = j_value
        pygame.draw.line(WINDOW, COLOR['YELLOW'], (x[j],600), (x[j],600-values[j]))     # highlight i line with yellow

    pygame.display.update()


def highlight_section(i, j, values):
    '''
    Highlights the section that is selected in which the value will be searched
    '''

    # highlight section with blue
    for point in range(i,j):
        pygame.draw.line(WINDOW, COLOR['BLUE'], (x[point],600), (x[point], 600-point))

    pygame.display.update()

    # De-highlight the section 
    display.draw_lines(values)
    time.sleep(0.2)


def disp_condition(condition, c, key, values):
    '''
    Displays the comparison between center value and key at the top below indexes
    '''

    pygame.draw.rect(WINDOW, COLOR['BLACK'], pygame.Rect(590,100, 90, 30))                  # background for text
    if condition == 1:
        WINDOW.blit(FONT[25].render(f"{values[c]} != {key}", 1, COLOR['WHITE']),(590,100))
    if condition == 2:
        WINDOW.blit(FONT[25].render(f"{key} > {values[c]}", 1, COLOR['WHITE']),(590,100))
    if condition == 3:
        WINDOW.blit(FONT[25].render(f"{key} < {values[c]}", 1, COLOR['WHITE']),(590,100))
    if condition == 4:
        WINDOW.blit(FONT[25].render(f"{key} = {values[c]}", 1, COLOR['WHITE']),(590,100))

    pygame.display.update()

# =========================================================================

# =============== Main Logic of the algo. =================================

def logic_loop(values, key):
    '''
    logic of linear search called from the search function 
    -- the key is searched in this function --
    Args:
        - values: list of values 
        - key: key to be searched
    '''

    # the number of comparisons set to zero before logic loop
    no_of_compares = 0

    # i is assumed to be the 0th index of the list
    i = 0
    # j is assumed to be -1th i.e last index of the list
    j = len(values)-1
    # c = center of the partition calculated from i and j values
    c = int((i+j)/2)

    # display i,c,j lines and indexes
    disp_line(values, i=i,c=c,j=j)

    # if the center value != key and the start is less the end of partition
    while values[c] != key and i<=j:                # logic loop
        clock.tick(FPS)                             # control fps

        # display condition 1 => key != c_value
        disp_condition(1, c, key, values)
        
        # reset to red lines
        display.draw_lines(values)
        
        # display the no. of comparisons
        display.comparisons(no_of_compares)

        if key > values[c]:
            # display condition 2 => key > c_value
            disp_condition(2,c,key, values)
            # select right partition
            i = c+1
            # highlight the right partition
            highlight_section(i,j,values)
            # display the new i and j values and highlight the lines
            disp_line(values,i=i,j=j)

        else: 
            # display condition 3 => key < c_value
            disp_condition(3,c,key, values)
            # select left partition
            j = c-1
            # highlight the left partition
            highlight_section(i,j,values)
            # display the new i and j values and highlight the lines
            disp_line(values,i=i,j=j)
        
        # calculate the new center
        c = int((i+j)/2)

        # display the new value of center
        disp_line(values, c=c)

        # increment the no. of comparisons
        no_of_compares += 1

        # check if the cross button is pressed
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                string = 'quit'
                return string

    # if the center value == key it breaks from the while loop and the following condition is run
    # if the start is less the end of partition
    if i<=j:
        # reset to red lines
        display.draw_lines(values)
        # display condition 4 => key == value
        disp_condition(4, c, key, values)
        # go to result screen
        string = display.results_screen(key, c, x[c],600, x[c],600-values[c])
        
    return string


def search(values, key):
    '''
    Main function called from main_screen 
    Args:
        - values - list of values
        - key - key to be searched
    '''

    once = True              

    running = True              # loop variable
    while running:              # main loop
        clock.tick(FPS)         # control FPS

        # Display the constant header section of algorithm and the lines
        # name of the algo, key being searched and the lines
        display.draw("Binary Search", key, values) 

        # Binary searching needs a sorted list
        # display the sorting text
        WINDOW.blit(FONT[25].render("Sorting...", 1, COLOR['GREEN'], COLOR['BLACK']), (10,110))
        pygame.display.update()
        time.sleep(0.5)

        # run only once
        if once:       
            # sort the list     
            values.sort()
            # set once var. to false
            once = False
        
        # Clear the screen with black, again blit the name of algo, key
        # and disp. the lines acc. to the sorted list of value
        display.draw("Binary Search", key, values)


        string = logic_loop(values, key)
        
        if string == 'quit':
            running = False
        if string == 'back':
            running = False
        if string == 'retry':
            continue

        # check if cross button is pressed
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.update()

    return string

# =========================================================================
