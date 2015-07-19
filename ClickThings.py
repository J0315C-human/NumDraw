from random import choice, randint
import pygame, sys
from pygame.locals import *
from Bases import *
from VectorSet import *
from NumSelect import *
from Globals import *


class knobHandler:
    def __init__(self, vectorSet):
        self.hasItem = False
        self.Item = None #will be of type digitVector
        self.vectorSet = vectorSet
        
    def getKnob(self):
        for n in range(self.vectorSet.base):
            x, y = pygame.mouse.get_pos()
            xdiff = abs(DIALPOS[0] + self.vectorSet[n].x() - x)
            ydiff = abs(DIALPOS[1] + self.vectorSet[n].y() - y)
            if xdiff < 7 and ydiff < 7:
                self.Item = self.vectorSet[n]
                self.hasItem = True
                #print("item is now " + str(self.vectorSet[n]))
                return True
        return False # No item under mouse.
    
    def doubleClicked(self):
        if self.getKnob():
            self.Item.toggle()
        self.Item = None
        self.hasItem = False
    def Down(self):
        if not self.hasItem:
            self.getKnob()
    def Move(self):
        if self.hasItem:
            self.Item.setToMouse()
    def Up(self):
        self.hasItem = False

class numSelectHandler(object):
    def __init__(self, listObjectsToHandle):
        self.selectors = listObjectsToHandle

    def click(self):
        x, y = pygame.mouse.get_pos()

        for Obj in self.selectors:
            # if x within 15 of middle or y within 5 of middle
            upx, upy = Obj.upPos()
            dwnx, dwny = Obj.downPos()
            
            if abs(x- upx) <= 15 and abs(y-upy) <= 5:
                Obj.increment()
                return
            elif abs(x - dwnx) <= 15 and abs(y-dwny) <= 5:
                Obj.decrement()
                return
            
    def motion(self):
        x, y = pygame.mouse.get_pos()

        for Obj in self.selectors:
            # if x within 15 of middle or y within 5 of middle
            upx, upy = Obj.upPos()
            dwnx, dwny = Obj.downPos()
            
            if abs(x- upx) <= 15 and abs(y-upy) <= 5:
                Obj.u_active()
                return
            elif abs(x - dwnx) <= 15 and abs(y-dwny) <= 5:
                Obj.d_active()
                return
            else:
                Obj.inactive()














