import pygame

screen_width = 306 #ширина экрана
screen_height = 544 #высота экрана
screen = pygame.display.set_mode((306, 544)) #обозначение экрана

arrow_actual_pos = 0

arrow_pos = [
    (22, 45),
    (22, 69),
    (22, 93),
    (22, 141),
    (22, 165),
    (22, 189)
]


class arrows():

    def __init__ (self, x, y, image):
        self.pos_x = x
        self.pos_y = y
        self.image = image

    def draw (self, x, y):
        screen.blit(self.image, (x, y))



arrow = arrows(arrow_pos[0][0], arrow_pos[0][1], pygame.image.load('images/UI/arrow.png'))