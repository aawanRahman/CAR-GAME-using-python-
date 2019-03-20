
"""
@author:awan-ur-rahman
"""
import pygame as pg
import cv2
import time 
import random 
import sys

pg.ver
pg.init()

#defining color .......

blue = (0,0,200)
bright_blue = (0,0,255)
green = (0,200,0)
bright_green = (0,255,0)
red = (200,0,0)
bright_red = (255,0,0)     

#define the windows size
display_width = 500
display_height = 500

#displaying the windows
game_display = pg.display.set_mode((display_width, display_height))

pg.display.set_caption("racing game")
background_color = [119,118,110]
game_display.fill(background_color)
pg.display.flip()
clock = pg.time.Clock()


#car_img = cv2.imread("image/car1.png",1)
#car_img = cv2.resize(car_img, (50,80))
#cv2.imwrite("car5.png", car_img)

# =============================================================================
# load image and scaling 
# =============================================================================
car_image = pg.image.load("image/car11.png")
car_image = pg.transform.scale(car_image, (30, 60))
car_width = 30

# =============================================================================
# #load obstacle car image..
# =============================================================================

obstacle_pic = pg.image.load("image/car1.png")
obstacle_pic = pg.transform.scale(obstacle_pic, (50, 80))
#car_width = 50

obstacle_image2 = pg.image.load("image/car2.png")
obstacle_image2 = pg.transform.scale(obstacle_image2, (50, 80))
#car_width = 50

obstacle_image3 = pg.image.load("image/car3.png")
obstacle_image3 = pg.transform.scale(obstacle_image3, (50, 80))
#car_width = 50

obstacle_image4 = pg.image.load("image/car4.png")
obstacle_image4 = pg.transform.scale(obstacle_image4, (50, 80))
#car_width = 50

obstacle_image5 = pg.image.load("image/car5.png")
obstacle_image5 = pg.transform.scale(obstacle_image5, (50, 80))
#car_width = 50


# =============================================================================
# #introduction pic of game ...
# =============================================================================

instuction_pic =  pg.image.load("image/introduction.jpg")
instuction_pic = pg.transform.scale(instuction_pic, (500, 480))
start_background =  pg.image.load("image/intro_pic.png")
start_background = pg.transform.scale(start_background, (500,480))

# =============================================================================
# #load background image 
# =============================================================================

background_roadside = pg.image.load("image/white.jpg")
background_roadside = pg.transform.scale(background_roadside, (2,500))

background_border = pg.image.load("image/black1.png")
background_border = pg.transform.scale(background_roadside, (2,500))

background_grass = pg.image.load("image/grass.jpg")
background_grass = pg.transform.scale(background_grass, (80,500))
background_roadstrip = pg.image.load("image/strip.png")
background_roadstrip = pg.transform.scale(background_roadstrip, (3,50))
# rect = car_image.get_rect() -->GET THE BOUNDARY RECTANGLE OF THE PICTURE


def instruction() :
    global game_display , blue, bright_blue
    instruction = True 
    while instruction :
        for event in pg.event.get():
            if event.type is pg.QUIT:
                instruction = False
                pg.quit()
                quit()
                sys.exit()
                
        game_display.blit(instuction_pic , (0, 0))
        medium_font = pg.font.Font("freesansbold.ttf", 20)
        small_font = pg.font.Font("freesansbold.ttf", 15)
        text_surf , text_rect = Text_Objects("In This Game You Need To Avoid The Collison Of UpComing Car ", small_font)
        text_rect.center = (249, 200)
        Text_Surf , Text_Rect = Text_Objects("INSTRUCTION", medium_font)
        Text_Rect.center = (249, 100)
        game_display.blit(text_surf , text_rect)
        game_display.blit(Text_Surf , Text_Rect)
#        atext_surf , atext_rect = Text_Objects("a : LEFT MOVE   ", medium_font)
#        atext_rect.center = (120, 300)
#        dtext_surf , dtext_rect = Text_Objects("d : RIGHT MOVE  ", medium_font)
#        dtext_rect.center = (120, 330)
#        stext_surf , stext_rect = Text_Objects("s : DOWN MOVE   ", medium_font)
#        stext_rect.center = (120, 360)
#        wtext_surf , wtext_rect = Text_Objects("w : FORWARD MOVE", medium_font)
#        wtext_rect.center = (120, 390)
#        game_display.blit(atext_surf , atext_rect)
#        game_display.blit(dtext_surf , dtext_rect)
#        game_display.blit(stext_surf , stext_rect)
#        game_display.blit(wtext_surf , wtext_rect)
       
        font = pg.font.SysFont(None , 20)
        a_text = font.render("a: LEFT MOVE" , True, (255,255,0))
        d_text = font.render("d : RIGHT MOVE" , True, (255,255,0))
        s_text = font.render("s : DOWN MOVE" , True, (255,255,0))
        w_text = font.render("w : FORWARD MOVE" , True, (255,255,0))
        game_display.blit(a_text, (50,300))
        game_display.blit(d_text, (50,330))
        game_display.blit(s_text, (50,360))
        game_display.blit(w_text, (50,390))
        
        button("Back" , 400, 400, 100 , 50 , blue , bright_blue , "menu")
        
        
      
        
        
        
