from collections import defaultdict

def addEdge(graph, u, v):
  graph[u].append(v)

graph = defaultdict(list)
with open("SCC.txt") as file:
    lines = file.readlines()

outside = [line.rstrip(" \n").split(" ") for line in lines]
for inner in outside:
    addEdge(graph, inner[0], inner[1])

print(graph)

# with open("SCC.txt") as file:
#     line = file.readline()


# line = line.rstrip(" \n").split(" ")

