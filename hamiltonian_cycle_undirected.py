import time


class Graph:
    def __init__(self, vertices):
        self.graph = [[0 for _ in range(vertices)] for _ in range(vertices)]
        self.vert = vertices

    def isSafe(self, v, pos, path):
        if self.graph[path[pos-1]][v] == 0:                 # sprawdzamy czy ostatnie 2 wierzchołki są połączon
            return False

        for vertex in path:                                 # sprawdzamy czy wierzchołek nie wystąpił już w cyklu
            if vertex == v:
                return False
        return True

    def hamSearch(self, path, pos):
        if pos == self.vert:                                # jeżeli jesteśmy na ostatnim wierzchołku (pos = ilość_wierzchołków)
            if self.graph[path[pos-1]][path[0]] == 1:       # sprawdzamy czy ostatni wierzchołek w cyklu łączy się z pierwszym
                return True
            else:
                return False

        for v in range(1, self.vert):                       # dla każdego wierzchołka
            if self.isSafe(v, pos, path) == True:           # sprawdzamy czy ostatnie 2 wierzchołki są połączone i czy wierzchołek nie wystąpił już w cyklu
                path[pos] = v                               # wstawiamy aktualny wierzchołek na koniec cyklu
                if self.hamSearch(path, pos+1) == True:     # wykonujemy funkcję dla elementu cyklu...
                    return True
                else:
                    path[pos] = -1                          # jeżeli nie pasuje, usuwamy wierzchołek z końca cyklu
        return False

    def findHamCycle(self):
        path = [0] + [-1] * (self.vert - 1)                 # -1 to id wierzchołka, który nie istnieje + ustawiamy, że zaczynamy od wierzchołka 0

        if self.hamSearch(path, 1) == False:
            print("There is no Hamiltonian cycle for this graph")
        else:
            for vertex in path:
                print(vertex, end=" ")
            print(path[0])
        

# Graph generator
for i in range(1, 6):
    file = [[int(x) for x in line.split()] for line in open("graphs/" + str(i) + ".txt").readlines()]

    for i in range(len(file)):
        if i == 0:
            v = file[i][0]
            g = Graph(v)
            graph = [[0 for _ in range(v)] for _ in range(v)]
        else:
            graph[file[i][0] - 1][file[i][1] - 1] = 1
            graph[file[i][1] - 1][file[i][0] - 1] = 1

    g.graph = graph

# Time measurement for test cases

    start = time.time()

    g.findHamCycle()

    print((time.time() - start))
