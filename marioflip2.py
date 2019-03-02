import math
from mariopuzzles import *
import pygame, sys
from pygame.locals import *
import random
#note from Tom

#constants representing colours
WHITE = (255,   255,   255  )
BROWN = (153, 76,  0  )
BLUE = (169, 232, 228)
 
#constants representing the different resources
LEAF  = 1
TOAD = 0
TILESIZE  = 40
MAPWIDTH  = 4
MAPHEIGHT = 4
tilemaps = []
cat = [LEAF,TOAD]
#a dictionary linking resources to colours
colours =   {
                LEAF  : pygame.image.load('brownblock.png'),
                TOAD  : pygame.image.load('whiteblock.png')
            }
#maps

tilemaps = arbitrary
tilemap = arbitrar
tilemap2 = arbitrar2
#Click function
def click(x,y):
    x = (x-40)/40
    x = math.ceil(x)
    y = (y-240)/40
    y = math.ceil(y)
    yl = y-2,y,y-1
    xl = x-2,x,x-1
    for ax in range(0,4):
        for ay in range(0,4):
            if ax in xl and ay in yl:
                if tilemap2[ay][ax] == TOAD:
                    tilemap2[ay][ax] = LEAF
                elif tilemap2[ay][ax] == LEAF:
                    tilemap2[ay][ax] = TOAD
def nextpuzzle(aa,bb):
    global cc
    global dd
    if aa == bb:
        next = False
        for x in range(0,len(tilemaps)):
            if tilemaps[x] == [aa,bb]:
                next = True
                if x != len(tilemaps)-1:
                    cc = tilemaps[x+1][0]
                    dd = tilemaps[x+1][1]
            elif next == True:
                pass

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
        if event.type == pygame.MOUSEBUTTONDOWN:
            (x, y)= pygame.mouse.get_pos()
            click(x,y)
    if tilemap == tilemap2:
        nextpuzzle(tilemap,tilemap2)
        
        tilemap = cc
        tilemap2 = dd
        if tilemap2 == tilemaps[len(tilemaps)-1][0]:
            tilemap = [
            [TOAD,LEAF,TOAD,LEAF],
            [TOAD,TOAD,TOAD,TOAD],
            [TOAD,LEAF,TOAD,LEAF],
            [TOAD,TOAD,LEAF,TOAD]
          ]
            tilemap2 = [
            [TOAD,TOAD,TOAD,LEAF],
            [LEAF,TOAD,LEAF,TOAD],
            [TOAD,LEAF,TOAD,TOAD],
            [TOAD,TOAD,TOAD,TOAD]
          ]    
        
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