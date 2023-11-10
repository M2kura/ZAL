class Car:
    def __init__(self, identification:int, name:str, brand:str, price:int, active:bool) -> None:
        self.identification = identification
        self.name = name
        self.brand = brand
        self.price = price
        self.active = active

    def __repr__(self):
        return f"{self.__class__.__name__}({self.identification}, '{self.name}', '{self.brand}', {self.price}, {self.active})"

class Node:
    def __init__(self, data):
            self.data = data
            self.nextNode = None
            self.prevNode = None

class LinkedList():
    def __init__(self):
        super().__init__()

        self.head = None
        self.end = None
        self.count = 0

    def add(self, car):
        node = Node(car)
        if self.head == None:
            self.head = self.end = node
        else:
            
        pass
    
    # def push(self,item):
    #     node = Node(item) 
    #     if not self.head:
    #         self.head = self.end = node
    #     else: 
    #         node.next = self.head
    #         self.head = node
    #     self.count += 1
        
    # def pop(self): 
    #     if self.head:
    #         ret = self.head.data 
    #         self.head = self.head.next
    #         if self.head == None:
    #             self.end = None
    #         self.count -= 1
    #         return ret
    # pass


car1 = Car(0, "Beha", "BMW", 750000, True)
print(car1.__repr__())

db = LinkedList()


def init(cars):
    pass


def add(car: Car):
    return Node(car)
    


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