def Start_Page() :
    global start_background , green , bright_green , blue ,bright_blue, red , bright_red
    start = True 
    game_display.blit(start_background , (0, 0))
    while start :
         for event in pg.event.get():
            if event.type is pg.QUIT:
                start = False
                pg.quit()
                
         
         largetext = pg.font.Font("freesansbold.ttf", 80)
         text_surf , text_rect = Text_Objects("CAR GAME", largetext)
         text_rect.center = (display_width/2 , display_height/2)
         game_display.blit(text_surf , text_rect)
         

         button("START",40, 350, 60, 50 , green , bright_green , "play")  
         
         button("INSTRUCTION",130,350, 130, 50 , blue , bright_blue , "instruction")   
        
         button("QUIT",300, 350, 80, 50, red , bright_red , "quit")   
    
         


#button action ..............

def button(message,x,y,w,h,ic, ac , action = None ):
    global game_display 
    
    mouse = pg.mouse.get_pos()
    click = pg.mouse.get_pressed()
    if x+w > mouse[0] > x and y+h > mouse[1] > y :
        pg.draw.rect(game_display, ac , (x,y,w,h))
        if click[0] ==1 and action != None :
            if action is "play" :
                game_loop()
            elif action is "instruction" :
                instruction()
            elif action is "menu" :
                Start_Page()
            elif action is "quit" :
                 pg.quit()
                 
    else :
         pg.draw.rect(game_display, ic , (x,y,w,h))
         
    text_font = pg.font.Font("freesansbold.ttf", 15)
    text_surf , text_rect = Text_Objects(message, text_font)
    text_rect.center = (x+(w/2) , (y + h/2))
    game_display.blit(text_surf , text_rect)
    pg.display.update()
            

#start page load ............


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

def Background(real_y , background_moved , obstacles_speed) :
    global background_roadside, background_grass, background_roadstrip , game_display
    #left grass 
    
    
#    game_display.blit(background_grass, (0,real_y - background_grass.get_rect().width))
#    game_display.blit(background_grass, (420,real_y - background_grass.get_rect().width))
#    if real_y<500 :
#        game_display.blit(background_grass, (0,real_y))
#        game_display.blit(background_grass, (420,real_y))
    
    
    
#    game_display.blit(background_grass , (0, 0))
#    game_display.blit(background_grass , (0, 140))
#    game_display.blit(background_grass , (0, 270))
#    game_display.blit(background_grass , (0, 400))
#    
#    #right grass 
#    game_display.blit(background_grass , (420, 0))
#    game_display.blit(background_grass , (420, 140))
#    game_display.blit(background_grass , (420, 270))
#    game_display.blit(background_grass , (420, 400))
#    
    #road border
    game_display.blit(background_roadside , (80, 0)) #left
    game_display.blit(background_roadside , (420, 0)) #right
    
    #road strip 
    x=0
    for i in range(0,500,50) :
          game_display.blit(background_roadstrip ,  (249, real_y + (i+(x*20))))
          x=x+1

def Text_Objects(text , font) :
    textsurface = font.render(text , True , (0,0,0))
    return textsurface , textsurface.get_rect()

def Message_Display(text) :
    largetext = pg.font.Font("freesansbold.ttf", 80)
    text_surf , text_rect = Text_Objects(text, largetext)
    text_rect.center = (display_width/2 , display_height/2)
    game_display.blit(text_surf , text_rect)
    pg.display.update()
    time.sleep(3)
    game_loop()
def Crash() :
    Message_Display("you Crashed")



#global display_width , display_height ,car_width 
#running = True
#x = display_width *0.45
#y = display_height *0.45

#defining functions for obstacles ........

def Obstacles( obstacles_startx , obstacles_starty , obstcle ) :
     
    global obstacle_pic, obstacle_image1, obstacle_image2 , obstacle_image3 , obstacle_image4 , obstacle_image5 , game_display
    if obstcle is 0 :
        obstacle_pic = pg.image.load("car1.png")
        obstacle_pic = pg.transform.scale(obstacle_pic, (30, 60))
    elif obstcle is 1 :
        obstacle_pic = pg.image.load("car2.png")
        obstacle_pic = pg.transform.scale(obstacle_pic, (30, 60))
    elif obstcle is 2 :
        obstacle_pic = pg.image.load("car3.png")
        obstacle_pic = pg.transform.scale(obstacle_pic, (30, 60))
    elif obstcle is 3 :
        obstacle_pic = pg.image.load("car4.png")
        obstacle_pic = pg.transform.scale(obstacle_pic, (30, 60))
    
    elif obstcle is 4 :
        obstacle_pic = pg.image.load("car8.png")
        obstacle_pic = pg.transform.scale(obstacle_pic, (30, 60))
   
   

    game_display.blit(obstacle_pic , (obstacles_startx , obstacles_starty))


