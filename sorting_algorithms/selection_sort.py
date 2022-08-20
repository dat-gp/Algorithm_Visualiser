# imports
import pygame
import random, time
import display
from essentials import WINDOW, COLOR, FPS, FONT

# delay 
delay = 0

# x coordinates
x = [x for x in range(4,1300,3)]

#clock object
clock = pygame.time.Clock()

def check_quit():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return -1
    
    return 0

def swap(a,b):
    temp = a
    a = b
    b = temp
    return a, b


def disp_min(i_min):
    pygame.draw.rect(WINDOW, COLOR['BLACK'], pygame.Rect(0,625, 1300, 100))
    pygame.draw.line(WINDOW, COLOR['WHITE'], (x[i_min], 625), (x[i_min],645))
    WINDOW.blit(FONT[20].render("min.",1, COLOR['BLUE']), (x[i_min]-10, 647))
    pygame.display.update()


def disp_swap(i_min, i, delay):
    pygame.draw.line(WINDOW, COLOR['WHITE'], (x[i_min], 635), (x[i], 635))
    pygame.draw.line(WINDOW, COLOR['WHITE'], (x[i], 625), (x[i], 645))
    WINDOW.blit(FONT[25].render("i",1, COLOR['GREEN'], COLOR['BLACK']), (x[i]-1, 647))

    dist = int((x[i_min]+x[i])/2)
    WINDOW.blit(FONT[20].render('swap',1,COLOR['WHITE']), (dist-25, 645))

    pygame.display.update()
    time.sleep(delay)


def logic_loop(arr, delay):
    compares = 0
    iterations = 0
    for i in range(len(arr)-1):
        clock.tick(FPS)
        i_min = i                       # index of minimum number
        for j in range(i+1, len(arr)):
            
            pygame.draw.rect(WINDOW, COLOR['BLACK'], pygame.Rect(0,625, 1300, 100))
            if delay != 0:
                pygame.draw.line(WINDOW,COLOR['BLACK'], (x[j],600), (x[j], 600-arr[j]))
                pygame.display.update()
                pygame.draw.line(WINDOW,COLOR['RED'], (x[j],600), (x[j], 600-arr[j]))
                pygame.display.update()
                        
            if arr[j]<arr[i_min]:
                i_min = j
            
            compares += 1
            display.comparisons(compares)

            result = check_quit()
            if result == -1:
                return -1

        display.draw_lines(arr)
        pygame.draw.line(WINDOW, COLOR['BLUE'], (x[i_min],600), (x[i_min], 600-arr[i_min]))
        disp_min(i_min)
        pygame.display.update()
        time.sleep(delay)

        if i_min != i:                                                  # swap
            arr[i], arr[i_min] = swap(arr[i], arr[i_min])
            
            pygame.draw.line(WINDOW,COLOR['GREEN'], (x[i],600), (x[i], 600-arr[i]))
            disp_swap(i_min, i, delay)
            pygame.display.update()
            time.sleep(delay)

        display.underline_sec(i, x)
        display.draw_lines(arr)
        pygame.display.update()

        iterations += 1
        display.iterations(iterations)
        result = check_quit()
        if result == -1:
            return -1

    return 0



def sort(values):
    once = True
    running = True
    while running:
        clock.tick(FPS)
        
        if once:
            display.draw("Selection Sort", values)
            result = logic_loop(values, delay)
            once = False
            
            if result == -1:
                return -1

            if result == 0:
                pygame.draw.rect(WINDOW, COLOR['BLACK'], pygame.Rect(0,625, 1300, 100))
                result = display.result_screen()
                if result == -1:
                    return -1
                if result == 1:
                    print("Redo Not Running")
                    once = False
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
