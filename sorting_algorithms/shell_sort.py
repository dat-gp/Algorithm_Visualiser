import pygame
import random, time
import display
from essentials import WINDOW, FONT, COLOR

# initilization
pygame.init()

# list of x coordinates of red lines
x = [x for x in range(4,1300,3)]


# Delay
delay = 0


def disp_currentlines(arr, j, step):
    pygame.draw.rect(WINDOW, COLOR['BLACK'], pygame.Rect(0, 601, 1300, 100))

    # Blue lines 
    pygame.draw.line(WINDOW, COLOR['BLUE'], (x[j],600), (x[j], 600-arr[j]))                     # j 
    pygame.draw.line(WINDOW, COLOR['BLUE'], (x[j-step],600), (x[j-step], 600-arr[j-step]))      # j-step

    # Arrows
    pygame.draw.line(WINDOW, COLOR['BLUE'], (x[j],602), (x[j], 618))                            
    pygame.draw.line(WINDOW, COLOR['BLUE'], (x[j-step],602), (x[j-step], 618))            
    
    # Texts
    WINDOW.blit(FONT[20].render("j", 1, COLOR['BLUE']), (x[j]-1,623))
    WINDOW.blit(FONT[20].render("j-step", 1, COLOR['BLUE']), (x[j-step]-13,623))

    pygame.display.update()


def check_quit():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return -1
    return 0


def disp_swap(a, b):
    pygame.draw.line(WINDOW, COLOR['WHITE'], (x[a]-1,610), (x[b]+1,610))
    WINDOW.blit(FONT[20].render("swap", 1, COLOR['WHITE']), ((x[a]+x[b])//2,613))
    pygame.display.update()


def disp_step(step):    
    # step = {step}  text
    pygame.draw.rect(WINDOW, COLOR['BLACK'], pygame.Rect(567, 50, 170, 50))
    WINDOW.blit(FONT[25].render("Step / Gap: ", 1, COLOR['WHITE']), (585,50))
    WINDOW.blit(FONT[25].render(f"{step}", 1, COLOR['GREEN']), (685,50))
    
    # step = n/2 = {n}/2   text
    WINDOW.blit(FONT[25].render(f"Step = n/2 =", 1, COLOR['WHITE']), (567,80))
    WINDOW.blit(FONT[25].render(f"{step*2}", 1, COLOR['GREEN']), (674,80))
    WINDOW.blit(FONT[25].render(f"/ 2", 1, COLOR['WHITE']), (709,80))

    pygame.display.update()


def shell_sort(arr, n):
    step = n//2
    while step>0:
        disp_step(step)
        for i in range(step, n):
            temp = arr[i]
            j = i
            
            while j>=step:
                disp_currentlines(arr, j, step)

                if temp < arr[j-step]:
                    arr[j] = arr[j-step]
                    
                    if delay>0:
                        disp_swap(j, j-step)
                        time.sleep(delay)
                else:
                    break
                
                j = j-step

                display.draw_lines(arr)
                pygame.display.update()

                result = check_quit()
                if result == -1:
                    return -1

            arr[j] = temp

            i+=1
            display.draw_lines(arr)
            pygame.display.update()
            result = check_quit()
            if result == -1:
                return -1

        step = step//2
        result = check_quit()
        if result == -1:
            return -1

    return 0


def sort(arr):
    once = True
    running = True
    while running:
        if once:
            display.draw("Shell Sort", arr)
            result = shell_sort(arr, len(arr))
            once = False
            if result == -1:
                return -1

            if result == 0:
                pygame.draw.rect(WINDOW, COLOR['BLACK'], pygame.Rect(567, 50, 170, 50))
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



def is_sorted(arr, sorted_list):
    flag = {"True" : 0, 
            "False": 0}

    for i in range(len(arr)):
        if arr[i] == sorted_list[i]:
            flag["True"]+=1
        else:
            flag["False"]+=1

    return flag




if __name__ == "__main__":
    values = [x for x in range(1, 431)]
    random.shuffle(values)
    sorted_list = sorted(values)
    sort(values)
    print(is_sorted(values, sorted_list))
