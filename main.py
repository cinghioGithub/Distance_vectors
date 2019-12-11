#! /usr/bin/python3.7m

import ST
import GRAPH

def read_file(name, st):
    try:
        fp = open(name, "r")
    except:
        print('Error on opening file\n')
        quit()
    
    content = fp.readlines()

    for line in content:
        strlist = line.split()
        st.insert(strlist[0])
        st.insert(strlist[1])

def loadGraph(name, st, g):
    try:
        fp = open(name, "r")
    except:
        print('Error on opening file\n')
        quit()
    
    content = fp.readlines()

    for line in content:
        strlist = line.split()
        g.insVertex(strlist[0], strlist[1], st)

#main:

st = ST.ST()

name = 'file.txt'

read_file(name, st)

g = GRAPH.GRAPH(st.getDimention())
loadGraph(name, st, g)

timePass = []
for i in range(g.getVertexNum()):
    timePass.append(0)

timeEnd = []
for i in range(g.getVertexNum()):
    timeEnd.append(0)

clock = int(0)

vet = [0] * g.getVertexNum()

print(g.distanceVector(0, 3, vet))

#g.BFS(0, timePass, timeEnd, clock)

#print(g.getMatrix(), st.getDimention())