import pygame #импорт библиотеки


pygame.init() #инициализация библиотеки
screen = pygame.display.set_mode((306, 544)) #присваивание переменной screen значение размера окна
pygame.display.set_caption("Calculator warrior") #обозначение названия окна


bg_image = pygame.image.load('images/BG/BG.png') #присваивание переменной bg_image картинки заднего фона
button_1 = pygame.image.load('images/Buttons/Button_1.png') #присваивание переменной button_1 картинки кнопки 1


running = True #обьявление переменной обозначающей работу приложения
while running: #обьявление бесконечного цикла

    screen.blit(bg_image, (0, 0)) #добавление заднего фона на экранs
    screen.blit(button_1, (100, 100)) #добавление кнопки на экран

    pygame.display.update() #обновление экрана

    for event in pygame.event.get(): #цикл проверки ивентов
        if event.type == pygame.QUIT: #проверка нажатия кнопки закрыть на окне
            running = False #остановка бесконечного цикла
            pygame.quit() #окончание работы pygame