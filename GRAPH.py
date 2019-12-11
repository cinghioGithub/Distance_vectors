#! /usr/bin/python3.7m

import ST
import sys

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

    def BFS(self, start, timePass, timeEnd, clock):
        clock += 1
        timePass[start] = clock

        print(start,end="\n")

        for i in range(self.vertexNum):
            if(self.getMatrix()[start][i] != 0 and timePass[i] == 0):
                self.BFS(i, timePass, timeEnd, clock)
                
        timeEnd[start] = clock

    def distanceVector(self, start, destintion, vet):
        vet[start] = 1

        if (start == destintion):
            return 0

        mat = self.getMatrix()
        num = self.getVertexNum()
        MaxDist = sys.maxsize
        dist = 0

        for i in range(num):
            if(mat[start][i] != 0 and vet[i] == 0):
                dist = self.distanceVector(i, destintion, vet)

                #if(dist == 1+sys.maxsize):
                #    return sys.maxsize

                if(dist < MaxDist):
                    minDist = dist
        
        vet[start] = 0
        #if(minDist != sys.maxsize):
        return dist
        #else:
        #    return dist