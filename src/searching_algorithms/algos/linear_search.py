'''
Performs and displays the working of linear search
'''

# Imports
import pygame
import src.searching_algorithms.display as display
from src.helpers.constants import WINDOW, COLOR, FPS


# pygame initialisations
pygame.init()
pygame.font.init()


# clock object
clock = pygame.time.Clock()

# =============== Main Logic of the algo. =================================
def logic_loop(values, key):
    '''
    logic of linear search called from main function
    -- the key is searched in this function --
    Args:
        - values: list of values
        - key: the key to be searched
    '''
    # cursor in the array for linear_search 
    # and the number of comparisons 
    index = 0

    # Bottom Co-ordinates of the parser line (blue): y1 remains conmstant
    (x1,y1) = (4,600)

    running = True                 # loop variable  
    while running:                 # main loop
        clock.tick(FPS)            # controls fps

        # Display the constant header section of algorithm and the lines
        # name of the algo, key being searched and the lines
        display.draw("Linear Search", key, values)          

        # Upper Co-ordinates of parser line (blue):-   [Parser line shows the value being compared]
        # x2 = x1 => as the line is a straight vertical line
        # y2 = (y1-value[index]) => 600 - value at indexth index  
        # x2, y2 both change after every iteration

        # draw the parser line
        pygame.draw.line(WINDOW, COLOR['BLUE'], (x1,y1), (x1, y1-values[index]), 1)
        pygame.display.update()

        # display the number of comparisons
        display.comparisons(index)

        # if key == value
        if key == values[index]:
            # display comparisons
            display.comparisons(index)

            # go to result screen
            string = display.results_screen(key, index, x1,y1, x1,y1-values[index])
            break

        # check if the user wants to close the window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                string = 'quit'
                return string

        x1 += 3
        index += 1


    return string


def search(values, key):
    '''
    The search function calls the main logic function and is called from the main 
    '''    
    running = True                  # loop variable
    while running:                  # main loop
        clock.tick(FPS)             # controls the fps

        string = logic_loop(values,key)
        if string == "back":
            running = False
        if string == "quit":
            return string

                
# =========================================================================