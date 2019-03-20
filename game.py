# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 04:46:56 2019

@author:awan-ur-rahman
"""

import pygame as pg
import cv2
import time 
pg.ver
pg.init()

#define the windows size
display_weight = 500
display_height = 500

#displaying the windows
game_display = pg.display.set_mode((display_weight, display_height))

pg.display.set_caption("racing game")
background_color = [119,118,110]
game_display.fill(background_color)
pg.display.flip()
clock = pg.time.Clock()


#car_img = cv2.imread("car1.png",1)
#car_img = cv2.resize(car_img, (50,80))
#cv2.imwrite("car5.png", car_img)
# =============================================================================
# load image and scaling 
# =============================================================================
car_image = pg.image.load("car1.png")
car_image = pg.transform.scale(car_image, (50, 80))
car_width = 50
# =============================================================================
# #load background image 
# =============================================================================

background_roadside = pg.image.load("black1.png")
background_roadside = pg.transform.scale(background_roadside, (1,500))
background_grass = pg.image.load("grass.jpg")
background_grass = pg.transform.scale(background_grass, (80,150))
background_roadstrip = pg.image.load("strip.png")
background_roadstrip = pg.transform.scale(background_roadstrip, (3,50))
# rect = car_image.get_rect() -->GET THE BOUNDARY RECTANGLE OF THE PICTURE
# =============================================================================
# image display on the screen 
# =============================================================================
def Car(x , y ) :
    global game_display
    global car_image
    game_display.blit(car_image , (x, y))
#    pg.display.update()

#pg.display.update()


#backgroundimage

def Background() :
    global background_roadside, background_grass, background_roadstrip , game_display
    #left grass 
    game_display.blit(background_grass , (0, 0))
    game_display.blit(background_grass , (0, 140))
    game_display.blit(background_grass , (0, 270))
    game_display.blit(background_grass , (0, 400))
    
    #right grass 
    game_display.blit(background_grass , (420, 0))
    game_display.blit(background_grass , (420, 140))
    game_display.blit(background_grass , (420, 270))
    game_display.blit(background_grass , (420, 400))
    
    #road border
    game_display.blit(background_roadside , (80, 0)) #left
    game_display.blit(background_roadside , (420, 0)) #right
    
    #road strip 
    x=0
    for i in range(0,500,50) :
          game_display.blit(background_roadstrip , (249, i+(x*20)))
          x=x+1

def Text_Objects(text , font) :
    textsurface = font.render(text , True , (0,0,0))
    return textsurface , textsurface.get_rect()

def Message_Display(text) :
    largetext = pg.font.Font("freesansbold.ttf", 80)
    text_surf , text_rect = Text_Objects(text, largetext)
    text_rect.center = (display_weight/2 , display_height/2)
    game_display.blit(text_surf , text_rect)
    pg.display.update()
    time.sleep(3)
    game_loop()
def Crash() :
    Message_Display("you Crashed")



#global display_weight , display_height ,car_width 
#running = True
#x = display_weight *0.45
#y = display_height *0.45

def game_loop () :
    global display_weight , display_height ,car_width 
    running = True
    x = display_weight *0.45
    y = display_height *0.45

    while running :
        x_change = 0
        y_change = 0
#    Car(x,y)
        for event in pg.event.get():
            if event.type is pg.QUIT:
                running = False
                pg.quit()
            if event.type is pg.KEYUP :
                if event.key is pg.K_LEFT or event.key is ord('a') :
                    x_change = -10
                if event.key is pg.K_RIGHT or event.key is ord('d') :
                    x_change = 10
                if event.key is pg.K_UP or event.key is ord('w') :
                    y_change = -10
                if event.key is pg.K_DOWN or event.key is ord('s') :
                    y_change = 10
       
#            if event.type is pg.KEYDOWN:
#                if event.key is ord('a') or event.key is ord('d'):
#                    x_change = 0
#                if event.key is ord('w') or event.key is ord('s') :
#                    y_change = 0
            x+=x_change
            y+=y_change
            background_color = [119,118,110]
            game_display.fill(background_color)
            Background()
            pg.display.update()
            Car(x,y)
            pg.display.update()
            if x>450- car_width or x<60 :
                Crash()
                clock.tick(50)




if __name__ == "__main__":
    game_loop () 

























