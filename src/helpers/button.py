'''
Button Class 
- Button animation
- Displays description of button (if any)
- Returns true if button clicked
'''

# Imports
import pygame
import src.searching_algorithms.explanations 
from src.helpers.constants import WINDOW, COLOR, FONT, FPS

# Pygame Initialisation
pygame.init()
clock = pygame.time.Clock()

class Button:
    def __init__(self, text: str, pos: tuple, width:int, height:int, disp_explanation=src.searching_algorithms.explanations.none, elevation=4):
        # core attr.
        self.pressed = False
        self.elevation = elevation
        self.dynamic_elevation = elevation
        self.original_y_pos = pos[1]

        # top rectangle
        self.top_rect = pygame.Rect(pos, (width, height))
        self.top_rect_color = COLOR['WHITE']

        # bottom_rectangle
        self.bottom_rect = pygame.Rect(pos, (width, elevation))
        self.bottom_rect_color = COLOR['GREY']

        # texts
        self.text_surface = FONT[25].render(text, 1, COLOR["BLACK"])
        self.text_rect = self.text_surface.get_rect(center = self.top_rect.center)

        # exp
        self.disp_explanation = disp_explanation

    def draw(self):
        # elevation logic
        self.top_rect.y = self.original_y_pos-self.dynamic_elevation
        self.text_rect.center = self.top_rect.center
        
        self.bottom_rect.midtop = self.top_rect.midtop
        self.bottom_rect.height = self.top_rect.height+self.dynamic_elevation


        pygame.draw.rect(WINDOW, self.bottom_rect_color, self.bottom_rect, border_radius = 3)
        pygame.draw.rect(WINDOW, self.top_rect_color, self.top_rect, border_radius = 3)
        WINDOW.blit(self.text_surface, self.text_rect)
        clicked = self.check_click()
        if clicked:
            return True

    def check_click(self):
        # gets mouse position
        mx, my = pygame.mouse.get_pos()
        # checks if the mouse is hovering over the button 
        if self.top_rect.collidepoint((mx,my)):
            self.top_rect_color = COLOR["GREEN"]
            self.bottom_rect_color = COLOR["DARK GREEN"]
            self.disp_explanation()

            # checks if the user pressed the left mouse button
            if pygame.mouse.get_pressed()[0]:
                self.dynamic_elevation = 0
                # if pressed, the attribute is set to true
                self.pressed = True
            # checks if the user has pressed the button but not is not pressing it anymore
            else:
                self.dynamic_elevation = self.elevation
                # checks if the user has pressed the button and the attr. is true
                if self.pressed == True:
                    # set the attr. back to false
                    self.pressed = False            
                    
                    # return clicked
                    return True            
        # if the mouse not hovering on the button
        else:    
            self.dynamic_elevation = self.elevation
            self.top_rect_color = COLOR["WHITE"]
            self.bottom_rect_color = COLOR["GREY"]
            

# button1 = Button("Click Me", (580,300), 210, 50)

# def main():
#     running = True
#     while running:
#         WINDOW.fill(COLOR["BLACK"])
#         button1.draw()

#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 running = False

#         pygame.display.update()

#     pygame.quit()

# if __name__ == "__main__":
#     main()

