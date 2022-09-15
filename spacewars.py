import pygame
import random

pygame.init()   #initialize pygame

screen=pygame.display.set_mode((600,700))  #Creating the screen

#For setting the title and icon of  the game
pygame.display.set_caption("SpaceWars")
icon=pygame.image.load('spaceship.png')
pygame.display.set_icon(icon)

#background
background=pygame.image.load('space.png')


#player Ship
playship=pygame.image.load('playership.png')
playerX=280
playerY=550
playerX_change=0

#alien
alienimg=pygame.image.load('alien.png')
alienX=random.randint(0,600)    #using randint to spawwn the alien anywhere between those mentioned values.
alienY=random.randint(50,160)
alienX_change=3.1
alienY_change=20

def player(x,y):
    screen.blit(playship,(x,y))  #blit means drawing,here drawing player ship on the screen

def alien(x,y):
    screen.blit(alienimg,(x,y))

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
    alienX+=alienX_change   
    if alienX <=0:
        alienX_change=3.1
        alienY+=alienY_change
    elif alienX >= 536:
        alienX_change=-3.1
        alienY+=alienY_change
    
    player(playerX,playerY)   #Calling the player function from above
    alien(alienX,alienY)
    pygame.display.update()   #to update anything inside the game window running

