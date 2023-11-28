from level import Level
from level import Type
from numpy import random


class Person:

    def __init__(self, level):
        self.level = level
        self.neighbors = []
        self.isBeliever = False
        self.hear_count = 0
        self.L_count = 0
        self.isWaiting = False
        # self.place = None   # delete
        self.L = 0


    def hear(self):
        self.hear_count +=1


    def believe(self):
        if self.hear_count >= 2:
            if self.level.type != Type.S1:
                self.level.levelDown()
                self.isBeliever = random.choice([True, False],p = [self.level.getProb(), 1 - self.level.getProb()])
                self.level.levelUp()
            else:
                self.isBeliever = random.choice([True, False], p=[self.level.getProb(), 1 - self.level.getProb()])
        elif self.hear_count == 1:
            self.isBeliever = random.choice([True, False],p = [self.level.getProb(), 1 - self.level.getProb()])
        else: # if hear_count == 0
            self.isBeliever = False            
        self.hear_count = 0
        pass


    def spread(self):
        if self.L_count >= self.L:
            self.isWaiting = False
        if self.isWaiting:
            self.L_count +=1
        if not self.isWaiting and self.isBeliever:
            # spred the rumour
            for n in self.neighbors:
                n.hear()
            # zero the count
            self.isWaiting = True
            self.L_count = 0

        
            


            

