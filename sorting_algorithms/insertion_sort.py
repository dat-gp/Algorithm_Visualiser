import pygame
import random
import display
import time
from essentials import WINDOW, COLOR, FPS, FONT

pygame.init()

# delay 
delay = 0

# clock object
clock = pygame.time.Clock()

# x coordinates
x = [x for x in range(4,1300,3)]


def disp_selected(i, temp, delay):
    pygame.draw.rect(WINDOW, COLOR['BLACK'], pygame.Rect(0,100, 1305,30))
    WINDOW.blit(FONT[25].render(f"temp = {temp}", 1, COLOR['BLUE']),(x[i],100))
    pygame.draw.line(WINDOW, COLOR['BLUE'], (x[i], 600), (x[i], 600-temp))
    pygame.display.update()
    time.sleep(delay)


def disp_inserted(j, temp, delay):
    pygame.draw.rect(WINDOW, COLOR['BLACK'], pygame.Rect(0,100, 1305,30))
    WINDOW.blit(FONT[25].render(f"insert: {temp}", 1, COLOR['GREEN']), (x[j],100))
    pygame.draw.line(WINDOW, COLOR['GREEN'], (x[j+1], 600), (x[j+1], 600-temp))
    pygame.display.update()
    time.sleep(delay)



def underline_sec(i, delay):
    # Rendering black background for text
    pygame.draw.rect(WINDOW, COLOR['BLACK'],pygame.Rect(0,610,1300,20))                     # background
    
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


def highlight_line(j, arr, delay):
    pygame.draw.rect(WINDOW, COLOR['BLACK'], pygame.Rect(x[j],100, 100,30))
    pygame.draw.rect(WINDOW, COLOR['WHITE'], pygame.Rect(x[j],100, 45,20))
    WINDOW.blit(FONT[25].render(f"Shift", 1, COLOR['BLACK']), (x[(j)],100))
    pygame.draw.line(WINDOW, COLOR['BLUE'], (x[j],600), (x[j],600-arr[j]))
    pygame.display.update()

    if delay>0:
        time.sleep(0.1)
    


def disp_shift(arr, start, end, delay):
    
    pygame.draw.rect(WINDOW, COLOR['BLACK'], pygame.Rect(x[start],100, 100,30))         # background
    
    pygame.draw.rect(WINDOW, COLOR['WHITE'], pygame.Rect(x[start],100, 45,20))          # shift txt white back
    WINDOW.blit(FONT[25].render(f"Shift", 1, COLOR['BLACK']), (x[(start)],100))         # shift txt
    
    pygame.draw.rect(WINDOW, COLOR['BLACK'], pygame.Rect(0, 170, 1300, 430))

    index = 0
    (x1,y1) = (4,600)
    for value in arr:
        if start<index<end+1:
            pygame.draw.line(WINDOW, COLOR['BLUE'], (x1,y1), (x1,y1-value))
            index+=1
        else:
            pygame.draw.line(WINDOW, COLOR['RED'], (x1,y1), (x1,y1-value))
            index+=1
            
        x1+=3
    
    pygame.display.update()

    if delay!=0:
        time.sleep(delay+0.1)


# Delay Buttons

# for fast forwarding
button_1_txt = FONT[30].render("+",1,COLOR['BLACK'])
button_1 = pygame.Rect(600,650, 25, 25)

# for slowing
button_2_txt = FONT[30].render("-",1,COLOR['BLACK'])
button_2 = pygame.Rect(660,650, 25, 25)


def fast_slow(delay, condition=None):
    
    # Rendering Buttons
    pygame.draw.rect(WINDOW, COLOR['WHITE'], button_1)
    pygame.draw.rect(WINDOW, COLOR['WHITE'], button_2)
    
    # Rendering Texts on buttons
    WINDOW.blit(button_1_txt, (607,651))
    WINDOW.blit(button_2_txt, (669,652))
    
    # Rendering Delay Text
    delay_background = pygame.Rect(700,655,200,30)
    pygame.draw.rect(WINDOW,COLOR['BLACK'],delay_background)
    WINDOW.blit(FONT[25].render(f"Delay = {delay}", 1, COLOR['WHITE']), (700,660))
    pygame.display.update()
    
    delay_list = [0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]
    
    index = delay_list.index(delay) 
    
    if condition == 1:
        if index != 10:
            delay = delay_list[index+1]
    
    if condition == 2:    
        if index != 0:
            delay = delay_list[index-1]
    
    return delay


def insert_sort(arr, delay):
    for i in range(0,len(arr)):
        clock.tick(FPS)

        fast_slow(delay)                # Display delay buttons

        temp = arr[i]
        j = i-1

        disp_selected(i, temp, delay)               # Disp temp with blue line


        while temp < arr[j] and j>=0:
            if delay!=0:
                highlight_line(j, arr, delay)         
            
            # shifting 
            arr[j+1] = arr[j]
            j-=1

            result = check_quit()
            if result == -1:
                return -1
            
        arr[j+1] = temp

        if delay != 0: 
            disp_shift(arr, j+1, i, delay)
        
        disp_inserted(j, temp, delay)
        underline_sec(i, delay)
        display.draw_lines(arr)
        pygame.display.update()

        mx,my = pygame.mouse.get_pos()

        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return -1

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        if button_1.collidepoint((mx,my)):
            if click:
                delay = fast_slow(delay, 1)
        if button_2.collidepoint((mx,my)):
            if click:
                delay = fast_slow(delay, 2)

    return 0

def check_quit():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return -1

    return 0


def sort(values):
    once = True
    running = True
    while running:

        if once:
            display.draw("Insertion Sort", values)
            result = insert_sort(values, delay)                     # insertion sort function call

            once = False
            if result == -1:                           # quited mid execution of sort algo.
                return -1
            
            if result == 0:                            # execution complete of sort algo.
                
                result = display.result_screen()

                if result == -1:                       # quit
                    return -1

                if result == 0:                        # executed succesfully
                    return 0


        result = check_quit()
        if result == -1:
            return -1

    return 0
        
    



# if __name__ == "__main__":
#     values = [x for x in range(0,430)]
#     random.shuffle(values)
#     sort(values)

