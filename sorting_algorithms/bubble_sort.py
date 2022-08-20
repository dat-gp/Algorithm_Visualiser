import pygame
import random
import display
from essentials import WINDOW, COLOR, FPS, FONT

# x coordinates
x = [x for x in range(4,1300,3)]

# clock object
clock = pygame.time.Clock()

def check_quit():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return -1
    
    return 0

def swap(a, b):
    temp = a
    a = b
    b = temp
    return a, b

def logic_loop(arr):
    compares = 0
    iterations = 0
    display.iterations(iterations)
    exp()
    for i in range(len(arr)-1):
        # clock.tick(FPS)
        for index in range(len(arr)-i-1):
            if arr[index]>arr[index+1]:
                
                arr[index], arr[index+1] = swap(arr[index],arr[index+1])
                compares+=1
                display.comparisons(compares)

                pygame.draw.line(WINDOW,COLOR['BLUE'], (x[index+1],600),(x[index+1],600-arr[index+1]))
                pygame.draw.line(WINDOW,COLOR['GREEN'], (x[index],600),(x[index],600-arr[index]))
                pygame.display.update()
                
                display.draw_lines(arr)
                result = check_quit()
                if result == -1:
                    return result
            
        iterations+=1
        display.iterations(iterations)

        # display.draw_lines(arr)
        pygame.display.update()

        result = check_quit()
        if result == -1:
            return result
        
    return 0

def exp():
    WINDOW.blit(FONT[25].render("Green, Blue flickering lines represent swaps between data elements.",1,COLOR['WHITE']), (0,650))


def sort(values):
    once = True
    running = True
    while running:
        clock.tick(FPS)

        if once:
            display.draw("Bubble Sort", values)
            result = logic_loop(values)
            once = False
            
            if result == -1:
                return -1
            
            if result == 0:
                result = display.result_screen()        # result screen
                if result == -1:                        # if back
                    return -1                    
                if result == 1:                         # if retry --> not working
                    print("Redo doesn't work")
                    once = True
                if result == 0:
                    return 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return -1

    return 0

if __name__ == "__main__":
    values = [x for x in range(1,431)]
    random.shuffle(values)
    sort(values)
    # print(len(values))
