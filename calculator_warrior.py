import pygame #импорт библиотеки
from buttons import * #импорт всего из файла buttons
from arrows import *

pygame.init() #инициализация библиотеки

screen = pygame.display.set_mode((screen_width, screen_height)) #присваивание переменной screen значение размера окна
pygame.display.set_caption("Calculator warrior") #обозначение названия окна


bg_image = pygame.image.load('images/BG/BG.png') #присваивание картинки заднего фона
screen.blit(bg_image, (0, 0)) #добавление заднего фона на экран


running = True #обьявление переменной обозначающей работу приложения
while running: #обьявление бесконечного цикла

    #вызов функции отрисовки кнопок
    button_1.draw(button_1.pos_x, button_1.pos_y)
    button_2.draw(button_2.pos_x, button_2.pos_y)
    button_3.draw(button_3.pos_x, button_3.pos_y)
    button_4.draw(button_4.pos_x, button_4.pos_y)
    button_5.draw(button_5.pos_x, button_5.pos_y)
    button_6.draw(button_6.pos_x, button_6.pos_y)
    button_7.draw(button_7.pos_x, button_7.pos_y)
    button_8.draw(button_8.pos_x, button_8.pos_y)
    button_9.draw(button_9.pos_x, button_9.pos_y)
    button_0.draw(button_0.pos_x, button_0.pos_y)
    button_On_Off.draw(button_On_Off.pos_x, button_On_Off.pos_y)
    button_AC.draw(button_AC.pos_x, button_AC.pos_y)
    button_plus.draw(button_plus.pos_x, button_plus.pos_y)
    button_minus.draw(button_minus.pos_x, button_minus.pos_y)
    button_divide.draw(button_divide.pos_x, button_divide.pos_y)
    button_multiply.draw(button_multiply.pos_x, button_multiply.pos_y)
    button_equal.draw(button_equal.pos_x, button_equal.pos_y)
    button_backspace.draw(button_backspace.pos_x, button_backspace.pos_y)
    arrow.draw(arrow_pos[arrow_actual_pos][0], arrow_pos[arrow_actual_pos][1])

    if button_2.is_pressed == True:
        if arrow_actual_pos != 0:
            arrow_actual_pos = arrow_actual_pos - 1
        else:
            arrow_actual_pos = 5
        button_2.is_pressed = False

    if button_8.is_pressed == True:
        if arrow_actual_pos != 5:
            arrow_actual_pos = arrow_actual_pos + 1
        else:
            arrow_actual_pos = 0
        button_8.is_pressed = False

    pygame.display.update() #обновление экрана

    for event in pygame.event.get(): #цикл проверки ивентов
        if event.type == pygame.QUIT: #проверка нажатия кнопки закрыть на окне
            running = False #остановка бесконечного цикла
            pygame.quit() #окончание работы pygame
    