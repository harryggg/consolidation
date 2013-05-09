class Tree:
    def __init__(self,value):
        self.__value = value
        self.__left = None
        self.__right = None

    def getValue(self):
        return self.__value

    
    def add(self,value):
        if value < self.getValue():
            if self.__left:
                self.__left.add(value)
            else:
                self.__left = Tree(value)
        else:
            if self.__right:
                self.__right.add(value)
            else:
                self.__right = Tree(value)

        print ("node is added!")

    def inOrder(self):
        if self.__left:
            self.__left.inOrder()
        print(self.__value)
        if self.__right:
            self.__right.inOrder()
        
class Node:
    def __init__(self,value):
        self.__value = value
        self.__next = None

    def changeNext(self,pos):
        self.__next = pos
    
    def getNext(self):
        return self.__next

    def getValue(self):
        return self.__value
    
class List:
    def __init__(self):
        self.__first = None
        self.__last = None

    def add(self,node):
        if not self.__first:
            self.__first = node
        else:
            self.__last.changeNext(node)
        self.__last = node

    def insert(self,node,pos):
        current = self.__first
        for i in range(pos-1):
            current = current.getNext()
        node.changeNext(current.getNext())
        current.changeNext(node)

    def display(self):
        current = self.__first
        while  current:
            
            print(current.getValue())
            current = current.getNext()
        
