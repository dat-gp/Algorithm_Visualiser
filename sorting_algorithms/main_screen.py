# Imports
import pygame
import random
import info
import insertion_sort, bubble_sort, selection_sort
import quick_sort, count_sort, radix_sort
import shell_sort
from essentials import WINDOW, COLOR, FONT

# Initializations
pygame.init()

# button coordinates
button_1 = pygame.Rect(370, 100, 150, 40)
button_2 = pygame.Rect(370, 150, 150, 40)
button_3 = pygame.Rect(370, 200, 150, 40)

button_4 = pygame.Rect(575, 100, 150, 40)
button_5 = pygame.Rect(575, 150, 150, 40)
button_6 = pygame.Rect(575, 200, 150, 40)

button_7 = pygame.Rect(780, 100, 150, 40)

quit_button = pygame.Rect(600, 630, 100, 40)


def main_screen(values):
    running = True
    while running:
        WINDOW.fill(COLOR['BLACK'])

        # Rendering Heading
        WINDOW.blit(FONT[30].render('Sorting Algorithm', 1, COLOR['WHITE']), (560, 40))

        # Rendering buttons
        pygame.draw.rect(WINDOW, COLOR['WHITE'], button_1, border_radius= 3)
        pygame.draw.rect(WINDOW, COLOR['WHITE'], button_2, border_radius= 3)
        pygame.draw.rect(WINDOW, COLOR['WHITE'], button_3, border_radius= 3)
        pygame.draw.rect(WINDOW, COLOR['WHITE'], button_4, border_radius= 3)
        pygame.draw.rect(WINDOW, COLOR['WHITE'], button_5, border_radius= 3)
        pygame.draw.rect(WINDOW, COLOR['WHITE'], button_6, border_radius= 3)
        pygame.draw.rect(WINDOW, COLOR['WHITE'], button_7, border_radius= 3)
        pygame.draw.rect(WINDOW, COLOR['WHITE'], quit_button, border_radius= 3)

        # Rendering Texts on buttons
        WINDOW.blit(FONT[25].render("Insertion Sort", 1, COLOR['BLACK']), (385,113))
        WINDOW.blit(FONT[25].render("Bubble Sort", 1, COLOR['BLACK']), (395,163))
        WINDOW.blit(FONT[25].render("Selection Sort", 1, COLOR['BLACK']), (385,213))

        WINDOW.blit(FONT[25].render("Quick Sort", 1, COLOR['BLACK']), (607,112))
        WINDOW.blit(FONT[25].render("Counting Sort", 1, COLOR['BLACK']), (593,163))
        WINDOW.blit(FONT[25].render("Radix Sort", 1, COLOR['BLACK']), (607,213))
        
        WINDOW.blit(FONT[25].render("Shell Sort", 1, COLOR['BLACK']), (815,112))

        WINDOW.blit(FONT[30].render("Quit", 1, COLOR['BLACK']), (625, 640))
        info.general()  
        pygame.display.update()

        mx,my = pygame.mouse.get_pos()
    
        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
                    print(mx,my)

        if button_1.collidepoint((mx,my)):
            if click:
                random.shuffle(values)
                result = insertion_sort.sort(values)
                if result == -1:
                    running = False
                    
        
        if button_2.collidepoint((mx,my)):
            if click:
                random.shuffle(values)
                result = bubble_sort.sort(values)
                if result == -1:
                    running = False

        if button_3.collidepoint((mx,my)):
            if click:
                random.shuffle(values)
                result = selection_sort.sort(values)
                if result == -1:
                    running = False

        if button_4.collidepoint((mx,my)):
            if click:
                random.shuffle(values)
                result = quick_sort.sort(values)
                if result == -1:
                    running = False

        if button_5.collidepoint((mx,my)):
            if click:
                random.shuffle(values)
                result = count_sort.sort(values)
                if result == -1:
                    running = False

        if button_6.collidepoint((mx,my)):
            if click:
                random.shuffle(values)
                result = radix_sort.sort(values)
                if result == -1:
                    running = False
        
        if button_7.collidepoint((mx,my)):
            if click:
                random.shuffle(values)
                result = shell_sort.sort(values)
                if result == -1:
                    running = False

        if quit_button.collidepoint((mx,my)):
            if click:
                random.shuffle(values)
                running = False

    pygame.quit()


if __name__ == "__main__":
    values = [x for x in range(1,431)]
    main_screen(values)