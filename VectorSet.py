from random import choice, randint
from math import sqrt, sin, cos, hypot, atan2, degrees, radians
import pygame, sys
from pygame.locals import *
from Bases import *
from Globals import *

##
##ANGLEINCR = 10   #for vector assignments
##DISTANCEINCR = 7 # "
##MAXDISTANCE = 14 #number of DISTANCEINCR
##DIALPOS = (100, 400)


class digitVector(object):
    def __init__(self, angle, distance):
        self.setValues(angle, distance)
        self.enabled = True
  
    def toggle(self):
        self.enabled = not (self.enabled)
    def setValues(self, a, d):
        self.angle = a % 360
        self.distance = d
        self.quantize()
    
    def setToMouse(self):
        
        #move angle and distance to where the mouse is.
        xpos, ypos = pygame.mouse.get_pos()
        delta_x, delta_y = xpos - DIALPOS[0], DIALPOS[1] - ypos
        l_angle = atan2(delta_x, delta_y)
        l_dist = hypot(delta_x, delta_y)
        l_angle = degrees(l_angle)
        # the 90 deg. is to adjust for pygame's default 0 degrees.
        self.setValues(l_angle - 90, l_dist)
      
    def quantize(self):
        #make sure the angle and distance are multiples of discrete values
        l_angle = round(self.angle / ANGLEINCR, 0) * ANGLEINCR
        l_distance = round(self.distance / DISTANCEINCR, 0) * DISTANCEINCR
        if l_distance > (MAXDISTANCE * DISTANCEINCR):
            l_distance = MAXDISTANCE * DISTANCEINCR
        self.angle = l_angle
        self.distance = l_distance
    def x(self):
        return cos(radians(self.angle)) * self.distance # ***check for radians vs degrees issue
    def y(self):
        return sin(radians(self.angle)) * self.distance
    def __repr__(self):
        return "angle: " + str(self.angle) + " distance: " + str(self.distance) + "\n"



class VectorSet(object):
    def __init__(self, countingBase):
        self.base = countingBase
        self.digits = dict()
        self.randomize(0, self.base)

    def __getitem__(self, i):
        return self.digits[i]
    def __setitem__(self, i, angleDistTuple):
        if i < self.base and i >= 0:
            self.digits[i] = digitVector(*angleDistTuple)

    def setBase(self, newBase):
        if newBase == self.base:
            return
        elif newBase < self.base:   # remove higher vectors
            keys = list(self.digits.keys())
            for dig in keys:
                if dig > newBase:
                    self.digits.pop(dig)
        elif newBase > self.base:   # add remaining random vectors
            self.randomize(self.base, newBase)
        self.base = newBase
        
    def randomize(self, start, end):
        #clear and rebuild a range of digitVectors
        for i in range(start, end):
            keys = list(self.digits.keys())
            if i in keys:
                self.digits.pop(i)
        for n in range(start, end):
            again = True
            count = 0
            while again:
                again = False
                l_angle = randint(0, 360//ANGLEINCR) * ANGLEINCR
                l_distance = randint(0, MAXDISTANCE) * DISTANCEINCR
                #print("v#" + str(n) + ": " + str(l_angle) + " and " + str(l_distance))
                for m in self.digits:
                    if self.digits[m].angle == l_angle and self.digits[m].distance == l_distance:
                        again = True
                        count += 1
                        if count >40:
                            print("Not enough unique random values!")
                            raise IndexError
            self.digits[n] = digitVector(l_angle, l_distance)
    def __repr__(self):
        s = ""
        for d in range(0, self.base):
            s+= str(d) + " " + str(self.digits[d])
        return s











