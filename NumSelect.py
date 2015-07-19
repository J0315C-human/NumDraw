from random import choice, randint
import pygame, sys
from pygame.locals import *
from copy import deepcopy
from math import sqrt, cos, sin, asin, acos, degrees, radians
from Globals import *
#class to represent a fixed up/down arrow selector.

class NumSelect(object):
    def __init__(self, positionTuple, minimum, maximum,
                 default = None, incr = 1, title = ""):
        self.pos = positionTuple
        self.x, self.y = positionTuple
        self.ucolor = (100, 100, 100)
        self.dcolor = (100, 100, 100)
        if maximum < minimum:
            maximum, minimum = minimum, maximum
        self.minimum = minimum
        self.maximum = maximum
        if default == None or default < minimum or default > maximum:
            self.state = minimum
        else:
            self.state = default
        self.incr = incr
        self.title = title

    def increment(self):
        self.state = min((self.maximum, self.state + self.incr))

    def decrement(self):
        self.state = max((self.minimum, self.state - self.incr))

    def upPos(self):
        return (self.x + 15, self.y + 5)
    
    def downPos(self):
        return (self.x + 15, self.y + 55)

    def draw(self, surface):
        if isinstance(self.incr, float):
            stateLabel = str(round(self.state, 1))
        else:
            stateLabel = str(self.state)
        
        BASICFONT = pygame.font.Font('freesansbold.ttf', BASICFONTSIZE)
        SMALLFONT = pygame.font.Font('freesansbold.ttf', SMALLFONTSIZE)
        tri1 = [(self.x, self.y+ 10), (self.x + 15, self.y),
                  (self.x + 30, self.y+10)]
        tri2 = [(self.x, self.y+ 50), (self.x + 15, self.y+60),
                  (self.x + 30, self.y+50)]
        box = [(self.x, self.y+15), (self.x, self.y + 45),
               (self.x+30, self.y+45), (self.x+30, self.y+ 15)]
        
        pygame.draw.polygon(surface, self.ucolor, tri1)
        pygame.draw.polygon(surface, self.dcolor, tri2)
        pygame.draw.polygon(surface, (120, 120, 120), box)
        textSurf = BASICFONT.render(stateLabel, True, WHITE)
        textRect = textSurf.get_rect()
        textRect.center = (self.x+15, self.y+32)
        surface.blit(textSurf, textRect)
        textSurf1 = SMALLFONT.render(str(self.title), True, WHITE)
        textRect1 = textSurf1.get_rect()
        textRect1.center = (self.x+15, self.y - 20)
        surface.blit(textSurf1, textRect1)
        
    def u_active(self):
        self.ucolor = (150, 150, 150)
    def d_active(self):
        self.dcolor = (150, 150, 150)
    def inactive(self):
        self.dcolor = (100, 100, 100)
        self.ucolor = (100, 100, 100)



                                
