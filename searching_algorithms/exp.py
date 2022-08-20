import pygame
from essentials import WINDOW, WINDOW_HEIGHT, WINDOW_WIDTH, FONT, COLOR

# Explaination frame
FRAME = pygame.Rect(0,300,WINDOW_WIDTH,300)

def general():
    heading = FONT[30].render("General overview on Searching Algorithms:-", 1, COLOR['WHITE'])
    
    Point_1 = FONT[25].render("- Searching is a technique of finding an element (key) in a given list of elements.", 
    1, COLOR['WHITE'])
    
    Point_2 = FONT[25].render("- Searching technique should be able to locate an element as quickly and as effectively as possible.",  1, COLOR['WHITE'])
    
    Point_3 = FONT[25].render("- The complexity of any searching algorithm depends on the number of comparisons required to find the element.",1, COLOR['WHITE'])
    
    Point_3_new = FONT[25].render("  Performance of a searching algo. can be found by counting the number of comparisons reqd. in order to find the element.", 1, COLOR['WHITE'])
    
    WINDOW.blit(heading, (180,350))
    WINDOW.blit(Point_1, (200,390))
    WINDOW.blit(Point_2, (200,420))
    WINDOW.blit(Point_3, (200,450))
    WINDOW.blit(Point_3_new, (200,475))
    

def linear_search():
    pygame.draw.rect(WINDOW, COLOR['BLACK'], FRAME)

    heading = FONT[30].render("Linear / Sequential Search:-", 1, COLOR['WHITE'])
    
    point_1 = FONT[25].render("- In sequential search, elements in the list are examined sequentially (one-by-one) starting from the first element.", 1, COLOR['WHITE'])

    point_2 = FONT[25].render("- The process of searching terminates when either the list is exhausted or a comparison results in success.",  1, COLOR['WHITE'])

    time_complexity = FONT[25].render("- Time Complexity = O(n)               ... where n = number of comparions", 1, COLOR['WHITE'])
    time_complexity_new = FONT[25].render("  i.e. an element at ith index will need i comaprisons.", 1, COLOR['WHITE'])

    WINDOW.blit(heading, (180,350))
    WINDOW.blit(point_1, (200,390))
    WINDOW.blit(point_2, (200,420))
    WINDOW.blit(time_complexity, (200,455))
    WINDOW.blit(time_complexity_new, (200,480))

def binary_search():
    pygame.draw.rect(WINDOW, COLOR['BLACK'], FRAME)

    heading = FONT[30].render("Binary Search:-", 1, COLOR['WHITE'])
    
    point_1 = FONT[25].render("- In binary search, the search key is compared to the element that lies at the centre of the sorted list.", 1, COLOR['WHITE'])

    point_1_2 = FONT[25].render("- If  key < list[centre], then select the left half, Calculate the new centre in the left half.",  1, COLOR['WHITE'])
    point_1_3 = FONT[25].render("- If  key > list[centre], then select the right half, Calculate the new centre in the right half.",  1, COLOR['WHITE'])
    
    point_2 = FONT[25].render("- The above steps are executed until key == list[center].",  1, COLOR['WHITE'])

    point_3 = FONT[25].render("- This algo. follows the Divide and Conquer Approach and thus has lower complexity.",  1, COLOR['WHITE'])

    time_complexity = FONT[25].render("- Time Complexity:-", 1, COLOR['WHITE'])
    time_complexity_1 = FONT[25].render("- Worst Case = O(log2n)               ...where n = no. of comparisons ", 1, COLOR['WHITE'])
    time_complexity_2 = FONT[25].render("- Best Case = O(1)", 1, COLOR['WHITE'])

    WINDOW.blit(heading, (180,350))
    WINDOW.blit(point_1, (200,390))
    WINDOW.blit(point_1_2, (212,410))
    WINDOW.blit(point_1_3, (212,430))
    WINDOW.blit(point_2, (200,460))
    WINDOW.blit(point_3, (200,490))
    WINDOW.blit(time_complexity, (200,520))
    WINDOW.blit(time_complexity_1, (215,550))
    WINDOW.blit(time_complexity_2, (215,575))
