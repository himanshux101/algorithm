from graph import *
from collections import defaultdict

def inverserGraph(graph):
  inv = Graph()
  for i in graph:
      for j in graph[i]:
        inv.addEdge(j, i)
  return inv.returnGraph()

t = 0
s = None
def DFSLoop(graph):
  inv = inverserGraph(graph)
  visited = [False] * (len(graph))
  f = [0 for i in range(len(graph))]
  stack = []
  for i in range(len(inv), 0, -1):
  # for i in range(len(inv)):
    if visited[i-1] == False:
      DFS_finishing_times(inv, i, visited, stack, f)
  print(f)
  print(stack)
  global s
  s = None
  visited = [False] * (len(graph))
  # leader = [0 for i in range(len(graph))]
  leader = defaultdict(list)
  # see the top element stack[-1]
  while stack:
    i = stack.pop()
    if visited[i-1] == False:
      s = i
      DFS(graph, i, leader, visited, f)
  
  return leader


def DFS(graph, i, leader, visited, f):
  global s
  visited[i-1] = True
  # x = f[s-1]
  leader[s].append(i)
  for j in graph[i]:
    if visited[j-1] == False:
      DFS(graph, j, leader, visited, f)

def DFS_finishing_times(graph, i, visited, stack, f):
  global t
  visited[i-1] = True
  for j in graph[i]:
    if visited[j-1] == False:
      DFS_finishing_times(graph, j, visited, stack, f)
  t += 1
  f[i-1] = t
  stack.append(i)

def addEdge(graph, u, v):
  graph[u].append(v)

def generateGraph():
  graph = defaultdict(list)
  with open("SCC.txt") as file:
      lines = file.readlines()

  outside = [line.rstrip(" \n").split(" ") for line in lines]
  for inner in outside:
      addEdge(graph, inner[0], inner[1])

  return graph

graph = scc_graph_test1()
# visual(graph)
leader = DFSLoop(graph)
print(leader)
x = [len(leader[i]) for i in leader]
print(x)

# def Nmaxelements(list1, N): 
#   final_list = []
#   for i in range(0, N):
#     max1 = 0
#     for j in range(len(list1)):
#       if list1[j] > max1:
#         max1 = list1[j];
#       list1.remove(max1);
#       final_list.append(max1)
  
#   print(final_list)

# Nmaxelements(x, 5)



