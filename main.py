import pygame as pg
from random import randint
import os

pg.init() # init all modules for pg

#screen size
screen_x= 1000
screen_y=500

#scr start
screen = pg.display.set_mode((screen_x,screen_y))
pg.display.set_caption("Test")
screen.fill((255,255,255))

#image loader
class img_loader:
    #image loaders
    bg=pg.image.load(r"assets/background.png")
    bul=pg.image.load(r"assets/bullet.png")
    e_bul=pg.image.load(r"assets/enemy_bullet.png")
    e1=pg.image.load(r"assets/enemy1.png")
    e2=pg.image.load(r"assets/enemy2.png")
    e3=pg.image.load(r"assets/enemy3.png")
    menu=pg.image.load(r"assets/menu.png")
    p2=pg.image.load(r"assets/player2.png")
    p3=pg.image.load(r"assets/player3.png")
    p4=pg.image.load(r"assets/player4.png")
    shield=pg.image.load(r"assets/shield.png")

    #transformed
    bg_scaled=pg.transform.scale(bg,(screen_x,screen_y))#scales the image ; args : image,(x,y)
    bul_scaled=pg.transform.scale(bul,(screen_x,screen_y))
    e_bul_scaled=pg.transform.scale(e_bul,(screen_x,screen_y))
    e1_scaled=pg.transform.scale(e1,(screen_x,screen_y))
    e2_scaled=pg.transform.scale(e2,(screen_x,screen_y))
    e3_scaled=pg.transform.scale(e3,(screen_x,screen_y))
    menu_scaled=pg.transform.scale(menu,(screen_x,screen_y))
    p2_scaled=pg.transform.scale(p2,(screen_x,screen_y))
    p3_scaled=pg.transform.scale(p3,(screen_x,screen_y))
    p4_scaled=pg.transform.scale(p4,(screen_x,screen_y))
    shield_scaled=pg.transform.scale(shield,(screen_x,screen_y))

i_loader=img_loader()

#player class
class player:
    def __init__(self,x,y):
        #loaD x y and all images
        self.x=x
        self.y=y
        self.img_1=pg.image.load(r"assets/player1.png")
        self.img_2=pg.image.load(r"assets/player2.png")
        self.img_3=pg.image.load(r"assets/player3.png")
        self.img_4=pg.image.load(r"assets/player4.png")
        self.img=pg.transform.scale(self.img_1,(100,100))
        self.rect=self.img.get_rect()
        self.rect.center=(x,y)
        self.i=0
        self.is_jumping=False
        self.in_air=0

    def draw(self):
        if self.is_jumping==False:
            #drawthe player animating by counting op and choosing frame
            if self.i<=0.0:
                self.img=pg.transform.scale(self.img_1,(100,100))
            elif self.i<=1.0:
                self.img=pg.transform.scale(self.img_2,(100,100))
            elif self.i<=2.0:
                self.img=pg.transform.scale(self.img_3,(100,100))
            elif self.i<=3.0:
                self.img=pg.transform.scale(self.img_4,(100,100))
            if self.i>=3:
                self.i=0
            else:
                self.i+=0.31#animation speed
        self.img_scaled=pg.transform.scale(self.img,(100,100))
        self.rect.center=(self.x,self.y)
        screen.blit(self.img,self.rect)

    def jump(self):
        if self.jump==False:
            return
        self.in_air+=1
        if self.in_air<7:
            self.y-=((15-self.in_air)**2/10)
        if self.in_air==7:
            pass
        if self.in_air>=7:
            self.y+=((15-self.in_air)**2/10)
        if self.in_air>=15:
            self.is_jumping=False

p1=player(100,386) #found using trial n error

#control var
running=True

#clcock object to maintain fps and everything
clock=pg.time.Clock()
clock.tick(30)

bl_x=0# check notes.txt line 5 to 7, this var is set so bliiting x coord can be controlled
speed=0#speed of bg
count=0

#main loop
while running:
    
    #start event listener
    for event in pg.event.get():
        if event.type==pg.QUIT:#if event is quit which is close signal , update var to false to break loop
            running=False
        if event.type==pg.KEYDOWN:
            if event.key==pg.K_SPACE:
                p1.is_jumping=False
    bl_x-=(5+speed)#moves the img backwards and this is for speed
    

    if -(bl_x)==screen_x:#if img is completely off screen resets the image to complete image loop
        bl_x=0
      #  if speed<screen_x:
       #     speed+=.006

    #draws anything we mention ; args:image,(x,y)
    screen.blit(i_loader.bg_scaled,(bl_x,0)) #primary image which is going to move backk first 
    screen.blit(i_loader.bg_scaled,(screen_x+bl_x,0))#secondary image to fill the empty area which the primary image used to fill but as it moves back , the area is empty so this secondary image fills it, which eventually fills the screen and allows the primary image to reset and come to original pos again
    p1.draw()
    #p1.jump()
    pg.display.update() # to update scr for every loop iteration