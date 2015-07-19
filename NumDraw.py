from random import choice, randint
import pygame, sys
from pygame.locals import *
from copy import deepcopy
from math import sqrt, cos, sin, asin, acos, degrees, radians
from Bases import *
from VectorSet import *
from NumSelect import *
from Globals import *
from ClickThings import *

""" This is essentially an application of some doodling I was
    doing during Discrete Math II when we were covering binary 
    math, again. Pick a counting base, assign a different vector
    to each digit, and each vector gets drawn in the sequence
    (how to input sequences will be a tough part)"""

########All this file should have is drawing functions and main.

def drawDial(vectorset):
    pygame.draw.circle(DISPLAYSURF, DIALCOLOR1, DIALPOS, MAXDISTANCE * DISTANCEINCR + 10)
    for d in range(MAXDISTANCE):
        pygame.draw.circle(DISPLAYSURF, BGCOLOR, DIALPOS, d * DISTANCEINCR + 10, 1)
    #draw all lines
    for d in range(0, vectorset.base):
        knobPos = (int(vectorset[d].x() + DIALPOS[0]), int(vectorset[d].y() + DIALPOS[1]))
        pygame.draw.line(DISPLAYSURF, DIALCOLOR2, DIALPOS, (knobPos), 3)
    #draw all knobs
    for d in range(0, vectorset.base):
        knobPos = (int(vectorset[d].x() + DIALPOS[0]), int(vectorset[d].y() + DIALPOS[1]))
        if vectorset[d].enabled:
            pygame.draw.circle(DISPLAYSURF, DIALCOLOR3, knobPos, 10)
            textSurf = KNOBFONT.render(getStrChar(d), True, WHITE)
        else:   #Draw greyed out knob
            pygame.draw.circle(DISPLAYSURF, DIALCOLOR4, knobPos, 10)
            textSurf = KNOBFONT.render(getStrChar(d), True, OFFWHITE)
        textRect = textSurf.get_rect()
        textRect.center = knobPos
        DISPLAYSURF.blit(textSurf, textRect)

def drawSequenceBox(base, incr, start, length):
    nCols = 24
    nRows = 8
    vertIncr = 36
    #draw text box
    seq = getSequenceDisplay(base, incr, start, length, nCols, nRows)
    n = 0
    pygame.draw.rect(DISPLAYSURF, DIALCOLOR1, ((25, 520, 300, 300)))
    for y in range(545, 545 + (vertIncr * len(seq)), vertIncr):
        textSurf = BOXFONT.render(seq[n], True, OFFWHITE)
        textRect = textSurf.get_rect()
        textRect.center = (170, y)
        DISPLAYSURF.blit(textSurf, textRect)
        n += 1

def drawDiagram(Vectorset, base, incr, start, length, scale):
    seq = getSequenceStr(base, incr, start, length)
    x, y = DIAGRAMPOS
    scaleFactor = scale**3
    for i in range(len(seq)):
        #print("Base: ", base, " index: ", getNum(seq[i], base))
        digit = Vectorset[getNum(seq[i], base)] #index error?
        if digit.enabled == False:
            continue
        newPos = (x + digit.x()*scaleFactor, y + digit.y()*scaleFactor)
        pygame.draw.line(DISPLAYSURF, WHITE, (x, y), (newPos))
        x, y = newPos
        
def main(): #still copy-pasted and incomplete
    global FPSCLOCK, DISPLAYSURF, BASICFONT, BIGFONT, KNOBFONT, SMALLFONT, BOXFONT
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    KNOBFONT =  pygame.font.Font('freesansbold.ttf', KNOBFONTSIZE)
    SMALLFONT = pygame.font.Font('freesansbold.ttf', SMALLFONTSIZE)
    BOXFONT = pygame.font.SysFont('monospace', BOXFONTSIZE)
    BASICFONT = pygame.font.Font('freesansbold.ttf', BASICFONTSIZE)
    BIGFONT = pygame.font.Font('freesansbold.ttf', int(BASICFONTSIZE * 1.333))
    newBox = False

    
    V = VectorSet(10)

    BaseSel = NumSelect((20, 75), 2, 35, 10, 1, "Base")
    IncrSel = NumSelect((90, 75), 1, 1000, 1, 1, "Increment")
    StartSel = NumSelect((160, 75), 1, 10000, 0, 1, "Start")
    LengthSel = NumSelect((230, 75), 1, 1000, 40, 1, "Length")
    ScaleSel = NumSelect((300, 75), 0.1, 3, 0.75, 0.01, "Scale")
    numSelects = (BaseSel, IncrSel, StartSel, LengthSel, ScaleSel)
                         
    knobDrag = knobHandler(V)
    selectHandler = numSelectHandler(numSelects)
    clickDownCount = 0
    clickUpCount = 0
    while True:
        redraw = False
        for event in pygame.event.get(): # event handling loop
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN:
                knobDrag.Down()
                redraw = True
                
            elif event.type == MOUSEMOTION:
                knobDrag.Move()
                selectHandler.motion()
                redraw = True
                
            elif event.type == MOUSEBUTTONUP:
                knobDrag.Up()
                selectHandler.click()
                V.setBase(BaseSel.state)
                if clickUpCount < 7:
                    knobDrag.doubleClicked()
                redraw = True
                clickUpCount = 0
                clickDownCount = 0
                
        
        if pygame.mouse.get_pressed()[0] == 1:
            clickDownCount += 1
            redraw = True
           
            if (clickDownCount > 20 and clickDownCount % 7 == 0)\
                or (clickDownCount > 50 and clickDownCount % 4 == 0)\
                or (clickDownCount > 100 and clickDownCount % 2 == 0)\
                or clickDownCount > 300:
                selectHandler.click()
                V.setBase(BaseSel.state)
        else:
            clickUpCount += 1
        if redraw:
            DISPLAYSURF.fill(BGCOLOR) # drawing the window
            drawDial(V)
            for box in numSelects:
                box.draw(DISPLAYSURF)
            drawSequenceBox(BaseSel.state, IncrSel.state, StartSel.state, LengthSel.state)
            drawDiagram(V, BaseSel.state, IncrSel.state, StartSel.state, LengthSel.state, ScaleSel.state)
            pygame.display.update()
        else:
            FPSCLOCK.tick(100)
    return




if __name__ == "__main__":
    main()
    pygame.display.quit()
