class Node:
    def __init__(self, nextNode, prevNode, data):
        self.data = data
        self.next = nextNode
        self.prev = prevNode
        pass


class LinkedList:
    def __init__(self):
        self.head = None
        self.end = None
        self.count = 0
    
    def isEmpty(self):
        return self.head == None
    
    def push(self,item):
        node = Node(item) 
        if not self.head:
            self.head = self.end = node
        else: 
            node.next = self.head
            self.hean = node
        self.count += 1
        
    def pop(self): 
        if self.head:
            ret = self.head.data 
            self.head = self.head.next
            if self.head == None:
                self.end = None
            self.count -= 1
            return ret
    pass


class Car:
    def __init__(self, identification: 0, name: str, brand: str, price: int, active: bool):
        self.identification = identification
        self.name = name
        self.brand = brand
        self.price = price
        self.active = active

    def __repr__(self):
        return f"{self.__class__.__name__}({self.identification}, '{self.name}', '{self.brand}', {self.price}, {self.active})"

car1 = Car(0, "Beha", "BMW", 750000, True)
print(car1.__repr__())

db = LinkedList()


def init(cars):
    pass


def add(car):
    pass


def updateName(identification, name):
    pass


def updateBrand(identification, brand):
    pass


def activateCar(identification):
    pass


def deactivateCar(identification):
    pass


def getDatabaseHead():
    pass


def getDatabase():
    pass


def calculateCarPrice():
    pass


def clean():
    pass