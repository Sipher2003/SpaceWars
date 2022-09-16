import pygame
import random
import math
# from pygame import mixer
# from pygame import mixer_music

pygame.init()   #initialize pygame

screen=pygame.display.set_mode((600,700))  #Creating the screen

#For setting the title and icon of  the game
pygame.display.set_caption("SpaceWars")
icon=pygame.image.load('spaceship.png')
pygame.display.set_icon(icon)

#background
background=pygame.image.load('space.png')
#bg sound
# mixer.music.load("bg.wav")
# mixer.music.play(-1)  #-1 for playing sound on loop

#player Ship
playship=pygame.image.load('playership.png')
playerX=280
playerY=550
playerX_change=0

#alien
alienimg=[]
alienX=[]
alienY=[]
alienX_change=[]
alienY_change=[]
num_enemies=9

for i in range(num_enemies):
    alienimg.append(pygame.image.load('alien.png'))
    alienX.append(random.randint(0,535))    #using randint to spawwn the alien anywhere between those mentioned values.
    alienY.append(random.randint(50,160))
    alienX_change.append(3.1)
    alienY_change.append(20)

#gameover
game_over=pygame.font.Font("freesansbold.ttf",60)
gameoverX=300
gameoverY=350

#score
score=0
font=pygame.font.Font("freesansbold.ttf",32)
fontX=10
fontY=10

#bullet
bulletimg=pygame.image.load('bullet.png')
bulletX=0    #using randint to spawwn the alien anywhere between those mentioned values.
bulletY=550
bulletX_change=0
bulletY_change=10
bullet_state='ready'  # cant see bullet on the screen and fire state means we can see bullet on the screen

def gam_over():
    overtext=game_over.render("GAMEOVER",True,(255,255,255))
    screen.blit(overtext,(100,350))


def scoce_val(x,y):
    score_val=font.render("SCORE: "+ str(score),True,(255,255,255))
    screen.blit(score_val,(x,y))

def player(x,y):
    screen.blit(playship,(x,y))  #blit means drawing,here drawing player ship on the screen

def alien(x,y,i):
    screen.blit(alienimg[i],(x,y))

def bullet(x,y):
    global bullet_state
    bullet_state='fire'
    screen.blit(bulletimg,(x+16,y+10))

def collision(alienX,alienY,bulletX,bulletY):
    distance=math.sqrt((math.pow(alienX-bulletX,2)) +(math.pow(alienY-bulletY,2)))
    if distance<27:
        return True
    else:
        return False


#To avoid the closing of window quickly
running=True
while running:
    screen.fill((0,0,0)) #RGB values
    screen.blit(background,(0,0))  #adding background
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
    
#Checking keystroke if it is right or left

        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                # print("Left Key")
                playerX_change=-5   
            if event.key == pygame.K_RIGHT:
                # print("Right key")
                playerX_change=5
            if event.key==pygame.K_SPACE:
                if bullet_state=='ready':
                 bulletX=playerX
                 bullet(bulletX,bulletY)
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_LEFT or event.key == pygame.K_RIGHT:
                # print("key pressed was released")
                playerX_change=0
  


    playerX+=playerX_change   #adding playerX_change to x coordinate to move the spaceship.
    
    #Creating Boundaries for the spaceship
    if playerX <=0:
        playerX=0
    elif playerX >= 536:
        playerX=536

    
    #moving the alien
    for i in range(num_enemies):
      if alienY[i]>500:
        for j in range(num_enemies):
            alienY[j]=2000
        gam_over()
        break
      
      alienX[i]+=alienX_change[i]   
      if alienX [i]<=0:
          alienX_change[i]=3.1
          alienY[i]+=alienY_change[i]
      elif alienX[i] >= 536:
          alienX_change[i]=-3.1
          alienY[i]+=alienY_change[i]
         #collision
      collide=collision(alienX[i],alienY[i],bulletX,bulletY)
      if collide:
        bulletY=550
        bullet_state="ready"
        score+=1
        print(score)
        alienX[i]=random.randint(0,600)     #spawn the alien again.
        alienY[i]=random.randint(50,160)
      alien(alienX[i],alienY[i],i)          #calling the alien function

    #moving the bullet
    if bulletY<=0:
        bulletY=550
        bullet_state='ready'
    if bullet_state=='fire':
        bullet(bulletX,bulletY)
        bulletY-=bulletY_change

    player(playerX,playerY)   #Calling the player function from above   
    scoce_val(fontX,fontY)
    pygame.display.update()   #to update anything inside the game window running

