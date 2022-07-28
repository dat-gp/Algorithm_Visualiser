'''
This module is used for supplying the array of values and displays the main_screen
'''

print("In src.seaching_sort.main")

# Imports
import random
import src.searching_algorithms.main_screen

# Pygame Initialisation
# pygame.font.init()

def main():
    
    # Creating Search key, Values list
    key = random.randint(0,433)
    values = [x for x in range (0,434)]
    random.shuffle(values)


    # Searching ALgo. main_screen function call
    src.searching_algorithms.main_screen.main_screen(values,key)

