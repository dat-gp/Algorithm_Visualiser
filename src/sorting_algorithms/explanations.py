import pygame
from src.sorting_algorithms.constants import WINDOW, FONT, COLOR


def general():
    heading = FONT[30].render("General overview on Sorting Algorithms:-", 1, COLOR['WHITE'])
    
    Point_1 = FONT[25].render("- Sorting is a process of ordering a list of elements in either ascending or descending order.", 
    1, COLOR['WHITE'])
    
    Point_2 = FONT[25].render("- Categorized as:            1. Internal - Sorting takes place in the main memory",  1, COLOR['WHITE'])
    Point_2_a = FONT[25].render("a)", 1, COLOR['YELLOW'])
    Point_2_a1 = FONT[25].render("2. External - Sorting is carried out in secondary storage.", 1, COLOR['WHITE'])
    Point_2_b = FONT[25].render("b)", 1, COLOR['YELLOW'])
    Point_2_b1 = FONT[25].render("Sort Stability", 1, COLOR['WHITE'])
    Point_2_b_1 = FONT[25].render("1. Stable - Ex. Bubble, Selection, Insertion, Merge Sort", 1, COLOR['WHITE'])
    Point_2_b_2 = FONT[25].render("2. Unstable - Ex. Quick, Heap, Shell Sort", 1, COLOR['WHITE'])
    
    Point_3_1 = FONT[25].render("- Efficiency Analyzed over:   1. Best Case", 1, COLOR['WHITE'])
    Point_3_2 = FONT[25].render("2. Avg. Case", 1, COLOR['WHITE'])
    Point_3_3 = FONT[25].render("3. Worst Case", 1, COLOR['WHITE'])
    
    passes_point_1 = FONT[25].render("- Passes - Most algo. work in passes.", 1, COLOR['WHITE'])
    passes_point_2 = FONT[25].render("- In every pass, a number is placed at position where it will appear in the sorted list.", 1, COLOR['WHITE'])
    passes_point_3 = FONT[25].render("- Inside a pass a nmber is compared and positioned as reqd. by the algo.", 1, COLOR['WHITE'])

    WINDOW.blit(heading, (180,270))
    
    WINDOW.blit(Point_1, (200,310))

    WINDOW.blit(Point_2, (200,340))
    WINDOW.blit(Point_2_a, (377,340))
    WINDOW.blit(Point_2_a1, (400,362))
    WINDOW.blit(Point_2_b, (377,390))
    WINDOW.blit(Point_2_b1, (400,390))
    WINDOW.blit(Point_2_b_1, (400,415))
    WINDOW.blit(Point_2_b_2, (400,435))
    
    WINDOW.blit(Point_3_1, (200,475))
    WINDOW.blit(Point_3_2, (442,500))
    WINDOW.blit(Point_3_3, (442,525))

    WINDOW.blit(passes_point_1, (200,560))
    WINDOW.blit(passes_point_2, (273,580))
    WINDOW.blit(passes_point_3, (273,600))

    pygame.display.update()


def insertion_sort():
    WINDOW.blit()


def main():
    running = True
    while running:
        WINDOW.fill(COLOR['BLACK'])
        general()


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        
    pygame.quit()


if __name__ == "__main__":
    main()
