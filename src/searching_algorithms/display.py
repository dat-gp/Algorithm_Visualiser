'''
This module is consists of helper functions used for diplaying various elements on the screen.
They are called from algorithm functions.
'''

# Imports
import pygame
from src.helpers.constants import WINDOW, COLOR, FONT, FPS
from src.helpers.button import Button

# Pygame Initialisation
pygame.init()
pygame.font.init()

# Clock object
clock = pygame.time.Clock()



def header_txt(name: str, key: int):
    '''
    Responsible for blitting constant algo. hearder texts like:-
    - Algo. name
    - Key -  key to be searched
    - No of comaparisons title
    
    Args:
        - name: name of the algo.
        - key: key to be searched
    '''

    # Texts
    algo_name = FONT[25].render(f"Algo. Name: {name}", 1 , COLOR["WHITE"])
    searching = FONT[25].render(f"Searching for: {key}", 1, COLOR["WHITE"])
    comparisons = FONT[25].render("No of Comparions: ", 1, COLOR["WHITE"])
    
    # Rendering / Blitting Texts
    WINDOW.blit(algo_name, (0,0))
    WINDOW.blit(searching, (0,30))
    WINDOW.blit(comparisons, (550,30))


def draw_lines(values: list):
    '''
    Draws red lines acc. to the values in values list 
    Args: 
        - values: list of values
    '''

    # Bottom x coordintate, fist line starts from 4th co-ordinate from the left
    x = 4
    # for each value in the list of values
    for value in values:
        # Bottom y coordinate 600 from top
        (x1,y1) = (x,600)
        # calculating length of the line representing the value
        # length of line == y2 => substracting the value from 600
        (x2,y2) = (x1, y1-value)
        # Draw the line
        pygame.draw.line(WINDOW, COLOR["RED"], (x1,y1), (x2,y2), 1)
        # increment the x value with a step size of 3 so that the lines are not next to each other
        x+=3


def comparisons(no_of_compares):
    '''
    Displays the no of comparisons on the screen
    Arg:
        no_of_compares = the number of compares to be displayed
    '''
    comparisons_txt = FONT[25].render(f"{no_of_compares}", 1, COLOR['BLUE'], COLOR['BLACK'])
    WINDOW.blit(comparisons_txt, (710,30))
    pygame.display.update()


def draw(name, key, values):
    '''
    Prepares the screen before execution
    - Displays the name of the algorithm, the key being searched and the lines w.r.t the values
    Args:
        name = name of the algorithm passed from the algorithm function
        key = key being searched
        values = the array of values
    '''

    WINDOW.fill(COLOR["BLACK"])         # Blackens the screen so that the font and lines or other elements
                                        # that are blitted on the screen are clear and readable
    
    header_txt(name, key)               # The header text is blitted
    draw_lines(values)                  # lines are drawn according to the values in array
    pygame.display.update()   


# Button objs.
back_button = Button("Back", (0,645), 75,30)
redo_button = Button("Redo", (1235,645), 75,30)

def results_screen(key, index, x1,y1, x2,y2):
    '''
    Function called from algo. function when the key is found
    - BLits the result text - ___ key found at ___ index
    Args:
        - key = the key that was found
        - index = the index at which the key resides
        - x1,y1, x2,y2 = Co-ordinates of the key line
    '''

    running = True           # loop var.
    while running:           # main loop
        clock.tick(FPS)      # control FPS
        
        # result text
        result_txt = FONT[25].render(f"{key} found at index {index}", 1, COLOR['WHITE'], COLOR['BLACK'])
        WINDOW.blit(result_txt, (550, 650))
        
        # Highlighting the key line with green
        pygame.draw.line(WINDOW, COLOR['GREEN'], (x1,y1), (x2,y2), 1)
        
        # Buttons
        # back button returns to the main_screen
        clicked = back_button.draw()
        if clicked:
            return 'back'
        
        # finds the key again
        clicked = redo_button.draw()
        if clicked:
            return 'retry'
        
        
        pygame.display.update()
        
        # check if X button is pressed
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    return "quit"
        




          
