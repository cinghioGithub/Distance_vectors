#! /usr/bin/python3.7m

import ST

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

#main:

st = ST.ST()
name = 'file.txt'

read_file(name, st)

