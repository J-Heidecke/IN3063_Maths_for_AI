# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 20:20:06 2020

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

class Dijkstra:
    
    def __init__(self, grid, source, finish):
        self.grid = grid
        self.src = source
        self.finish = finish
    
    def get_neighbors(self, location):
        neighbors = []
        if (location[0] + 1) < (height):
            neighbors.append([location[0] + 1, location[1]])
                              
        if (location[0] - 1) >= 0:
            neighbors.append([location[0]-1, location[1]])
            
        if (location[1] + 1) < (width):
            neighbors.append([location[0], location[1] + 1])
            
        if (location[1] - 1) >= 0:
            neighbors.append([location[0], location[1] - 1])
        
        return neighbors
    
    def get_edges(self, location):
        neighbors = self.get_neighbors(location)
        edges = []
        
        for i in neighbors:
            edges.append(self.grid[i[0], i[1]])
            
        return edges
      
    def get_name(self, location):
        node_name = (location[0] * 100) + location[1]
        return str(node_name)
    
    def make_node(self, location):
        
        neighbors = self.get_neighbors(location)
        edges = self.get_edges(location)
        neighbor_names = []
        node_name = self.get_name(location)
        
        for i in neighbors:
            neighbor_names.append(self.get_name(i))
            
        neighbor_edges = dict(zip(neighbor_names, edges))
        
        return node_name, neighbor_edges
    
    def convert_grid(self):
        nodes = {}
        for i in range(self.finish[0]):
            for j in range(self.finish[1]):
                node = self.make_node([i,j])
                nodes[node[0]] = node[1]
        
        return nodes
    
src = [0,0]
finish = [height, width]
s = (src[0] * 100) + src[1]
e = ((finish[0] * 100) + finish[1]) - 101

def shortestpath(graph,start,end,visited=[],distances={},predecessors={}):
    """Find the shortest path btw start & end nodes in a graph"""
    # detect if first time through, set current distance to zero
    if not visited: distances[start]=0
    # if we've found our end node, find the path to it, and return
    if start==end:
        path=[]
        while end != None:
            path.append(end)
            end=predecessors.get(end,None)
        return distances[start], path[::-1]
    # process neighbors as per algorithm, keep track of predecessors
    for neighbor in graph[start]:
        if neighbor not in visited:
            neighbordist = distances.get(neighbor,sys.maxsize)
            tentativedist = distances[start] + graph[start][neighbor]
            if tentativedist < neighbordist:
                distances[neighbor] = tentativedist
                predecessors[neighbor]=start
    # neighbors processed, now mark the current node as visited 
    visited.append(start)
    # finds the closest unvisited node to the start 
    unvisiteds = dict((k, distances.get(k,sys.maxsize)) for k in graph if k not in visited)
    closestnode = min(unvisiteds, key=unvisiteds.get)
    # now take the closest node and recurse, making it current 
    return shortestpath(graph,closestnode,end,visited,distances,predecessors)

d = Dijkstra(grid, src, finish)
graph = d.convert_grid()

print (shortestpath(graph,str(s),str(e)))