#! /usr/bin/python3.7m

import ST

class GRAPH:

    def __init__(self, n):
        self.mat = []
        self.vertexNum = n
        for i in range(n):
            self.mat.append([])
            for j in range(n):
                self.mat[i].append(0)
    
    def insVertex(self, v1, v2, st):
        n1 = st.getPosition(v1)
        n2 = st.getPosition(v2)

        self.mat[n1][n2] = 1
        self.mat[n2][n1] = 1

    def getMatrix(self):
        return self.mat

    def getVertexNum(self):
        return self.vertexNum

    @staticmethod
    def dfsRecursive(g, start, timePass, timeEnd, clock):
        clock += 1
        time[start] = clock

        print(start + "\n")

        for i in range(g.vertexNum):
            if(g.getMatrix()[start][i] != 0 and timePass[i] != 0):
                dfsRecursive(g, g.getMatrix()[start][i], timePass, timeEnd)
                
        timeEnd[start] = clock
        
    dfsRecursive = staticmethod(dfsRecursive)

    def DFS(self, start, timePass, timeEnd, clock):
        dfsRecursive(self, start, timePass, timeEnd, clock)
            