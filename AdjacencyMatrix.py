"""An implementation of the adjacency list representation of a graph"""
from Interfaces import Graph, List
import numpy as np
import copy
import ArrayList
import ArrayStack

class AdjacencyMatrix(object):
    def __init__(self, n):
        self.n = n
        self.a = np.zeros([n, n], np.bool_)
                
    def add_edge(self, i, j):
        self.a[i][j] = True
        
    def remove_edge(self, i, j):
        self.a[i][j] = False
        
    def has_edge(self, i, j):
        return self.a[i][j]

    def out_edges(self, i):
        l = ArrayList.ArrayList()
        for j in range(self.n):
            if self.has_edge(i,j):
                l.append(j)
        return l

    def in_edges(self, j):
        l = ArrayList.ArrayList()
        for i in range(self.n):
            if self.has_edge(i,j):
                l.append(i)
        return l
        
    def in_degree(self, i):
        deg = 0
        for j in range(self.n):
            if self.a[j][i]:
                deg = deg + 1
        return deg
        
    def out_degree(self, i):
        for j in range(self.n):
            if self.a[i][j]:
                deg = deg + 1
        return deg

    def size(self) -> int :
        return self.n
                  
    def __str__(self):
        s = ""
        for i in range(0, self.n):
            for j in range(0, self.n):
                if self.has_edge(i,j):
                    s += f"{i,j}"
        return s

'''
g = AdjacencyMatrix(6)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(0, 3)
g.add_edge(2, 4)
g.add_edge(4, 5)
g.add_edge(1, 4)
g.add_edge(4, 5)

print(g.dfs(0,1))

'''
