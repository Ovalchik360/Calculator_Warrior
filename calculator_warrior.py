import pygame #импорт библиотеки


pygame.init() #инициализация библиотеки
screen = pygame.display.set_mode((306, 544)) #присваивание переменной screen значение размера окна
pygame.display.set_caption("Calculator warrior") #обозначение названия окна


bg_image = pygame.image.load('images/BG/BG.png') #присваивание картинки заднего фона
button_1 = pygame.image.load('images/Buttons/Button_1.png') #присваивание кнопок
button_2 = pygame.image.load('images/Buttons/Button_2.png')
button_3 = pygame.image.load('images/Buttons/Button_3.png') 
button_4 = pygame.image.load('images/Buttons/Button_4.png') 
button_5 = pygame.image.load('images/Buttons/Button_5.png') 
button_6 = pygame.image.load('images/Buttons/Button_6.png') 
button_7 = pygame.image.load('images/Buttons/Button_7.png') 
button_8 = pygame.image.load('images/Buttons/Button_8.png') 
button_9 = pygame.image.load('images/Buttons/Button_9.png') 
button_0 = pygame.image.load('images/Buttons/Button_0.png') 
button_On_Off = pygame.image.load('images/Buttons/Button_On-Off.png')
button_AC = pygame.image.load('images/Buttons/Button_AC.png')
button_plus = pygame.image.load('images/Buttons/Button_plus.png')
button_minus = pygame.image.load('images/Buttons/Button_minus.png')
button_divide = pygame.image.load('images/Buttons/Button_divide.png')
button_multiply = pygame.image.load('images/Buttons/Button_multiply.png')
button_equal = pygame.image.load('images/Buttons/Button_equal.png')
button_backspace = pygame.image.load('images/Buttons/Button_backspace.png')


screen.blit(bg_image, (0, 0)) #добавление заднего фона на экранs
screen.blit(button_1, (18, 309)) #добавление кнопок на экран
screen.blit(button_2, (73, 309))
screen.blit(button_3, (128, 309))
screen.blit(button_4, (18, 364))
screen.blit(button_5, (73, 364))
screen.blit(button_6, (128, 364))
screen.blit(button_7, (18, 419))
screen.blit(button_8, (73, 419))
screen.blit(button_9, (128, 419))
screen.blit(button_0, (73, 474))
screen.blit(button_On_Off, (18, 254))
screen.blit(button_AC, (73, 254))
screen.blit(button_plus, (183, 309))
screen.blit(button_minus, (183, 419))
screen.blit(button_divide, (238, 419))
screen.blit(button_multiply, (238, 309))
screen.blit(button_equal, (18, 474))
screen.blit(button_backspace, (128, 474))


running = True #обьявление переменной обозначающей работу приложения
while running: #обьявление бесконечного цикла

    Rectangles = [
    button_1.get_rect(),
    button_2.get_rect(),
    button_3.get_rect(),
    button_4.get_rect(),
    button_5.get_rect(),
    button_6.get_rect(),
    button_7.get_rect(),
    button_8.get_rect(),
    button_9.get_rect(),
    button_0.get_rect(),
    button_On_Off.get_rect(),
    button_AC.get_rect(),
    button_plus.get_rect(),
    button_minus.get_rect(),
    button_divide.get_rect(),
    button_multiply.get_rect(),
    button_equal.get_rect(),
    button_backspace.get_rect()
]

    pygame.display.update() #обновление экрана

    for event in pygame.event.get(): #цикл проверки ивентов
        if event.type == pygame.QUIT: #проверка нажатия кнопки закрыть на окне
            running = False #остановка бесконечного цикла
            pygame.quit() #окончание работы pygame
        if event.type == pygame.MOUSEBUTTONUP:
            mouse_pos = pygame.mouse.get_pos()
        