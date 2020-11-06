# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 17:15:42 2020
My code's functionality is when you run the code, a display screen 
will show up with two-button choices to either play or quit. 
If you choose to quit, you will exit the game. On the other hand, 
if you decided to play, you will be taken to another screen.
There is a serious of questions the user needs to answer.
On the other screen, there will be images shown with three buttons 
on each image. One button is to exit, second & third,
has either write or wrong answer choice 
@author: okand
"""

import pygame
import random  # we use this to make a random right button
import os
import sys
import time 

pygame.init()  # insslatize all pygame

"""" lad the mp3 files"""
"""" lad the mp3 files"""
Tiger= open("/Users/okand/Documents/school/code/ChoosingRightAnswer/Audio/Tiger.wav",)
circle= open("/Users/okand/Documents/school/code/ChoosingRightAnswer/Audio/Circle_Circulo.wav",)
#s= open("/Users/okand/Documents/school/code/Choosing_Right_Answer/tiger3.wav",)

Tiger = pygame.mixer.Sound(Tiger)
circle = pygame.mixer.Sound(circle)
#tiger3 = pygame.mixer.Sound("tiger3.wav")

"setting up the display parmeters"
display_width = 600
display_height = 600
"setting up the clors and the bright's"
black = (0, 0, 0)
alpha = (0, 88, 255)
white = (255, 255, 255)
red = (200, 0, 0)
green = (0, 200, 0)
blue = (0, 0, 255)
bright_red = (255, 0, 0)
bright_green = (0, 255, 0)
bright_bule = (0, 255, 0)


""""Setting display. note the starderd we use is 600*600 display limtation"""
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("guessing Game")  # title of the window
gameDisplay.fill(white)


""" Loading images to the paython from the pic file """
current_path = os.path.dirname(__file__)
image_path = os.path.join(current_path, "image")


def close():
    pygame.quit()
    sys.exit()


def message_display(text):
    largeText = pygame.font.Font("freesansbold.ttf", 30)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width / 2), (display_height / 2))
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()


def text_objects(text, font):
    textSurface = font.render(text, True, alpha)
    return textSurface, textSurface.get_rect()


""" This function is to set the button paramters x_axis Y_axis width hight 
Also, when you hit thr button it will take an action """


