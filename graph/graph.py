from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def generateEdges(self):
        edges = []
        for node in self.graph:
            for neighbour in self.graph[node]:
                edges.append((node, neighbour))
        return edges

    def returnGraph(self):
        return self.graph

def visual(graph):
  for i in graph:
    for j in graph[i]:
      print('{} -> {}'.format(i, j), end=' ')
    print('')

def small():
  g = Graph()
  g.addEdge(0, 1)
  g.addEdge(0, 2)
  g.addEdge(1, 2)
  g.addEdge(2, 0)
  g.addEdge(2, 3)
  g.addEdge(3, 3)

  return g.returnGraph()

def big():
  g = Graph()
  g.addEdge(1, 3)
  g.addEdge(1, 2)
  g.addEdge(2, 1)
  g.addEdge(2, 4)
  g.addEdge(2, 5)
  g.addEdge(3, 5)
  g.addEdge(3, 1)
  g.addEdge(4, 2)
  g.addEdge(4, 5)
  g.addEdge(4, 6)
  g.addEdge(5, 6)
  g.addEdge(5, 3)
  g.addEdge(5, 2)
  g.addEdge(5, 4)
  g.addEdge(6, 4)
  g.addEdge(6, 5)

  return g.returnGraph()

def scc_graph():
  g = Graph()
  g.addEdge(7, 1)
  g.addEdge(4, 7)
  g.addEdge(1, 4)
  g.addEdge(9, 7)
  g.addEdge(6, 9)
  g.addEdge(3, 6)
  g.addEdge(9, 3)
  g.addEdge(8, 6)
  g.addEdge(2, 8)
  g.addEdge(5, 2)
  g.addEdge(8, 5)

  return g.returnGraph()

def scc_graph_test1():
    g = Graph()
    g.addEdge(1, 4)
    g.addEdge(2, 8)
    g.addEdge(3, 7)
    g.addEdge(3, 9)
    g.addEdge(4, 4)
    g.addEdge(4, 7)
    g.addEdge(5, 2)
    g.addEdge(6, 3)
    g.addEdge(7, 1)
    g.addEdge(8, 6)
    g.addEdge(8, 20)
    g.addEdge(9, 6)
    g.addEdge(10, 1)
    g.addEdge(10, 16)
    g.addEdge(11, 10)
    g.addEdge(12, 11)
    g.addEdge(1, 15)
    g.addEdge(13, 17)
    g.addEdge(13, 18)
    g.addEdge(14, 13)
    g.addEdge(15, 17)
    g.addEdge(16, 11)
    g.addEdge(17, 12)
    g.addEdge(18, 14)
    g.addEdge(19, 5)
    g.addEdge(20, 19)

    return g.returnGraph()