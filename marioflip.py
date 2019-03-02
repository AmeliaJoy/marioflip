import pygame, sys
from pygame.locals import *
 
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
 
#a list representing our tilemap

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

b = tilemap 
c = tilemap2    
#useful game dimensions
TILESIZE  = 40
MAPWIDTH  = 4
MAPHEIGHT = 4
tilemaps = []
tilemaps2 = [tilemap,tilemap2]
tilemaps.append(tilemaps2)
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
d = tilemap
e = tilemap2
tilemaps2 = [tilemap,tilemap2]
tilemaps.append(tilemaps2)
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
f = tilemap
g = tilemap2
tilemap = b
tilemap2 = c
tilemaps2 = [tilemap,tilemap2]
tilemaps.append(tilemaps2)
tilemap = [
            [TOAD,TOAD,TOAD,TOAD],
            [TOAD,TOAD,TOAD,TOAD],
            [TOAD,TOAD,TOAD,TOAD],
            [TOAD,TOAD,TOAD,TOAD]
          ]
tilemap2 = [
            [TOAD,TOAD,TOAD,TOAD],
            [TOAD,LEAF,TOAD,LEAF],
            [TOAD,TOAD,TOAD,TOAD],
            [TOAD,TOAD,TOAD,TOAD]
          ]
H = tilemap
i = tilemap2
tilemap = b
tilemap2 = c
tilemaps2 = [tilemap,tilemap2]
tilemaps.append(tilemaps2)
#click functions

def oneone():
    for ax in range(0,4):
        for ay in range(0,4):
            if ax <= 1 and ay <= 1:
                if tilemap2[ay][ax] == TOAD:
                    tilemap2[ay][ax] = LEAF
                elif tilemap2[ay][ax] == LEAF:
                    tilemap2[ay][ax] = TOAD
def twoone():
    for ax in range(0,4):
        for ay in range(0,4):
            if ax <= 2 and ay <= 1:
                if tilemap2[ay][ax] == TOAD:
                    tilemap2[ay][ax] = LEAF
                elif tilemap2[ay][ax] == LEAF:
                    tilemap2[ay][ax] = TOAD        
def threeone():
    for ax in range(0,4):
        for ay in range(0,4):
            if ay <= 1 and ax >= 1:
                if tilemap2[ay][ax] == TOAD:
                    tilemap2[ay][ax] = LEAF
                elif tilemap2[ay][ax] == LEAF:
                    tilemap2[ay][ax] = TOAD
def fourone():
    for ax in range(0,4):
        for ay in range(0,4):
            if ay <= 1 and ax >= 2:
                if tilemap2[ay][ax] == TOAD:
                    tilemap2[ay][ax] = LEAF
                elif tilemap2[ay][ax] == LEAF:
                    tilemap2[ay][ax] = TOAD
def onetwo():
    for ax in range(0,4):
        for ay in range(0,4):
            if ax <= 1 and ay <= 2:
                if tilemap2[ay][ax] == TOAD:
                    tilemap2[ay][ax] = LEAF
                elif tilemap2[ay][ax] == LEAF:
                    tilemap2[ay][ax] = TOAD
def twotwo():
    for ax in range(0,4):
        for ay in range(0,4):
            if ay <= 2 and ax <= 2:
                if tilemap2[ay][ax] == TOAD:
                    tilemap2[ay][ax] = LEAF
                elif tilemap2[ay][ax] == LEAF:
                    tilemap2[ay][ax] = TOAD  
def threetwo():
    for ax in range(0,4):
        for ay in range(0,4):
            if ay <= 2 and ax >= 1:
                if tilemap2[ay][ax] == TOAD:
                    tilemap2[ay][ax] = LEAF
                elif tilemap2[ay][ax] == LEAF:
                    tilemap2[ay][ax] = TOAD  
def fourtwo():
    for ax in range(0,4):
        for ay in range(0,4):
            if ay <= 2 and ax >= 2:
                if tilemap2[ay][ax] == TOAD:
                    tilemap2[ay][ax] = LEAF
                elif tilemap2[ay][ax] == LEAF:
                    tilemap2[ay][ax] = TOAD 
def onethree():
    for ax in range(0,4):
        for ay in range(0,4):
            if ax <= 1 and ay >= 1:
                if tilemap2[ay][ax] == TOAD:
                    tilemap2[ay][ax] = LEAF
                elif tilemap2[ay][ax] == LEAF:
                    tilemap2[ay][ax] = TOAD
def twothree():
    for ax in range(0,4):
        for ay in range(0,4):
            if ay >= 1 and ax <= 2:
                if tilemap2[ay][ax] == TOAD:
                    tilemap2[ay][ax] = LEAF
                elif tilemap2[ay][ax] == LEAF:
                    tilemap2[ay][ax] = TOAD 
def threethree():
    for ax in range(0,4):
        for ay in range(0,4):
            if ay >= 1 and ax >= 1:
                if tilemap2[ay][ax] == TOAD:
                    tilemap2[ay][ax] = LEAF
                elif tilemap2[ay][ax] == LEAF:
                    tilemap2[ay][ax] = TOAD 
