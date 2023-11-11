import pygame #импорт библиотеки

screen_width = 306 #ширина экрана
screen_height = 544 #высота экрана
screen = pygame.display.set_mode((306, 544)) #обозначение экрана

class Button (): #создание класса кнопка

    def __init__ (self, x, y, button_height, button_width, image, image_pressed, is_pressed): #обозначение минимальных параметров кнопки
        self.pos_x = x
        self.pos_y = y
        self.button_height = button_height
        self.button_width = button_width
        self.image = image
        self.image_pressed = image_pressed
        self.is_pressed = is_pressed    

    def draw (self, x, y):  #функция отрисовки кнопки
        mouse_pos = pygame.mouse.get_pos()  #присвоение позиции мыши к переменной
        click = pygame.mouse.get_pressed()  #присвоение состояния мыши к переменной

        screen.blit(self.image, (self.pos_x, self.pos_y))   #отрисовка не нажатой кнопки

        if click[0] == 1:   #проверка нажата ли мышка
            if x < mouse_pos[0] < x + self.button_width:    #проверка положения курсора к кнопке по координате x
                if y < mouse_pos[1] < y + self.button_height:   #проверка положения курсора к кнопке по координате y
                    screen.blit(self.image_pressed, (self.pos_x, self.pos_y))   #отрисовка нажатой кнопки


#объявление кнопок
button_1 = Button(18, 309, 50, 50, pygame.image.load('images/Buttons/Button_1.png'), pygame.image.load('images/Buttons/Button_1_pressed.png'), False)
button_2 = Button(73, 309, 50, 50, pygame.image.load('images/Buttons/Button_2.png'), pygame.image.load('images/Buttons/Button_2_pressed.png'), False)
button_3 = Button(128, 309, 50, 50, pygame.image.load('images/Buttons/Button_3.png'), pygame.image.load('images/Buttons/Button_3_pressed.png'), False)
button_4 = Button(18, 364, 50, 50, pygame.image.load('images/Buttons/Button_4.png'), pygame.image.load('images/Buttons/Button_4_pressed.png'), False)
button_5 = Button(73, 364, 50, 50, pygame.image.load('images/Buttons/Button_5.png'), pygame.image.load('images/Buttons/Button_5_pressed.png'), False)
button_6 = Button(128, 364, 50, 50, pygame.image.load('images/Buttons/Button_6.png'), pygame.image.load('images/Buttons/Button_6_pressed.png'), False)
button_7 = Button(18, 419, 50, 50, pygame.image.load('images/Buttons/Button_7.png'), pygame.image.load('images/Buttons/Button_7_pressed.png'), False)
button_8 = Button(73, 419, 50, 50, pygame.image.load('images/Buttons/Button_8.png'), pygame.image.load('images/Buttons/Button_8_pressed.png'), False)
button_9 = Button(128, 419, 50, 50, pygame.image.load('images/Buttons/Button_9.png'), pygame.image.load('images/Buttons/Button_9_pressed.png'), False)
button_0 = Button(73, 474, 50, 50, pygame.image.load('images/Buttons/Button_0.png'), pygame.image.load('images/Buttons/Button_0_pressed.png'), False)
button_On_Off = Button(18, 254, 50, 50, pygame.image.load('images/Buttons/Button_On-Off.png'), pygame.image.load('images/Buttons/Button_On-Off_pressed.png'), False)
button_AC = Button(73, 254, 50, 50, pygame.image.load('images/Buttons/Button_AC.png'), pygame.image.load('images/Buttons/Button_AC_pressed.png'), False)
button_plus = Button(183, 309, 105, 50, pygame.image.load('images/Buttons/Button_plus.png'), pygame.image.load('images/Buttons/Button_plus_pressed.png'), False)
button_minus = Button(183, 419, 105, 50, pygame.image.load('images/Buttons/Button_minus.png'), pygame.image.load('images/Buttons/Button_minus_pressed.png'), False)
button_divide = Button(238, 419, 105, 50, pygame.image.load('images/Buttons/Button_divide.png'), pygame.image.load('images/Buttons/Button_divide_pressed.png'), False)
button_multiply = Button(238, 309, 105, 50, pygame.image.load('images/Buttons/Button_multiply.png'), pygame.image.load('images/Buttons/Button_multiply_pressed.png'), False)
button_equal = Button(18, 474, 50, 50, pygame.image.load('images/Buttons/Button_equal.png'), pygame.image.load('images/Buttons/Button_equal_pressed.png'), False)
button_backspace = Button(128, 474, 50, 50, pygame.image.load('images/Buttons/Button_backspace.png'), pygame.image.load('images/Buttons/Button_backspace_pressed.png'), False)