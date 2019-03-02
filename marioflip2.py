import pygame, sys
from pygame.locals import *

#note from Tom

#constants representing colours
WHITE = (255,   255,   255  )
BROWN = (153, 76,  0  )
BLUE = (169, 232, 228)
 
#constants representing the different resources
LEAF  = 0
TOAD = 1

 
#a dictionary linking resources to colours
colours =   {
                LEAF  : pygame.image.load('brownblock.png'),
                TOAD  : pygame.image.load('whiteblock.png')
            }
#maps
tilemap = [
            [LEAF,TOAD,TOAD,LEAF],
            [LEAF,LEAF,TOAD,LEAF],
            [LEAF,TOAD,LEAF,LEAF],
            [LEAF,TOAD,TOAD,LEAF]
          ]
tilemap2 = [
            [LEAF,TOAD,TOAD,LEAF],
            [LEAF,LEAF,LEAF,TOAD],
            [LEAF,TOAD,TOAD,TOAD],
            [LEAF,TOAD,LEAF,TOAD]
          ]
tilemap = [
            [LEAF,TOAD,TOAD,LEAF],
            [TOAD,LEAF,LEAF,TOAD],
            [TOAD,LEAF,LEAF,TOAD],
            [LEAF,TOAD,TOAD,LEAF]
          ]
tilemap2 = [
            [LEAF,TOAD,TOAD,LEAF],
            [LEAF,TOAD,LEAF,TOAD],
            [LEAF,TOAD,LEAF,TOAD],
            [TOAD,LEAF,TOAD,LEAF]
          ]
tilemap = [
            [TOAD,TOAD,TOAD,TOAD],
            [TOAD,LEAF,LEAF,TOAD],
            [TOAD,LEAF,LEAF,TOAD],
            [TOAD,TOAD,TOAD,TOAD]
          ]
tilemap2 = [
            [TOAD,TOAD,LEAF,LEAF],
            [TOAD,LEAF,TOAD,LEAF],
            [TOAD,LEAF,LEAF,TOAD],
            [TOAD,TOAD,TOAD,TOAD]
          ]

pygame.init()
DISPLAYSURF = pygame.display.set_mode((MAPWIDTH*TILESIZE+80,MAPHEIGHT*TILESIZE+280))
DISPLAYSURF.fill(BLUE) 
while True:
    
    

    #get all the user events
    for event in pygame.event.get():
        #if the user wants to quit
            if event.type == QUIT:
            #and the game and close the window
            pygame.quit()
            sys.exit()
        (x, y)= pygame.mouse.get_pos()

 
    #loop through each row
    for row in range(MAPHEIGHT):
        #loop through each column in the row
        for column in range(MAPWIDTH):
            #draw the resource at that position in the tilemap, using the correct colour
            DISPLAYSURF.blit(colours[tilemap[row][column]], (column*TILESIZE+40,row*TILESIZE+40))
    #loop through each row
    for row in range(MAPHEIGHT):
        #loop through each column in the row
        for column in range(MAPWIDTH):
            #draw the resource at that position in the tilemap, using the correct colour
            DISPLAYSURF.blit(colours[tilemap2[row][column]], (column*TILESIZE+40,row*TILESIZE+240))
    #update the display
    pygame.display.update()