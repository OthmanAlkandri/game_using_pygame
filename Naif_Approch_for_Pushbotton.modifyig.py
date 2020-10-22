# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 23:19:00 2020

@author: okand
"""


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
from pygame import mixer 
import time 

pygame.init()  # insslatize all pygame

"""" lad the mp3 files"""
#r= open("/Users/okand/Documents/school/code/pydub-master/wrong.wav",)
#s= open("/Users/okand/Documents/school/code/pydub-master/good_job.wav",)

# wrong = pygame.mixer.Sound("wrong.wav")

# right = pygame.mixer.Sound("good_job.wav")

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


def button(msg, x, y, w, h, ic, ac, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    # print (click)
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


""" This function is to print & display good job massege"""


def s2t():
    global screen
    gameDisplay.blit(Img, (0, 0))
    message_display("good job")
    print("good job")
    # mixer.init()
    # mixer.music.load ("myfile.mp3")
    # mixer.music.play()
    screen += 1


""" This function is to print & display Wrong massege"""


def st2():
    gameDisplay.blit(Img, (0, 0))
    message_display("wrong")
    print("wrong")
  #  pygame.mixer.Sound.play(right)
    # pygame.mixer.music.stop()


"""This function is for checing the value i  of the , changes the loaded picutres as well 
as the button options. to get the response s2t & st2 functions are called"""


def game():
    global screen
    # screen in range (0,2)
    screen +=1


"""" In The main function is to show the frist screen with 
two buttons options play or quit. if the user choes quit. the game will quit.
On the other hand, if the user choses to play button. it is going
 to take him 
to game function  """
def Img  (Img):
     Img =   pygame.image.load(os.path.join(image_path, "Lala_showerd.jpg"))
     gameDisplay.blit(Img, (0, 0))
     return (Img)
def main():
    NewRightButton = random.randint(1, 2)
    Zyaid = True
    global screen
    screen = 0
    while Zyaid:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        if screen==0:
            global Img
            Img (Img)
            
            button("Quit", 450, 450, 100, 50, red, bright_red, close)
            button("play", 150, 450, 100, 50, green, bright_green, game)
            pygame.display.update()
            

        elif screen==1:
            Img = pygame.image.load(os.path.join(image_path, "lalaa.jpg"))
            gameDisplay.blit(Img, (0, 0))

            if NewRightButton == 1:
                button("Dog", 150, 450, 100, 50, green, bright_green, s2t)
                button("Cat", 50, 450, 100, 50, blue, bright_bule, st2)
                button("Quit", 450, 450, 100, 50, red, bright_red, close)
                pygame.display.update()

            else:
                button("Cat", 150, 450, 100, 50, green, bright_green, st2)
                button("Dog", 50, 450, 100, 50, blue, bright_bule, s2t)
                button("Quit", 450, 450, 100, 50, red, bright_red, close)
                pygame.display.update()

        elif screen==2:
            Img = pygame.image.load(os.path.join(image_path, "Ross.jpg"))
            gameDisplay.blit(Img, (0, 0))

            if NewRightButton == 1:
                button("ross", 150, 450, 100, 50, green, bright_green, s2t)
                button("Cat", 50, 450, 100, 50, blue, bright_bule, st2)
                button("Quit", 450, 450, 100, 50, red, bright_red, close)
                pygame.display.update()
            else:
                button("Cat", 150, 450, 100, 50, green, bright_green, st2)
                button("ross", 50, 450, 100, 50, blue, bright_bule, s2t)
                button("Quit", 450, 450, 100, 50, red, bright_red, close)
                pygame.display.update()

        elif screen==3:
            Img = pygame.image.load(os.path.join(image_path, "gator.jpg"))
            gameDisplay.blit(Img, (0, 0))

            if NewRightButton == 1:
                button("gator", 150, 450, 100, 50, green, bright_green, s2t)
                button("Cat", 50, 450, 100, 50, blue, bright_bule, st2)
                button("Quit", 450, 450, 100, 50, red, bright_red, close)
                pygame.display.update()

            else:
                button("Cat", 150, 450, 100, 50, green, bright_green, st2)
                button("gator", 50, 450, 100, 50, blue, bright_bule, s2t)
                button("Quit", 450, 450, 100, 50, red, bright_red, close)
                pygame.display.update()

        elif screen==4:
            Img = pygame.image.load(os.path.join(image_path, "Lala_showerd.jpg"))
            gameDisplay.blit(Img, (0, 0))
            message_display("end of the game")
            button("Quit", 450, 450, 100, 50, red, bright_red, close)
            pygame.display.update()
            print("end of the game")

if __name__ == "__main__":
    main()
