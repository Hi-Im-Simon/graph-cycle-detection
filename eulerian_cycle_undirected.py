from collections import defaultdict
import time


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

    # A DFS based function to count reachable vertices from v
    def DFSCount(self, v, visited):
        count = 1
        visited[v] = True
        for i in self.graph[v]:
            if visited[i] == False:
                count = count + self.DFSCount(i, visited)
        return count

    def isValidNextEdge(self, v1, v2):
        if len(self.graph[v1]) == 1:
            return True
        else:
            '''
             2) If there are multiple adjacents, then u-v is not a bridge
                 Do following steps to check if u-v is a bridge
   
            2.a) count of vertices reachable from v1'''
            visited = [False]*(self.vert)
            count1 = self.DFSCount(v1, visited)

            '''2.b) Remove edge (v1, v2) and after removing the edge, count
                vertices reachable from v1'''
            self.removeEdge(v1, v2)
            visited = [False]*(self.vert)
            count2 = self.DFSCount(v1, visited)

            #2.c) Add the edge back to the graph
            self.addEdge(v1, v2)

            if count1 > count2:
                return False
            else:
                return True

    def eulSearch(self, v1):
        for v2 in self.graph[v1]:
            if self.isValidNextEdge(v1, v2):
                print(str(v1) + "-" + str(v2), end=" "),
                self.removeEdge(v1, v2)
                self.eulSearch(v2)
                break

    def findEulCycle(self):
        for i in range(self.vert):
            if len(self.graph[i]) % 2 != 0:
                print('There is no Eulerian cycle for this graph')
                return

        for i in range(self.vert):
            if len(self.graph[i]) > 0:
                start = i
                break
                
        self.eulSearch(start)


# Graph generator
for i in range(1, 2):
    file = [[int(x) for x in line.split()] for line in open("graphs/" + str(i) + ".txt").readlines()]

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
    # Complexity : O(V+E)
