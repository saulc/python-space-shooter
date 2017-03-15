'''
Created on May 12, 2015

Level class to parse a level file for data

Level description

Level length

enemy 
posY%    type    howmany    width    spaceing

LevelMaker class to generate more levels by a few parameters.

@author: saul
'''

import os
import random

class Level:
    
    def __init__(self, levelNum):
        file = open(os.path.abspath("./levels/level" + str(levelNum) + ".dat"), 'r')
        self.length = int(file.readline())
        self.file = file
        items = []
        for l in file:
            tokens = l.split(" ")
            if len(tokens) >= 5:
                items.append(levelItem( self.length*int(tokens[0])/100, tokens[1], tokens[2], tokens[3], tokens[4] ) )
        self.items = items
        self.currentItem = 0
    
    def next(self):
        item = self.items[self.currentItem]
        self.currentItem += 1
        return item
    
    def peek(self):
        if self.currentItem < len(self.items):
            return self.items[self.currentItem]
        else: return 0
    
    def getLength(self):
        return self.length
            
class levelItem:
    def __init__(self,y, kind, howmany, group, space):
        self.type = int(kind)
        self.y = int(y)
        self.howMany = int(howmany)
        self.space = int(space)
        self.groupWidth = int(group)
        
        
class levelMaker:
    def __init__(self,number, length, intensity, density, ships, groups):
        self.number = number
        self.length = length
        self.intensity = intensity
        self.density = density
        self.ships = ships
        self.groups = groups
        self.makeLevel()

    def makeLevel(self):
        print('making level: ' + str(self.number))
        file = open(os.path.abspath("../levels/level" + str(self.number) + ".dat"), 'w')
       
        shipsPer = self.ships // self.groups
        
        avgspace = (self.length - self.intensity * self.groups) // self.density
        at = 0
        space = self.length //self.groups
        
        file.write(str(self.length) + '\n')
        
        for group in range(self.groups):
            file.write('{0} {1} {2} {3} {4}\n'.format(at, random.randint(1, 4), shipsPer, avgspace) )
            at += space
        file.close()
        
        
        

    
        