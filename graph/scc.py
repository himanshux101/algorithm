from collections import defaultdict

# directed graph 
class Graph():
    def __init__(self):
        self._graph = defaultdict(list)
        self._reverse_graph = defaultdict(list)
        self.finishing_times = None
    
    def add_edge(self, u, v):
        self._graph[u].append(v)
        self._reverse_graph[v].append(u)

    def __str__(self):
        return '{}({})'.format(self.__class__.__name__, dict(self._graph))

    def calculate_finishing_time(self):
        visited = set()
        stack = []
        for u in self._reverse_graph.keys():
            if u not in visited:
                self._dfs_finishing_times(u, visited, stack)
            
        self.finishing_times = stack

    def _dfs_finishing_times(self, u, visited, stack):
        visited.add(u)
        for i in self._reverse_graph[u]:
            if i not in visited:
                self._dfs_finishing_times(i, visited, stack)
        stack.append(u)

    def compute_scc(self):
        s = None
        visited = set()
        leader = defaultdict(list)
        for i in reversed(self.finishing_times):
            if i not in visited:
                s = i
                self._dfs_scc(i, visited, s, leader)
        
        return leader

    def _dfs_scc(self, u, visited, s, leader):
        visited.add(u)
        leader[s].append(u)
        for i in self._graph[u]:
            if i not in visited:
                self._dfs_scc(i, visited, s, leader)

    def iterative_finishing_time(self):
        visited = set()
        finishing_times = []
        node_stack = []
        for i in self._reverse_graph.keys():
            if i in visited:
                continue
            node_stack = [i]





if __name__ == "__main__":
    g = Graph()
    # g.add_edge(7, 1)
    # g.add_edge(4, 7)
    # g.add_edge(1, 4)
    # g.add_edge(9, 7)
    # g.add_edge(6, 9)
    # g.add_edge(3, 6)
    # g.add_edge(9, 3)
    # g.add_edge(8, 6)
    # g.add_edge(2, 8)
    # g.add_edge(5, 2)
    # g.add_edge(8, 5)
    with open("SCC.txt") as file:
        lines = file.readlines()
    outside = [line.rstrip(" \n").split(" ") for line in lines]
    for inner in outside:
        g.add_edge(inner[0], inner[1])

    print("graph build --- Done")
    
    g.calculate_finishing_time()
    print("Finishing time --- Done")
    leader = g.compute_scc()
    print("Leader calculate --- Done")

    print("Calculating the biggest scc")
    inter = []
    for i in leader.keys():
        inter.append(len(leader[i]))

    print(reversed(inter[:10]))