from graph import *

def inverserGraph(graph):
  inv = Graph()
  for i in graph:
    for j in graph[i]:
      inv.addEdge(j, i)
  return inv.returnGraph() 

graph = scc_graph()
inv = inverserGraph(graph)

t = 0
s = None
def DFSLoop(graph):
  global t,s
  visited = [False] * (len(graph))
  leader = [0 for i in range(len(graph))]
  f = [0 for i in range(len(graph))]
  
  for i in range(len(graph), 0, -1):
    if visited[i-1] == False:
      s = i
      DFS(graph, i, leader, visited, f)

  return leader, f

def DFS(graph, i, leader, visited, f):
  global t,s
  visited[i-1] = True
  leader[i-1] = s
  for j in graph[i]:
    print(j)
    if visited[j-1] == False:
      DFS(graph, j, leader, visited, f)
  t += 1
  f[i-1] = t

leader, f = DFSLoop(inv)
print(leader)
print(f)



