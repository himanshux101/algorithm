"""
BFS uses stack 
"""
from collections import defaultdict, deque
from graph import *

# number graph zero indexed
def BFS(graph, s):
    visited = [False] * (len(graph))

    queue = deque()
    queue.append(s)
    visited[s] = True

    while queue:
        v = queue.popleft()
        print(v)

        for i in graph[v]:
            if visited[i] == False:
                visited[i] = True
                queue.append(i)

# s to v
# graph number starts from 1 not 0
def BFS_shortes_path(graph, s, v):
    visited = [False] * (len(graph))
    dist = defaultdict(int)
    if s == v:
        dist[v] = 0
    else:
        dist[v] = -99

    queue = deque()
    queue.append(s)
    visited[s - 1] = True

    while queue:
        v = queue.popleft()
        print(v)

        for i in graph[v]:
            print("i is {}".format(i))
            if visited[i - 1] == False:
                visited[i - 1] = True
                dist[i] = dist[v] + 1
                queue.append(i)

    print("distance from {} to {} is {}".format(s, v, dist[v]))

graph = big()
print(len(graph))
BFS_shortes_path(graph, 1, 4)
