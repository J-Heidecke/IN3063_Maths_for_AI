# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 20:14:32 2020

@author: heide
"""
# Import (limited) libraries
from random import seed
from random import randint
import numpy as np
import sys 

g = []
width = 3
height = 3
seed(6)

for row in range(height):
    g.append([])
    for column in range(width):
        g[row].append(randint(0,9))
        
# Convert to numpy.array
grid = np.array(g)
print(grid)

class Baseline():
    
    def __init__(self, graph):
        self.graph = graph
    
    # Algorithm goes down to last row, then right to last column -> finish
    def algorithm(self):
        src = [0,0]
        current = src
        timeSpent = 0 # Total time spent by algorithm
        X = current[1]
        y = current[0]
        
        # Go down through rows
        while(X != (height-1)):
            X += 1
            timeSpent += self.graph[X,y] # Value of field added to total
  
        # Go right through columns
        while(y != (width-1)):
            y += 1
            timeSpent += self.graph[X,y] # Value of field added to total
            
        return timeSpent

base = Baseline(grid)
result = base.algorithm()
print(result)
    
