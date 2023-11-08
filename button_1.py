import pygame

class Button_1():

    def __init__(self, screen):
        #Инициализация кнопки

        self.screen = screen
        self.image = pygame.image.load('images\Buttons\Button_1.png')
        self.rect = pygame.Rect(16, 288, 50, 50)
        self.screen_rect = screen.get_rect()
        
    def output(self):
        #Рисование кнопки
        self.screen.blit(self.image, self.rect)
        