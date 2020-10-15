from collections import defaultdict
import random

def addEdge(graph, u, v):
    graph[u].append(v)

def genrateGraph():
    graph = defaultdict(list)

    with open('kargerMinCut.txt') as file:
        lines = file.readlines()

    outside = [line.rstrip('\t\n').split('\t') for line in lines]
    
    for inner in outside: 
        for node in inner[1:]:
            addEdge(graph, inner[0], node)
    return graph

def generateEdges(graph):
    edges = []
    for node in graph:
        for neighbour in graph[node]:
            edges.append((node, neighbour))
    return edges

def randomContraction(graph):
    while len(graph) > 2:
        edge = random.choice(generateEdges(graph))
        contract(graph, edge[0], edge[1])
        randomContraction(graph)

def contract(graph, first, second):
    graph[first]= [node for node in graph[first] if node != second]
    graph[second] = [node for node in graph[second] if node != first]

    new_name = first + second

    graph[new_name] = graph[first] + graph[second]

    del graph[first]
    del graph[second]

    for node in graph:
        for n, neighbour in enumerate(graph[node]):
            if neighbour == first or neighbour == second:
                graph[node][n] = new_name


graph = genrateGraph()
randomContraction(graph)
final = 0
print('len is ', len(graph))
for node in graph:
    final += len(graph[node]) / 2
print('total is ', final)
# print(g)