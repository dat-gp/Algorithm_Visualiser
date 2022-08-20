# imports
import pygame
import random, time

import display
from essentials import FONT, WINDOW, COLOR

# pygame initialisation
pygame.init()


def disp_count(count):
    WINDOW.blit(FONT[25].render("Count = ", 1, COLOR['WHITE'], COLOR['BLACK']),(200,90))
    # x1 = 350
    # for i in range(20):
        # pygame.draw.line(WINDOW, COLOR['WHITE'], (x1, 80), (x1,110))
        # x1+=30

    x1 = 350
    for i in range(10):
        pygame.draw.line(WINDOW, COLOR['WHITE'], (x1,80), (x1+30,80))
        pygame.draw.line(WINDOW, COLOR['WHITE'], (x1,110), (x1+30,110))
        x1+=60

    x1 = 353
    for i in range(10):
        pygame.draw.rect(WINDOW, COLOR['BLACK'], pygame.Rect(x1-5,82,30,27))
        WINDOW.blit(FONT[20].render(f"{count[i]}", 1, COLOR['WHITE']), (x1, 90))
        x1+=60


def disp_empty_buckets():
    x1 = 353
    for i in range(10):
        pygame.draw.rect(WINDOW, COLOR['BLACK'], pygame.Rect(x1, 111, 25, 99))
        x1+=60


def disp_inbuckets(count):
    disp_empty_buckets()
    x = [x for x in range(363,963,60)]
    for i in range(len(count)):
        pygame.draw.line(WINDOW, COLOR['GREEN'], (x[i],209), (x[i], 209-count[i]), 5)
        i+=1


def disp_buckets():
    WINDOW.blit(FONT[25].render("Buckets:-", 1, COLOR['WHITE'], COLOR['BLACK']),(200, 180))                 # Buckets txt

    x1 = 350
    for i in range(20):                                                                                     # Drawing Buckets
        pygame.draw.line(WINDOW, COLOR['WHITE'], (x1, 150), (x1,230))       
        x1+=30

    # naming buckets with digits
    num = 0
    x1 = 360        
    for i in range(10):                                                                                     
        WINDOW.blit(FONT[20].render(f"{num}", 1, COLOR['WHITE'], COLOR['BLACK']), (x1,215))
        x1+=60
        num+=1

    # partition line in bukects (above numbers)
    x1 = 350
    for i in range(10):
        pygame.draw.line(WINDOW, COLOR['WHITE'], (x1,210),(x1+30,210))
        x1 += 60    
    
    pygame.display.update()


def disp_digit(divisor, passes):
    pygame.draw.rect(WINDOW, COLOR['BLACK'], pygame.Rect(400,30,270,30))

    WINDOW.blit(FONT[25].render(f"Total Passes = {passes}", 1, COLOR['WHITE']), (400,30))
    WINDOW.blit(FONT[25].render("Pass =", 1, COLOR['WHITE']), (600,30))
    WINDOW.blit(FONT[25].render(f"{len(str(divisor))}", 1, COLOR['GREEN']), (660,30))
    WINDOW.blit(FONT[25].render("Digit Place = ", 1, COLOR['WHITE']), (720,30))

    
    x1 = 770 + (50*passes)
    for i in range(passes):
        pygame.draw.line(WINDOW, COLOR["BLUE"], (x1, 45), (x1-20, 45))
        if i == (len(str(divisor))-1):
            pygame.draw.line(WINDOW, COLOR["GREEN"], (x1, 45), (x1-20, 45))
        
        x1-=30



def disp_copy_cursor(j):
    x = [x for x in range(4,1305,3)]
    pygame.draw.rect(WINDOW, COLOR['BLACK'], pygame.Rect(0, 260, 1300, 10))
    pygame.draw.line(WINDOW, COLOR['BLUE'], (x[j],260), (x[j],270))
    pygame.display.update()


def check_quit():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return -1

    return 0
    

def get_maxnum_digits(arr):
    max_num = arr[0]
    for num in arr:
        if num > max_num:
            max_num = num

    return len(str(max_num))


def radix_sort(arr, n): 
    passes = get_maxnum_digits(arr)                          # number of passes = number of digits in largest number

    divisor = 1
    
    i = 0
    while i<passes:                             
        disp_digit(divisor, passes)
        buckets = [[] for i in range(10)]                    # create buckets

        disp_buckets()
        
        # Initialise in buckets
        count = [0 for x in range(10)]

        disp_count(arr)
        pygame.display.update()
        x1 = 4
        for j in range(n):
            display.draw_lines(arr, y1=700)
            pygame.draw.line(WINDOW, COLOR['GREEN'], (x1, 700), (x1, 700-arr[j]))
            pygame.display.update()

            bucket_no = int((arr[j]/divisor)%10)
            buckets[bucket_no].append(arr[j])
            count[bucket_no]+=1

            disp_count(count)
            disp_inbuckets(count)
            pygame.display.update()

            j+=1
            x1+=3

            result = check_quit()
            if result == -1:
                return -1


        # copying back in main array
        j=0
        bucket_no = 0
        
        while bucket_no<10:
            for k in range(count[bucket_no]):
                arr[j] = buckets[bucket_no][k]
                k+=1
                j+=1
                count[bucket_no]-=1

                display.draw_lines(arr, y1=700)
                pygame.display.update()
                disp_copy_cursor(j)                
                disp_inbuckets(count)
                disp_count(count)
                pygame.display.update()

                result = check_quit()
                if result == -1:
                    return -1

            bucket_no+=1

            result = check_quit()
            if result == -1:
                return -1


        divisor*=10
        i+=1


        result = check_quit()
        if result == -1:
            return -1

    
    display.draw_lines(arr, y1=700)
    pygame.display.update()
    return 0


def sort(arr):
    n = len(arr)
    once = True
    running = True
    while running:
        if once:
            display.draw("Radix Sort", arr, y1=700)

            result = radix_sort(arr,n)
            once = False
            if result == -1:
                return -1

            if result == 0:
                display.draw("Radix Sort", arr)
                result = display.result_screen()
                if result == 0:
                    running = False
                if result == -1:
                    return -1
                if result == 1:
                    print("Redo not working")
                    running = False
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return -1

        
    return 0



if __name__ == "__main__":
    values = [x for x in range(1, 431)]
    sorted_list = sorted(values)
    random.shuffle(values)
    sort(values)


