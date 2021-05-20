import time
from collections import defaultdict


class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.vert = vertices

    def addEdge(self, v1, v2):
        self.graph[v1].append(v2)
        self.graph[v2].append(v1)

    def removeEdge(self, v1, v2):
        for index, key in enumerate(self.graph[v1]):
            if key == v2:
                self.graph[v1].pop(index)
        for index, key in enumerate(self.graph[v2]):
            if key == v1:
                self.graph[v2].pop(index)

    def DFScheck(self, v, visited):                                         # oznaczamy wierzchołek jako odwiedzony
        visited[v] = True                                                   # dla każdego nieodwiedzonego sąsiada aktualnego wierzchołka znów przeprowadzamy DFS
        for u in self.graph[v]:
            if not visited[u]:
                self.DFScheck(u, visited)

    def isConnected(self):
        visited = [False] * self.vert                                       # tworzenie listy odwiedzonych wierzchołków
        v = list(self.graph.keys())[0]                                      # pierwszy wierzchołek
        self.DFScheck(v, visited)

        for u in range(self.vert):                                          # po DFS całego grafu, jeżeli jakikolwiek wierzchołek nie został odwiedzony, to przerywamy program
            if not visited[u]:
                return False
        return True

    def DFSEuler(self, v, result):
        for u in self.graph[v]:                                             # za pomocą DFS usuwamy po kolei krawędzie i tworzymy z nich listę przejścia po wierzchołkach
            self.removeEdge(v, u)
            self.DFSEuler(u, result)
        result.append(v)

    def findEulCycle(self):
        for i in range(self.vert):
            if len(self.graph[i]) % 2 != 0:                                 # jeżeli którykolwiek z wierzchołków ma nieparzystą liczbę połączeń, to nie ma cyklu Eulera
                print('There is no Eulerian cycle for this graph')
                return False
        if not self.isConnected():                                          # jeżeli po przeprowadzeniu DFS jakikolwiek wierzchołek nie został odwiedzony, to nie ma cyklu Eulera
            print('There is no Eulerian cycle for this graph')
            return False
        result = list()
        v = list(self.graph.keys())[0]
        self.DFSEuler(v, result)
        print(result)


# Graph generator
for i in range(1, 2):
    file = [[int(x) for x in line.split()]
            for line in open("graphs/" + str(i) + ".txt").readlines()]

    for i in range(len(file)):
        if i == 0:
            vertices = file[i][0]
            edges = file[i][1]
            g = Graph(vertices)
        else:
            g.addEdge(file[i][0] - 1, file[i][1] - 1)

    # Time measurement for test cases

    start = time.time()

    g.findEulCycle()

    print((time.time() - start))
