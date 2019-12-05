#! /usr/bin/python3.7m

class ST:

    def __init__(self):
        self.dimention = 0
        self.mylist = []

    def getList(self):
        return self.mylist

    def getDimention(self):
        return self.dimention

    def insert(self, key):
        for i in range(self.dimention):
            if self.mylist[i] == key:
                return

        self.mylist.append(key)
        self.dimention += 1

    def getPosition(self, key):
        for i in range(self.dimention):
            if self.mylist[i] == key:
                break
        
        return i