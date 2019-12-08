#! /usr/bin/python3.7m

import ST

class GRAPH:

    def __init__(self, n):
        self.mat = []
        vertexNum = n
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