#function for calculating the score.....

def Score_system(passed , score) :
    global game_display 
    font = pg.font.SysFont(None , 22)
    passed_text = font.render("passed:" + str(passed), True, (255,255,0))
    score_text = font.render("score:" + str(score), True, (255,255,255))
    game_display.blit(passed_text, (0,100))
    game_display.blit(score_text, (0,70))
    
    


def game_loop () :
    global display_width , display_height ,car_width 
    running = True
    x = display_width *0.47
    y = 440
    obstacles_speed =0.5
    obstcle = 0 
    obstacles_startx = random.randrange(95,(display_width - 80))
    obstacles_starty = -500
    obstacle_width = 30
    obstacle_height = 60

    background_moved = 0
    passed = 0
    level = 0 
    score = 0
   
    
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
                    x_change = -1
                if event.key is pg.K_RIGHT or event.key is ord('d') :
                    x_change = 1
                if event.key is pg.K_UP or event.key is ord('w') :
                    y_change = -1
                if event.key is pg.K_DOWN or event.key is ord('s') :
                    y_change = 1
       
            if event.type is pg.KEYDOWN:
                if event.key is ord('a') or event.key is ord('d'):
                    x_change = 0
                if event.key is ord('w') or event.key is ord('s') :
                    y_change = 0
    
        keys_pressed = pg.key.get_pressed()

        if keys_pressed[ord('a')]:
            x_change -= 1

        if keys_pressed[ord('d')]:
            x_change += 1

        if keys_pressed[ord('w')]:
            y_change -= 1

        if keys_pressed[ord('s')]:
            y_change += 1

        x+=x_change
        y+=y_change
        background_color = [119,118,110]
        game_display.fill(background_color)
      
        real_y = background_moved % background_grass.get_rect().height
#        real_y2 = background_moved % background_roadstrip.get_rect().height
        
       
#        Background(real_y , background_moved , obstacles_speed)
        
        game_display.blit(background_roadside , (80, 0)) #left
        game_display.blit(background_roadside , (418, 0)) #right
        game_display.blit(background_grass, (0,real_y - background_grass.get_rect().height))
     
        game_display.blit(background_grass, (420,real_y - background_grass.get_rect().height))
        if real_y<600 :
            game_display.blit(background_grass, (0,real_y))
            game_display.blit(background_grass, (420,real_y))
#            game_display.blit(background_roadstrip, (249,real_y+100))
#            game_display.blit(background_roadstrip, (249,real_y+200))
#            game_display.blit(background_roadstrip, (249,real_y+300))
#            game_display.blit(background_roadstrip, (249,real_y+400))
#            game_display.blit(background_roadstrip, (249,real_y+500))
#            game_display.blit(background_roadstrip, (249,real_y-100))
            
           
            s=0
#            game_display.blit(background_roadstrip ,  (249, real_y))
            for i in range(0,502,50) :
                game_display.blit(background_roadstrip ,  (249, real_y + (i+(s*20))))
                s=s+1
            
            print(s)
            game_display.blit(background_roadstrip ,  (249, real_y))
            s=10
            for i in range(500,-1,-50) :
                game_display.blit(background_roadstrip ,  (249, real_y - (i+(s*20))))
                s=s-1
            game_display.blit(background_roadstrip ,  (249, real_y))
        background_moved +=obstacles_speed  
        
#        pg.display.update()
        obstacles_starty -= (obstacles_speed / 4)
        Obstacles(obstacles_startx ,obstacles_starty , obstcle )
        obstacles_starty +=  obstacles_speed
#            pg.display.update()
        Car(x,y)
#            pg.display.update()
        Score_system(passed , score)
        if x>405 or x<65 :
            Crash()
                
        if x > display_width - (car_width +40 ) or x <65 : 
            Crash()
        if obstacles_starty > display_height :
            obstacles_starty = 0 - obstacle_height
            obstacles_startx = random.randrange(95,(display_width - 100))
            obstcle = random.randrange(0,4)
            passed += 1
            score += 5
            if int(passed)%10 == 0 :
                level=level + 1
                obstacles_speed = 0.5+ (level *0.5)
                largetext = pg.font.Font("freesansbold.ttf", 80)
                text_surf , text_rect = Text_Objects("level "+ str(level), largetext)
                text_rect.center = (display_width/2 , display_height/2)
                game_display.blit(text_surf , text_rect)
                pg.display.update()
                time.sleep(2)
                
        if y  < obstacle_height + obstacles_starty   and y  >  obstacles_starty - obstacle_height :
#            print( obstacle_height + obstacles_starty)
            if x>obstacles_startx and x < obstacles_startx + obstacle_width or x+car_width>obstacles_startx and x+car_width < obstacles_startx + obstacle_width :
                Crash()
                       
        pg.display.update()


if __name__ == "__main__":
    
   Start_Page()
#   game_loop () 



























