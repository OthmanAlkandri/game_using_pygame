# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 17:15:42 2020

@author: okand
"""
import glob
import pygame
import random #we use this to make a random right button
import time 
import os 
pygame.init() # insslatize all pygame 

display_width = 600
display_height = 600

black = (0,0,0)
alpha = (0,88,255)
white = (255,255,255)
red = (200,0,0)
green = (0,200,0)
blue = (0, 0, 255)
bright_red = (255,0,0)
bright_green = (0,255,0)


""""Setting display. note the starderd we use is 600*600 display limtation"""
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('GUI Speech Recognition') #title of the window
gameDisplay.fill(white)


""" Loading images to the paython from the pic file """
current_path = os.path.dirname(__file__)

image_path = os.path.join('image')
def load_the_image(image):
    images = [
        load_the_image('lalaa.jpg'),
        load_the_image('Ross.jpg')
   ]


def close():
    pygame.quit()
    quit()

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



def s2t():
    carImg= game()
    gameDisplay.blit(carImg,(0,0))    
    message_display('good job')
    print('good job')
  
def st2():
    carImg= game()
    gameDisplay.blit(carImg,(0,0))  
    message_display('wrong')
    print('wrong')
    
    
def game ():
        aseel = 4
   while aseel  > 1: 
       aseel -= 1
       for event in pygame.event.get():
        for i in range(1,3):
            if i == 1:
                 
                 carImg = pygame.image.load(os.path.join(image_path, 'lalaa.jpg'))
                 gameDisplay.blit(carImg,(0,0))
                 pygame.display.update()
            
                 NewRightButton = 1   #random.randint(1,2)
                 
                 if NewRightButton == 1:
                    button("Dog",150,450,100,50,green,bright_green,s2t)
                    button("Cat",50,450,100,50,blue,bright_green,st2)
                    #code that says wich the right button is
                    pygame.display.update() 
                    # time.sleep(3)        
                    break  
                 else:
                    button("Cat",150,450,100,50,green,bright_green,st2)
                    button("Dog",50,450,100,50,blue,bright_green,s2t)
                    #code that says wich the right button is
                    #This makes the buttons swap back and forth
                    pygame.display.update() 
                    # time.sleep(3)
                    break 
                 aseel = aseel + 1
                 print (aseel)
            elif i == 2: 
                 carImg = pygame.image.load(os.path.join(image_path, 'Ross.jpg'))
                 gameDisplay.blit(carImg,(0,0))
                 pygame.display.update()
            
                 NewRightButton = 1   #random.randint(1,2)
                 
                 if NewRightButton == 1:
                    button("Dog",150,450,100,50,green,bright_green,s2t)
                    button("Cat",50,450,100,50,blue,bright_green,st2)
                    #code that says wich the right button is
                    pygame.display.update() 
                    # time.sleep(3)        
                    break  
                 else:
                    button("Cat",150,450,100,50,green,bright_green,st2)
                    button("Dog",50,450,100,50,blue,bright_green,s2t)
                    #code that says wich the right button is
                    #This makes the buttons swap back and forth
                    pygame.display.update() 
                    # time.sleep(3)
                    break 
                 aseel = aseel + 1 
                 print (aseel)
                
            else :
                aseel = aseel + 1
                continue 
            print ('end of the game')
            aseel = aseel + 1
             
        
     
 
                
        
            
def trake_mouse():   #To  trake mosue postion
    gameExit = False
    while not gameExit:
        for event in pygame.event.get():
            print (event)
                         
def main ():
     while True:
        for event in pygame.event.get():
                 if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()
        pygame.display.update()
        button("Quit",450,250,100,50,red,bright_red,close)
        button("play",150,250,100,50,green,bright_green,game)
        pygame.display.update()   
     
        
if __name__ == '__main__':
    main()