def button(msg, x, ic, ac, action=None):
    y =450;
    w=100;
    h=50;
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac, (x, y, w, h))

        if click[0] == 1 and action != None:
            action()
            pygame.time.wait(200)
    else:
        pygame.draw.rect(gameDisplay, ic, (x, y, w, h))

    smallText = pygame.font.SysFont("comicsansms", 20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ((x + (w / 2)), (y + (h / 2)))
    gameDisplay.blit(textSurf, textRect)


"""This function is for checing the value i  of the , changes the loaded picutres as well 
as the button options. to get the response s2t & st2 functions are called"""


""" This function is to print & display good job massege"""


def Check_right():
    global screen
    gameDisplay.blit(Img, (0, 0))
    message_display("good job")
    print("good job")
    screen += 1


""" This function is to print & display Wrong massege"""


def Check_wrong():
    gameDisplay.blit(Img, (0, 0))
    message_display("wrong")
    print("wrong")
  #  pygame.mixer.Sound.play(right)
    # pygame.mixer.music.stop()




""" This fuction is to take the screeen vaule from main fuction 
and increase it by one"""
def game():
    global screen
    screen +=1
    
    
""" This fuction is to take the screeenS vaule wich is equal to 4
    from main fuction  and increase it by one"""
def gameS():
    global screen
    screen = screenS +1
    
    
"""" In The main function is to show the frist screen with 
two buttons options play or quit. if the user choes quit. the game will quit.
On the other hand, if the user choses to play button. it is going
 to take him 
to game function  """

def main():
    NewRightButton = random.randint(1, 2)
    Zyaid = True
    global screen
    global screenS
    screen = 0
    screenS = 13
    while Zyaid:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        if screen==0 and screenS==13 :
            global Img
            Img =   pygame.image.load(os.path.join(image_path, "Lalaa.jpg"))
            gameDisplay.blit(Img, (0, 0))
            button("Quit", 450, red, bright_red, close)
            button("English", 150, green, bright_green, game)
            button("Spanish", 50, blue, bright_bule, gameS)
            pygame.display.update()

        elif screen==1:
            Img =   pygame.image.load(os.path.join(image_path, "tiger.jpg"))
            gameDisplay.blit(Img, (0, 0))
            pygame.mixer.Sound.play(Tiger)
            pygame.mixer.music.stop()
            time.sleep(3)
            if NewRightButton == 1:
                button("Tiger", 150,  green, bright_green, Check_right)
                button("Dog", 50, blue, bright_bule, Check_wrong)
                button("Quit", 450,  red, bright_red, close)
                pygame.display.update()

            else:
                button("Cat", 150,  green, bright_green, Check_wrong)
                button("Tiger", 50, blue, bright_bule, Check_right)
                button("Quit", 450,  red, bright_red, close)
                pygame.display.update()

        elif screen==2:
            Img =   pygame.image.load(os.path.join(image_path, "panda.jpg"))
            gameDisplay.blit(Img, (0, 0))
            if NewRightButton == 1:
                button("Panda", 150,  green, bright_green, Check_right)
                button("Fish", 50, blue, bright_bule, Check_wrong)
                button("Quit", 450,  red, bright_red, close)
                pygame.display.update()

            else:
                button("Fish", 150,  green, bright_green, Check_wrong)
                button("Panda", 50, blue, bright_bule, Check_right)
                button("Quit", 450,  red, bright_red, close)
                pygame.display.update()

        elif screen==3:
            Img =   pygame.image.load(os.path.join(image_path, "monkey.jpg"))
            gameDisplay.blit(Img, (0, 0))
            if NewRightButton == 1:
                button("Monkey", 150,  green, bright_green, Check_right)
                button("Duck", 50, blue, bright_bule, Check_wrong)
                button("Quit", 450,  red, bright_red, close)
                pygame.display.update()

            else:
                button("Duck", 150,  green, bright_green, Check_wrong)
                button("Monkey", 50, blue, bright_bule, Check_right)
                button("Quit", 450,  red, bright_red, close)
                pygame.display.update()
        elif screen==4:
            Img =   pygame.image.load(os.path.join(image_path, "cat.jpg"))
            gameDisplay.blit(Img, (0, 0))
            if NewRightButton == 1:
                button("Cat", 150,  green, bright_green, Check_right)
                button("Elephant", 50, blue, bright_bule, Check_wrong)
                button("Quit", 450,  red, bright_red, close)
                pygame.display.update()

            else:
                button("Elephant", 150,  green, bright_green, Check_wrong)
                button("Cat", 50, blue, bright_bule, Check_right)
                button("Quit", 450,  red, bright_red, close)
                pygame.display.update()
        elif screen==5:
            Img =   pygame.image.load(os.path.join(image_path, "blue.jpg"))
            gameDisplay.blit(Img, (0, 0))
            if NewRightButton == 1:
                button("Blue", 150,  green, bright_green, Check_right)
                button("White", 50, blue, bright_bule, Check_wrong)
                button("Quit", 450,  red, bright_red, close)
                pygame.display.update()

            else:
                button("White", 150,  green, bright_green, Check_wrong)
                button("Blue", 50, blue, bright_bule, Check_right)
                button("Quit", 450,  red, bright_red, close)
                pygame.display.update()
                
        elif screen==6:
            Img =   pygame.image.load(os.path.join(image_path, "yellow.jpg"))
            gameDisplay.blit(Img, (0, 0))
            if NewRightButton == 1:
                button("Yellow", 150,  green, bright_green, Check_right)
                button("Black", 50, blue, bright_bule, Check_wrong)
                button("Quit", 450,  red, bright_red, close)
                pygame.display.update()

            else:
                button("Black", 150,  green, bright_green, Check_wrong)
                button("Yellow", 50, blue, bright_bule, Check_right)
                button("Quit", 450,  red, bright_red, close)
                pygame.display.update()
        elif screen==7:
            Img =   pygame.image.load(os.path.join(image_path, "red.jpg"))
            gameDisplay.blit(Img, (0, 0))
            if NewRightButton == 1:
                button("red", 150,  green, bright_green, Check_right)
                button("pink", 50, blue, bright_bule, Check_wrong)
                button("Quit", 450,  red, bright_red, close)
                pygame.display.update()

            else:
                button("pink", 150,  green, bright_green, Check_wrong)
                button("red", 50, blue, bright_bule, Check_right)
                button("Quit", 450,  red, bright_red, close)
                pygame.display.update()
        elif screen==8:
            Img =   pygame.image.load(os.path.join(image_path, "green.jpg"))
            gameDisplay.blit(Img, (0, 0))
            if NewRightButton == 1:
                button("green", 150,  green, bright_green, Check_right)
                button("brown", 50, blue, bright_bule, Check_wrong)
                button("Quit", 450,  red, bright_red, close)
                pygame.display.update()

            else:
                button("Brown", 150,  green, bright_green, Check_wrong)
                button("green", 50, blue, bright_bule, Check_right)
                button("Quit", 450,  red, bright_red, close)
                pygame.display.update()
        elif screen==9:
            Img =   pygame.image.load(os.path.join(image_path, "heart.jpg"))
            gameDisplay.blit(Img, (0, 0))
            if NewRightButton == 1:
                button("Heart", 150,  green, bright_green, Check_right)
                button("Triangle", 50, blue, bright_bule, Check_wrong)
                button("Quit", 450,  red, bright_red, close)
                pygame.display.update()

            else:
                button("Triangle", 150,  green, bright_green, Check_wrong)
                button("Cubic", 50, blue, bright_bule, Check_right)
                button("Quit", 450,  red, bright_red, close)
                pygame.display.update()
        elif screen==10:
            Img =   pygame.image.load(os.path.join(image_path, "square.jpg"))
            gameDisplay.blit(Img, (0, 0))
            if NewRightButton == 1:
                button("Square", 150,  green, bright_green, Check_right)
                button("Cubic", 50, blue, bright_bule, Check_wrong)
                button("Quit", 450,  red, bright_red, close)
                pygame.display.update()

            else:
                button("Black", 150,  green, bright_green, Check_wrong)
                button("Square", 50, blue, bright_bule, Check_right)
                button("Quit", 450,  red, bright_red, close)
                pygame.display.update()
        elif screen==11:
            Img =   pygame.image.load(os.path.join(image_path, "triangle.jpg"))
            gameDisplay.blit(Img, (0, 0))
            if NewRightButton == 1:
                button("Triangle", 150,  green, bright_green, Check_right)
                button("Cylinder", 50, blue, bright_bule, Check_wrong)
                button("Quit", 450,  red, bright_red, close)
                pygame.display.update()

            else:
                button("Cylinder", 150,  green, bright_green, Check_wrong)
                button("Triangle", 50, blue, bright_bule, Check_right)
                button("Quit", 450,  red, bright_red, close)
                pygame.display.update()
        elif screen==12:
            Img =   pygame.image.load(os.path.join(image_path, "circle.jpg"))
            gameDisplay.blit(Img, (0, 0))
            if NewRightButton == 1:
                button("Circle", 150,  green, bright_green, Check_right)
                button("Cubick", 50, blue, bright_bule, Check_wrong)
                button("Quit", 450,  red, bright_red, close)
                pygame.display.update()

            else:
                button("Cubic", 150,  green, bright_green, Check_wrong)
                button("Circle", 50, blue, bright_bule, Check_right)
                button("Quit", 450,  red, bright_red, close)
                pygame.display.update()
        elif screen==13:
            Img = pygame.image.load(os.path.join(image_path, "Lala_showerd.jpg"))
            gameDisplay.blit(Img, (0, 0))
            message_display("end of the game")
            button("Quit", 450, red, bright_red, close)
            pygame.display.update()
            print("end of the game")
          
            """ here is the spanish language """
        elif screen== 14:
            Img = pygame.image.load(os.path.join(image_path, "tiger.jpg"))
            gameDisplay.blit(Img, (0, 0))
            if NewRightButton == 1:
                button("Tigre", 150,  green, bright_green, Check_right)
                button("Perro", 50, blue, bright_bule, Check_wrong)
                button("Quit", 450,  red, bright_red, close)
                pygame.display.update()
            else:
                button("Perro", 50, blue, bright_bule, Check_wrong)
                button("Tigre", 50, blue, bright_bule, Check_right)
                button("Quit", 450,  red, bright_red, close)
                pygame.display.update()

        elif screen==15:
            Img =   pygame.image.load(os.path.join(image_path, "panda.jpg"))
            gameDisplay.blit(Img, (0, 0))
            if NewRightButton == 1:
                button("Oso", 150,  green, bright_green, Check_right)
                button("Fish", 50, blue, bright_bule, Check_wrong)
                button("Quit", 450,  red, bright_red, close)
                pygame.display.update()

            else:
                button("Fish", 150,  green, bright_green, Check_wrong)
                button("Oso", 50, blue, bright_bule, Check_right)
                button("Quit", 450,  red, bright_red, close)
                pygame.display.update()

        elif screen==16:
            Img =   pygame.image.load(os.path.join(image_path, "monkey.jpg"))
            gameDisplay.blit(Img, (0, 0))
            if NewRightButton == 1:
                button("Mono", 150,  green, bright_green, Check_right)
                button("Duck", 50, blue, bright_bule, Check_wrong)
                button("Quit", 450,  red, bright_red, close)
                pygame.display.update()

            else:
                button("Duck", 150,  green, bright_green, Check_wrong)
                button("Mono", 50, blue, bright_bule, Check_right)
                button("Quit", 450,  red, bright_red, close)
                pygame.display.update()
        elif screen==17:
            Img =   pygame.image.load(os.path.join(image_path, "cat.jpg"))
            gameDisplay.blit(Img, (0, 0))
            if NewRightButton == 1:
                button("Gato", 150,  green, bright_green, Check_right)
                button("Elephant", 50, blue, bright_bule, Check_wrong)
                button("Quit", 450,  red, bright_red, close)
                pygame.display.update()

            else:
                button("Elephant", 150,  green, bright_green, Check_wrong)
                button("Gato", 50, blue, bright_bule, Check_right)
                button("Quit", 450,  red, bright_red, close)
                pygame.display.update()
        elif screen==18:
            Img =   pygame.image.load(os.path.join(image_path, "blue.jpg"))
            gameDisplay.blit(Img, (0, 0))
            if NewRightButton == 1:
                button("Azul", 150,  green, bright_green, Check_right)
                button("White", 50, blue, bright_bule, Check_wrong)
                button("Quit", 450,  red, bright_red, close)
                pygame.display.update()

            else:
                button("White", 150,  green, bright_green, Check_wrong)
                button("Azul", 50, blue, bright_bule, Check_right)
                button("Quit", 450,  red, bright_red, close)
                pygame.display.update()
                
        elif screen==19:
            Img =   pygame.image.load(os.path.join(image_path, "yellow.jpg"))
            gameDisplay.blit(Img, (0, 0))
            if NewRightButton == 1:
                button("Amarillo", 150,  green, bright_green, Check_right)
                button("Black", 50, blue, bright_bule, Check_wrong)
                button("Quit", 450,  red, bright_red, close)
                pygame.display.update()

            else:
                button("Black", 150,  green, bright_green, Check_wrong)
                button("Amarillo", 50, blue, bright_bule, Check_right)
                button("Quit", 450,  red, bright_red, close)
                pygame.display.update()
        elif screen==20:
            Img =   pygame.image.load(os.path.join(image_path, "red.jpg"))
            gameDisplay.blit(Img, (0, 0))
            if NewRightButton == 1:
                button("Rojo", 150,  green, bright_green, Check_right)
                button("pink", 50, blue, bright_bule, Check_wrong)
                button("Quit", 450,  red, bright_red, close)
                pygame.display.update()

            else:
                button("pink", 150,  green, bright_green, Check_wrong)
                button("Rojo", 50, blue, bright_bule, Check_right)
                button("Quit", 450,  red, bright_red, close)
                pygame.display.update()
        elif screen==21:
            Img =   pygame.image.load(os.path.join(image_path, "green.jpg"))
            gameDisplay.blit(Img, (0, 0))
            if NewRightButton == 1:
                button("Verde", 150,  green, bright_green, Check_right)
                button("brown", 50, blue, bright_bule, Check_wrong)
                button("Quit", 450,  red, bright_red, close)
                pygame.display.update()

            else:
                button("Brown", 150,  green, bright_green, Check_wrong)
                button("Verde", 50, blue, bright_bule, Check_right)
                button("Quit", 450,  red, bright_red, close)
                pygame.display.update()
        elif screen==22:
            Img =   pygame.image.load(os.path.join(image_path, "heart.jpg"))
            gameDisplay.blit(Img, (0, 0))
            if NewRightButton == 1:
                button("Corazon", 150,  green, bright_green, Check_right)
                button("Triangulo", 50, blue, bright_bule, Check_wrong)
                button("Quit", 450,  red, bright_red, close)
                pygame.display.update()

            else:
                button("Triangulo", 150,  green, bright_green, Check_wrong)
                button("Corazon", 50, blue, bright_bule, Check_right)
                button("Quit", 450,  red, bright_red, close)
                pygame.display.update()
        elif screen==23:
            Img =   pygame.image.load(os.path.join(image_path, "square.jpg"))
            gameDisplay.blit(Img, (0, 0))
            if NewRightButton == 1:
                button("Cuadrodo", 150,  green, bright_green, Check_right)
                button("Cubico", 50, blue, bright_bule, Check_wrong)
                button("Quit", 450,  red, bright_red, close)
                pygame.display.update()

            else:
                button("Cubico", 150,  green, bright_green, Check_wrong)
                button("Cuadrodo", 50, blue, bright_bule, Check_right)
                button("Quit", 450,  red, bright_red, close)
                pygame.display.update()
        elif screen==24:
            Img =   pygame.image.load(os.path.join(image_path, "triangle.jpg"))
            gameDisplay.blit(Img, (0, 0))
            if NewRightButton == 1:
                button("Triangulo", 150,  green, bright_green, Check_right)
                button("Cilindro", 50, blue, bright_bule, Check_wrong)
                button("Quit", 450,  red, bright_red, close)
                pygame.display.update()

            else:
                button("Cilindro", 150,  green, bright_green, Check_wrong)
                button("Triangulo", 50, blue, bright_bule, Check_right)
                button("Quit", 450,  red, bright_red, close)
                pygame.display.update()
        elif screen==25:
            Img =   pygame.image.load(os.path.join(image_path, "circle.jpg"))
            gameDisplay.blit(Img, (0, 0))
            if NewRightButton == 1:
                button("Circulo", 150,  green, bright_green, Check_right)
                button("Cubico", 50, blue, bright_bule, Check_wrong)
                button("Quit", 450,  red, bright_red, close)
                pygame.display.update()

            else:
                button("Cubico", 150,  green, bright_green, Check_wrong)
                button("Circulo", 50, blue, bright_bule, Check_right)
                button("Quit", 450,  red, bright_red, close)
                pygame.display.update()
        elif screen==26:
            Img = pygame.image.load(os.path.join(image_path, "Lala_showerd.jpg"))
            gameDisplay.blit(Img, (0, 0))
            message_display("end of the game")
            button("Quit", 450, red, bright_red, close)
            pygame.display.update()
            print("end of the game")
            

if __name__ == "__main__":
    main()
