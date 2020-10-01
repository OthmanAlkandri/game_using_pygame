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
import pdb 
pygame.init() # insslatize all pygame 

global carImg
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
pygame.display.set_caption('GUI Speech Recognition') #title of the window
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


    



"""This function is for checing the value i  of the , changes the loaded picutres as well 
as the button options. to get the response s2t & st2 functions are called"""    

def game ():
   aseel = 1
   while aseel == 1:        
       for event in pygame.event.get():
        for i in range(1,5):
            print (i)
            if i == 1:
                 carImg = pygame.image.load(os.path.join(image_path, 'lalaa.jpg'))
                 gameDisplay.blit(carImg,(0,0))
                 pygame.display.update()
                 NewRightButton = random.randint(1,2)     
                 if NewRightButton == 1:
                    # pdb.set_trace() 
                    button("Dog",150,450,100,50,green,bright_green,s2t)
                    button("Cat",50,450,100,50,blue,bright_bule,st2)
                   #pdb.set_trace() 
                    #code that says wich the right button is
                    pygame.display.update() 
                    
                    time.sleep(3)        
                    # break  
                 else:
                    # pdb.set_trace() 
                    button("Cat",150,450,100,50,green,bright_green,st2)
                    button("Dog",50,450,100,50,blue,bright_bule,s2t)
                    # pdb.set_trace() 
                    #code that says wich the right button is
                    #This makes the buttons swap back and forth
                    pygame.display.update() 
                
                    time.sleep(3)

            elif i == 2:
                 
                 carImg = pygame.image.load(os.path.join(image_path, 'Ross.jpg'))
                 gameDisplay.blit(carImg,(0,0))
                 pygame.display.update()
                 NewRightButton = random.randint(1,2)
                 if NewRightButton == 1:
                    # pdb.set_trace() 
                    button("ross",150,450,100,50,green,bright_green,s2t)
                    button("Cat",50,450,100,50,blue,bright_green,st2)
                    # pdb.set_trace()
                    #code that says wich the right button is
                    pygame.display.update() 
                    # pdb.set_trace()
                    time.sleep(3)        
                    # break  
                 else:
                    # pdb.set_trace() 
                    button("Cat",150,450,100,50,green,bright_green,st2)
                    button("ross",50,450,100,50,blue,bright_green,s2t)
                    # pdb.set_trace()
                    #code that says wich the right button is
                    #This makes the buttons swap back and forth
                    pygame.display.update() 
                    # pdb.set_trace()
                    time.sleep(3)
                    # break 
            elif i == 3: 
                 carImg = pygame.image.load(os.path.join(image_path, 'gator.jpg'))
                 gameDisplay.blit(carImg,(0,0))
                 pygame.display.update()
                 NewRightButton = random.randint(1,2)
                 if NewRightButton == 1:
                    # pdb.set_trace()
                    button("gator",150,450,100,50,green,bright_green,s2t)
                    button("Cat",50,450,100,50,blue,bright_green,st2)
                    # pdb.set_trace()
                    #code that says wich the right button is
                    pygame.display.update() 
                    # pdb.set_trace()
                    time.sleep(3)        
                    # break  
                 else:
                    # pdb.set_trace()
                    button("Cat",150,450,100,50,green,bright_green,st2)
                    button("gator",50,450,100,50,blue,bright_green,s2t)
                    # pdb.set_trace()
                    #code that says wich the right button is
                    #This makes the buttons swap back and forth
                    pygame.display.update() 
                    # pdb.set_trace()
                    time.sleep(3)
                                    
            else :
                # pdb.set_trace()
                carImg = pygame.image.load(os.path.join(image_path, 'Lala_showerd.jpg'))
                gameDisplay.blit(carImg,(0,0))    
                message_display('end of the game')              
                # pdb.set_trace()
                print ('end of the game')
                time.sleep(3)
                aseel = aseel + 1
                # pdb.set_trace()
            
            
            
def s2t():
    # pdb.set_trace() 
    #carImg= game()
    gameDisplay.blit(carImg,(0,0))    
    message_display('good job')
    print('good job')
  
def st2():
    # pdb.set_trace()
    #carImg= game()
    gameDisplay.blit(carImg,(0,0))  
    message_display('wrong')
    print('wrong')




            
            
def trake_mouse():   #To  trake mosue postion
    gameExit = False
    while not gameExit:
        for event in pygame.event.get():
            print (event)

"""" In The main function is to show the frist screen with 
two buttons options play or quit. if the user choes quit. the game will quit.
On the other hand, if the user choses to play button. it is going to take him 
to game function  """
def main ():
     while True:
        for event in pygame.event.get():
                 if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()
        carImg = pygame.image.load(os.path.join(image_path, 'Lala_showerd.jpg'))
        gameDisplay.blit(carImg,(0,0))                
        # pygame.display.update()
        button("Quit",450,250,100,50,red,bright_red,close)
        button("play",150,250,100,50,green,bright_green,game)
        pygame.display.update()   
     
        
if __name__ == '__main__':
    main()

