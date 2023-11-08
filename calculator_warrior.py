import pygame
import sys
from button_1 import Button_1

def run():
    pygame.init()
    screen = pygame.display.set_mode((302, 516))
    pygame.display.set_caption("Calculator warrior")
    bg_image = pygame.image.load("images\BG\BG.png")
    button_1 = Button_1(screen)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
    
        screen.blit(bg_image, [0,0])
        button_1.output()
        pygame.display.flip()

run()