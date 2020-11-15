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

'''
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
'''
width = 10
height = 10
seed(6)

def make_grid(h, w):
    g = []
    for r in range(h):
        g.append([])
        for c in range(w):
            g[r].append(randint(0,9))
            
    output = np.array(g)   
    return output

grid = make_grid(height, width)

class Convert:
    
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
    if start == end:
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

d = Convert(grid, src, finish)
graph = d.convert_grid()

print (shortestpath(graph,str(s),str(e)))


# -- Dijkstra new ---

# https://www.youtube.com/watch?v=IG1QioWSXRI
def dijkstra(graph, start, goal):
    shortest_distance = {}
    predecessor = {}
    unseenNodes = list(graph.keys())
    inf = 999999
    path = []
    
    for node in unseenNodes:
        shortest_distance[node] = inf
    shortest_distance[start] = 0
    
    while unseenNodes:
        minNode = None
        for node in unseenNodes:
            if minNode is None:
                minNode = node
            elif shortest_distance[node] < shortest_distance[minNode]:
                minNode = node

        for childNode, weight in graph[minNode].items():
            if weight + shortest_distance[minNode] < shortest_distance[childNode]:
                shortest_distance[childNode] = weight + shortest_distance[minNode]
                predecessor[childNode] = minNode
        unseenNodes.remove(minNode)
    
    current = goal
    while current != start:
        try:
            path.insert(0, current)
            current = predecessor[current]
        except KeyError:
            print('Path not readable')
            break
    path.insert(0, start)

    if shortest_distance[goal] != inf:
        print(shortest_distance[goal])



test = make_grid(4,4)
src = [0,0]
finish = [4,4]
d = Convert(test, src, finish)
graph = d.convert_grid()
dijkstra(graph, '0', '202')
'''
paths = []
for i in range(3,101):
    src_ = [0,0]
    finish_ = [i, i]
    grid_ = make_grid(i, i)
    d_ = Convert(grid_, src_, finish_)
    graph_ = d.convert_grid()
    s_ = (src_[0] * 100) + src_[1]
    e_ = ((finish_[0] * 100) + finish_[1]) - 101
    
    paths.append(dijkstra(graph_, str(s_), str(e_)))
print(paths)
'''
# -- Analytics ---
'''
class Analytics:
    
    def __init__(self, algorithm):
        self.algorithm = algorithm
    
    def make_grid(self,w, h):
        g = []
        seed(70)
        for r in range(w):
            g.append([])
            for c in range(h):
                g[r].append(randint(0,9))
            
        output = np.array(g)   
        return output
    
    def ant(self):
        pass;

    def dijkstra(self):
        pass;
    
    def baseline(self):
        paths = []
    
        for i in range(3, 101):
            grid = self.make_grid(i,i)
            b = Baseline(grid)
            path = b.algorithm()
            paths.append(path)

        return paths
            
    def run(self):
        if(self.algorithm == 'base'):
            baseline_results = self.baseline()
            return baseline_results
        elif(self.algorithm == 'dijk'):
            dijkstra_results =  self.dijkstra()
            return dijkstra_results
        elif(self.algorithm == 'ant'):
            print('Not implemented yet')
        else:
            print('Algorithm not defined')
    
    def plot(self):
        results = self.run()
        plt.plot(results)
        plt.xlabel('Run')
        plt.ylabel('Length of Path Selected')
        
        return ('Mean: %.2f' %np.mean(results))
    
analytics = Analytics('base')
analytics.plot()
'''