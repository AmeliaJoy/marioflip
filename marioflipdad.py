import math
TOAD = 0
LEAF = 1
tilemap = [
            [TOAD,TOAD,LEAF,LEAF],
            [TOAD,LEAF,TOAD,LEAF],
            [TOAD,LEAF,LEAF,TOAD],
            [TOAD,TOAD,TOAD,TOAD]
          ]
def click(x,y):
    x = (x-40)/40
    if (x).is_integer:
        pass
    else: 
        x = math.ceil(x)
    y = (y-240)/40
    if (y).is_integer:
        pass
    else: 
        y = math.ceil(y)
    yl = y,y+1,y-1
    xl = x,x+1,x-1
    for ax in range(0,4):
        for ay in range(0,4):
            if ax in xl and ay in yl:
                if tilemap[ax][ay] == TOAD:
                    tilemap[ax][ay] = LEAF
                elif tilemap[ax][ay] == LEAF:
                    tilemap[ax][ay] = TOAD
    print(tilemap)

click(95,295)