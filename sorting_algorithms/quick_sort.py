# Imports
import pygame
import random, time
import display
from essentials import WINDOW, COLOR, FONT

pygame.init()


# x coordinates
x = [x for x in range(4,1300,3)]

# Delay
delay = 0.2

# Frame below the lines, where naming is done
naming_frame = pygame.Rect(0,605,1300,44)


def disp_pivot(pivot_i, arr):
    pygame.draw.line(WINDOW, COLOR['GREEN'], (x[pivot_i],600), (x[pivot_i], 600-arr[pivot_i]))
    WINDOW.blit(FONT[20].render("pivot", 1, COLOR['GREEN']), (x[pivot_i]-5, 635))
    pygame.display.update()


def disp_i(i, arr, pivot_i):
    pygame.draw.rect(WINDOW, COLOR['BLACK'], naming_frame)                # Background

    display.draw_lines(arr)
    
    disp_pivot(pivot_i, arr)
    pygame.draw.line(WINDOW, COLOR['BLUE'], (x[i],605), (x[i],605+10))
    WINDOW.blit(FONT[20].render("i", 1, COLOR['WHITE']), (x[i],620))
    pygame.draw.line(WINDOW, COLOR['BLUE'], (x[i], 600), (x[i], 600-arr[i]))
    pygame.display.update()


def disp_j(j, arr, pivot_i, condition=0):
    if condition==0:
        pygame.draw.rect(WINDOW, COLOR['BLACK'], naming_frame)            # Background

    display.draw_lines(arr)

    pygame.draw.line(WINDOW, COLOR['BLUE'], (x[j],605), (x[j],605+10))
    disp_pivot(pivot_i, arr)
    WINDOW.blit(FONT[20].render("j", 1, COLOR['WHITE']), (x[j],620))
    pygame.draw.line(WINDOW, COLOR['BLUE'], (x[j], 600), (x[j], 600-arr[j]))
    pygame.display.update()


def disp_swap(a, b, arr, pivot_i, delay):
    pygame.draw.rect(WINDOW, COLOR['BLACK'], naming_frame)                # Bacground

    disp_i(a, arr, pivot_i)
    disp_j(b, arr, pivot_i, 1)
    pygame.draw.line(WINDOW, COLOR['WHITE'], (x[a+1],610), (x[b-1], 610))
    WINDOW.blit(FONT[20].render("swap", 1, COLOR['WHITE']), ((x[a]+x[b])//2, 620))
    pygame.display.update()
    if delay>0:
        time.sleep(0.1)


def check_quit():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return -1

    return 0


def partition(arr, l, u, delay):
    pivot = arr[l]
    i = l+1
    j = u

    while i<j:
        while i<=u and arr[i]<pivot:
            disp_i(i, arr, l)
            i+=1
            
            result = check_quit()
            if result == -1:
                return -1


        while j>=l and arr[j]>pivot:
            disp_j(j, arr, l)
            j-=1       

            result = check_quit()
            if result == -1:
                return -1


        if i<j:
            arr[i], arr[j] = arr[j], arr[i]
            display.draw_lines(arr)
            disp_swap(i, j, arr, l, delay)

    if j<i:
        display.draw_lines(arr)
        pygame.draw.rect(WINDOW, COLOR['BLACK'], naming_frame)                # Background
        pygame.draw.line(WINDOW, COLOR['GREEN'], (x[j],600), (x[j],600-arr[j]))
        pygame.draw.line(WINDOW, COLOR['GREEN'], (x[l],600), (x[l],600-arr[l]))

        arr[j], arr[l] = arr[l], arr[j]

        pygame.draw.line(WINDOW, COLOR['GREEN'], (x[l],605), (x[l],605+10))
        pygame.draw.line(WINDOW, COLOR['GREEN'], (x[j],610), (x[l],610))
        pygame.draw.line(WINDOW, COLOR['GREEN'], (x[j],605), (x[j],605+10))
        WINDOW.blit(FONT[20].render("swap", 1, COLOR['GREEN']), ((x[l]+x[j])//2, 620))
        pygame.display.update()

        if delay>0:
            time.sleep(0.5)

        display.draw_lines(arr)
        pygame.display.update()


    result = check_quit()
    if result == -1:
        print("last")
        return -1

    return j


def quick_sort(arr, l, u, delay):
    if l<u:
        j = partition(arr,l,u, delay)
        
        if j == -1:
            return -1

        result = quick_sort(arr, l, j-1, delay)
        if result == -1:
            return -1

        result = quick_sort(arr, j+1, u, delay)
        if result == -1:
            return -1


        display.draw_lines(arr)
        pygame.display.update()

    return 0


def sort(values):
    once = True
    running = True
    while running:
        
        if once:
            display.draw("Quick Sort", values)
            result = quick_sort(values, 0, len(values)-1, delay)
            once = False
            
            if result == -1:
                print("main loop")
                running = False

            if result == 0:
                pygame.draw.rect(WINDOW, COLOR['BLACK'], naming_frame)        # background

                result = display.result_screen()
                if result == -1:
                    return -1
                if result == 0:
                    return 0
                if result == 1:
                    print("redo not working")
                    # once = True
                    return 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return -1

    return 0


if __name__ == "__main__":    
    values = [x for x in range(0,431)]
    random.shuffle(values)
    sort(values)

