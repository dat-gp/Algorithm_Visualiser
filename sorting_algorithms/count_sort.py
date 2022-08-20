# Imports
import pygame
import random, time

import display
from essentials import WINDOW, COLOR, FONT

# Initialsation
pygame.init()

# Delay
dealy = 0

# x coordinates
x = [x for x in range(4,1300,3)]



def disp_count_arr():
    '''
    displays "Count Arr." WHITE text
    '''
    
    WINDOW.blit(FONT[25].render("Count Arr.", 1, COLOR['WHITE'], COLOR['BLACK']),(600, 110))


def check_quit():
    '''
    checks if quit was clicked  
    '''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return -1                       # if quit

    return 0        


def max_func(arr):
    # returns the max number in array

    max_num = arr[0]
    for num in arr:
        if num > max_num:
            max_num = num
        
    return max_num


def count_sort(arr):
    max_num = max_func(arr)
    count_arr = [0 for x in range(max_num+1)]
    disp_count_arr()

    x1 = 4
    for value in arr:
        count_arr[value]+=1
        display.draw_lines(arr)
        pygame.display.update()
        pygame.draw.line(WINDOW, COLOR['GREEN'], (x1, 600), (x1, 600-value))         # Green Parser through lines
        pygame.draw.rect(WINDOW, COLOR['BLACK'], pygame.Rect(0, 96, 1300, 8))        # Background for count arr. cursor
        pygame.draw.line(WINDOW, COLOR['GREEN'], (x[value], 96), (x[value], 103))    # Green count arr. cursor
        pygame.draw.line(WINDOW, COLOR['RED'], (x[value], 85), (x[value], 93))       # red points
        pygame.display.update()
        # time.sleep(0.1)
        # display.draw_lines(arr)
        # pygame.display.update()

        result = check_quit()
        if result == -1:
            return -1

        x1+=3
    
    pygame.draw.rect(WINDOW, COLOR['BLACK'], pygame.Rect(0, 96, 1300, 8))        # Background for count arr. cursor
    display.draw_lines(arr)    

    value = 0
    j = 0
    x1 = 4
    compare = 0
    while value < max_num+1:                                                    # max_num+1 is the len of the final arr.
        pygame.draw.line(WINDOW, COLOR['GREEN'], (x1,85), (x1,93))              # Green parser in count arr.
        if count_arr[value] > 0:
            arr[j] = value
            display.draw_lines(arr)
            pygame.display.update()
            j+=1
            count_arr[value]-=1
            pygame.draw.rect(WINDOW, COLOR['BLACK'], pygame.Rect(0, 85, x1, 9))              # Green parser in count arr.
            pygame.draw.line(WINDOW, COLOR['GREEN'], (x[value], 603), (x[value], 615))       # Green main lines cursor
            pygame.draw.rect(WINDOW, COLOR['BLACK'], pygame.Rect(0, 603, x1, 7))             
            pygame.display.update()

            # time.sleep(0.2)

        else:
            value+=1
            if x1<1299:
                x1+=3     

        result = check_quit()
        if result == -1:
            return -1

    return 0


def is_sorted(arr):
    d = {"True" : 0,
         "False": 0}

    sorted_list = sorted(arr)

    for i in range(len(arr)):
        if arr[i] == sorted_list[i]:
            d["True"]+=1
        else:
            d["False"]+=1

    return d


def sort(arr):
    once = True
    running = True
    while running:
        if once:
            display.draw("Count Sort", arr)
            result = count_sort(arr)
            once = False
            if result == -1:
                return -1

            if result == 0:
                pygame.draw.rect(WINDOW, COLOR['BLACK'], pygame.Rect(0, 603, 1300, 15))             
                result = display.result_screen()
                if result == -1:
                    return -1

                if result == 0:
                    running = False
                
                if result == 1:
                    print("redo not working")
                    running = False

        result = check_quit()
        if result == -1:
            return -1


    return 0



if __name__ == "__main__":
    values = [x for x in range(1,431)]
    random.shuffle(values)
    sort(values)
    # print(is_sorted(values))
    
        

    


