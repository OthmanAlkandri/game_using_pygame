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
import random #we use this to make a random right button
import os 
import sys 
pygame.init() # insslatize all pygame 



"setting up the display parmeters"
display_width = 600
display_height = 600

"setting up the clors and the bright's"
black = (0,0,0)
alpha = (0,88,255)
white = (255,255,255)
red = (200,0,0)
green = (0,200,0)
blue = (0, 0, 255)
bright_red = (255,0,0)
bright_green = (0,255,0)
bright_bule = (0,255,0)


""""Setting display. note the starderd we use is 600*600 display limtation"""
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('guessing Game') #title of the window
gameDisplay.fill(white)


""" Loading images to the paython from the pic file """
current_path = os.path.dirname(__file__)

image_path = os.path.join('image')
def load_the_image(image):
    images = [
        load_the_image('lalaa.jpg'),
        load_the_image('Ross.jpg'),
        load_the_image('gator.jpg'),
        load_the_image('blue_sea_water.jpg'),
        load_the_image('mountains.jpg'),
        load_the_image('elif.jpg'),
        load_the_image('Lala_showerd.jpg')
   ]
    # for carImg in carImg :
    #     carImg [ ] = pygame.image.load(os.path.join(im, 'Lala_showerd.jpg'))

def close():
    pygame.quit()
    sys.exit()

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',30)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()
    

    
def text_objects(text, font):
    textSurface = font.render(text, True, alpha)
    return textSurface, textSurface.get_rect()




""" This function is to set the button paramters x_axis Y_axis width hight 
Also, when you hit thr button it will take an action """
def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    # print (click)
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac,(x,y,w,h))

        if click[0] == 1 and action != None:
            action()         
    else:
        pygame.draw.rect(gameDisplay, ic,(x,y,w,h))

    smallText = pygame.font.SysFont("comicsansms",20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    gameDisplay.blit(textSurf, textRect)


    
""" This function is to print & display good job massege"""
def s2t(): 
    gameDisplay.blit(carImg,(0,0))    
    message_display('good job')
    print('good job')

""" This function is to print & display Wrong massege"""  
def st2():
    gameDisplay.blit(carImg,(0,0))  
    message_display('wrong')
    print('wrong')   

"""This function is for checing the value i  of the , changes the loaded picutres as well 
as the button options. to get the response s2t & st2 functions are called"""    
 
def game ():
   aseel = True 
   while aseel:        
       for event in pygame.event.get():
            if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
       
            for i in range(1,5):
                print (i)
                if i == 1:
                      global carImg                       
                      carImg = pygame.image.load(os.path.join(image_path, 'lalaa.jpg'))
                      gameDisplay.blit(carImg,(0,0))
                      # pygame.display.update()
                      NewRightButton = random.randint(1,2)
                      if NewRightButton == 1:
                        button("Dog",150,450,100,50,green,bright_green,s2t())
                        button("Cat",50,450,100,50,blue,bright_bule,st2())                        
                        button("Quit",450,450,100,50,red,bright_red,close)
                        pygame.display.update()        
                        
                      else:   
                         button("Cat",30,250,50,50,green,bright_green,st2())
                         button("Dog",50,450,100,50,blue,bright_bule,s2t())
                         button("Quit",450,450,100,50,red,bright_red,close)    
                         pygame.display.update()
                         
                elif i == 2:
                     
                      carImg = pygame.image.load(os.path.join(image_path, 'Ross.jpg'))
                      gameDisplay.blit(carImg,(0,0))
                      # pygame.display.update()
                      NewRightButton = random.randint(1,2)
                      if NewRightButton == 1:
                        button("ross",150,450,100,50,green,bright_green,s2t())
                        button("Cat",50,450,100,50,blue,bright_bule,st2())
                        button("Quit",450,450,100,50,red,bright_red,close)
                        pygame.display.update() 
                      else:
                        button("Cat",150,450,100,50,green,bright_green,st2())
                        button("ross",50,450,100,50,blue,bright_bule,s2t())
                        button("Quit",450,450,100,50,red,bright_red,close)
                        pygame.display.update() 
                        
                elif i == 3: 
                      carImg = pygame.image.load(os.path.join(image_path, 'gator.jpg'))
                      gameDisplay.blit(carImg,(0,0))
                      # pygame.display.update()
                      NewRightButton = random.randint(1,2)
                      if NewRightButton == 1:
                        button("gator",150,450,100,50,green,bright_green,s2t())
                        button("Cat",50,450,100,50,blue,bright_bule,st2())
                        button("Quit",450,450,100,50,red,bright_red,close)
                        pygame.display.update() 
       
                      else:
                        button("Cat",150,450,100,50,green,bright_green,st2())
                        button("gator",50,450,100,50,blue,bright_bule,s2t())
                        button("Quit",450,450,100,50,red,bright_red,close)
                        pygame.display.update()                                       
                else :
                    carImg = pygame.image.load(os.path.join(image_path, 'Lala_showerd.jpg'))
                    gameDisplay.blit(carImg,(0,0))    
                    message_display('end of the game')      
                    button("Quit",450,450,100,50,red,bright_red,close)
                    print ('end of the game')
                    aseel = False  
                             


"""" In The main function is to show the frist screen with 
two buttons options play or quit. if the user choes quit. the game will quit.
On the other hand, if the user choses to play button. it is going
 to take him 
to game function  """
def main():
     Zyaid = True 
     while Zyaid:
        for event in pygame.event.get():
                 if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
        global carImg                 
        carImg = pygame.image.load(os.path.join(image_path, 'Lala_showerd.jpg'))
        gameDisplay.blit(carImg,(0,0))                
        button("Quit",450,450,100,50,red,bright_red,close)
        button("play",150,450,100,50,green,bright_green, game)
        pygame.display.update()   
     
        
if __name__ == '__main__':
    main()

