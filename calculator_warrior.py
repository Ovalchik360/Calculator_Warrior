import pygame


pygame.init()
screen = pygame.display.set_mode((302, 516))
pygame.display.set_caption("Calculator warrior")
bg_image = pygame.image.load("images\BG\BG.png")

running = True

while running:
    
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()