"""
DFS uses stack 
"""
from graph import *

# number graph zero indexed
def DFSLoop(graph):
    visited = [False] * (len(graph))
    for u in graph:
      DFS(graph, u, visited)

def DFS(graph, u, visited):
  visited[u-1] = True
  print(u)
  for i in graph[u]:
    if visited[i-1] == False:
      DFS(graph, i, visited)

graph = big()
DFSLoop(graph)
