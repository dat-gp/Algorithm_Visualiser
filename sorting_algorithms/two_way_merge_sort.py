import pygame
import random
import display
from essentials import WINDOW, COLOR


pygame.init()

# Frames in which lines reside
FRAME = pygame.Rect(0, 150, 1300, 450)


def check_quit():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return -1
        
    return 0


def disp_sec(arr, i, j):
    mid = (i+j)//2

    running = True
    while running:
    
        pygame.draw.rect(WINDOW, COLOR['WHITE'], FRAME)
        disp_dots(arr)
        for i in range(4,1300,3):
            if i<mid:
                pygame.draw.line(WINDOW, COLOR['BLUE'], (i,))
    
    


def disp_dots(arr):
    x = 4
    for i in range(len(arr)):
        pygame.draw.line(WINDOW, COLOR['RED'], (x, 150), (x, 153))
        
        result = check_quit()
        if result == -1:
            return -1

        x+=3

    return 0


def animate_up():
    i = 0 
    while i < 21:
        pygame.draw.rect(WINDOW, COLOR['BLACK'], pygame.Rect(0, 130, 1300, i))          # down
        i+=1
       
        result = check_quit()
        if result == -1:
            return -1

        pygame.display.update()        
    

    j = 601
    while j > 153:
        pygame.draw.rect(WINDOW, COLOR['BLACK'], pygame.Rect(0, j, 1300, 601-j))          # up
        j-=1
        result = check_quit()
        if result == -1:
            return -1

        pygame.display.update()        
    

    return 0
    
def sort(arr):
    running = True
    while running:
        
        result = display.disp_under_construction("Two-Way Merge Sort")
        if result == -1:
            return -1
        if result == 0:
            running = False
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return -1

    return 0

def main():
    once = True
    running = True
    while running:

        if once:
            display.draw("Two Way Merge Sort", values)
            result = disp_dots(values)
            result1 = animate_up()
            pygame.display.update()
            once = False

            if result == -1:
                running = False
            
            if result1 == -1:
                running = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.quit()


if __name__ == "__main__":
    values = [x for x in range(1, 431)]
    random.shuffle(values)
    # main()
    sort(values)