def fourthree():
    for ax in range(0,4):
        for ay in range(0,4):
            if ay >= 1 and ax >= 2:
                if tilemap2[ay][ax] == TOAD:
                    tilemap2[ay][ax] = LEAF
                elif tilemap2[ay][ax] == LEAF:
                    tilemap2[ay][ax] = TOAD 
def onefour():
    for ax in range(0,4):
        for ay in range(0,4):
            if ax <= 1 and ay >= 2:
                if tilemap2[ay][ax] == TOAD:
                    tilemap2[ay][ax] = LEAF
                elif tilemap2[ay][ax] == LEAF:
                    tilemap2[ay][ax] = TOAD         
def twofour():
    for ax in range(0,4):
        for ay in range(0,4):
            if ax <= 2 and ay >= 2:
                if tilemap2[ay][ax] == TOAD:
                    tilemap2[ay][ax] = LEAF
                elif tilemap2[ay][ax] == LEAF:
                    tilemap2[ay][ax] = TOAD         
def threefour():
    for ax in range(0,4):
        for ay in range(0,4):
            if ax >= 1 and ay >= 2:
                if tilemap2[ay][ax] == TOAD:
                    tilemap2[ay][ax] = LEAF
                elif tilemap2[ay][ax] == LEAF:
                    tilemap2[ay][ax] = TOAD   
def fourfour():
    for ax in range(0,4):
        for ay in range(0,4):
            if ax >= 2 and ay >= 2:
                if tilemap2[ay][ax] == TOAD:
                    tilemap2[ay][ax] = LEAF
                elif tilemap2[ay][ax] == LEAF:
                    tilemap2[ay][ax] = TOAD   

def nextpuzzle():
    global tilemap2
    global tilemap
    print(tilemap2)
    print(tilemap)
    for x in range(0,len(tilemaps)):
        if tilemap2 in tilemaps[x]:
            if len(tilemaps) == x+1:
                pass
            else:
                tilemap = tilemaps[x+1][0]
                tilemap2 = tilemaps[x+1][1]
#set up the display
pygame.init()
DISPLAYSURF = pygame.display.set_mode((MAPWIDTH*TILESIZE+80,MAPHEIGHT*TILESIZE+280))
DISPLAYSURF.fill(BLUE) 
while True:
    
    

    #get all the user events
    for event in pygame.event.get():
        #if the user wants to quit
        a = False
        if tilemap2 == tilemap:
            print(tilemaps)
            for x in range(0, len(tilemaps)):
                if a == True:
                    print(tilemaps[x][0])
                    tilemap = tilemaps[x][0]
                    tilemap2 = tilemaps[x][1]
                    break
                if tilemap2 == tilemaps[x][0]:
                    print('c')
                    a = True
                        
                        
        if event.type == QUIT:
            #and the game and close the window
            pygame.quit()
            sys.exit()
        (x, y)= pygame.mouse.get_pos()
        if x > 40 and x < 80 and y > 240 and y < 280 and event.type == pygame.MOUSEBUTTONDOWN:
            oneone()
        elif x > 80 and x < 120 and y > 240 and y < 280 and event.type == pygame.MOUSEBUTTONDOWN:
            twoone()
        elif x > 120 and x < 160 and y > 240 and y < 280 and event.type == pygame.MOUSEBUTTONDOWN:
            threeone()
        elif x > 160 and x < 200 and y > 240 and y < 280 and event.type == pygame.MOUSEBUTTONDOWN:
            fourone()
        elif x > 40 and x < 80 and y > 280 and y < 320 and event.type == pygame.MOUSEBUTTONDOWN:
            onetwo()
        elif x > 80 and x < 120 and y > 280 and y < 320 and event.type == pygame.MOUSEBUTTONDOWN:
            twotwo()
        elif x > 120 and x < 160 and y > 280 and y < 320 and event.type == pygame.MOUSEBUTTONDOWN:
            threetwo()
        elif x > 160 and x < 200 and y > 280 and y < 320 and event.type == pygame.MOUSEBUTTONDOWN:
            fourtwo()
        elif x > 40 and x < 80 and y > 320 and y < 360 and event.type == pygame.MOUSEBUTTONDOWN:
            onethree()
        elif x > 80 and x < 120 and y > 320 and y < 360 and event.type == pygame.MOUSEBUTTONDOWN:
            twothree()
        elif x > 120 and x < 160 and y > 320 and y < 360 and event.type == pygame.MOUSEBUTTONDOWN:
            threethree()
        elif x > 160 and x < 240 and y > 320 and y < 360 and event.type == pygame.MOUSEBUTTONDOWN:
            fourthree()
        elif x > 40 and x < 80 and y > 360 and y < 400 and event.type == pygame.MOUSEBUTTONDOWN:
            onefour()
        elif x > 80 and x < 120 and y > 360 and y < 400 and event.type == pygame.MOUSEBUTTONDOWN:
            twofour()
        elif x > 120 and x < 160 and y > 360 and y < 400 and event.type == pygame.MOUSEBUTTONDOWN:
            threefour()
        elif x > 160 and x < 200 and y > 360 and y < 400 and event.type == pygame.MOUSEBUTTONDOWN:
            fourfour()
 
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
