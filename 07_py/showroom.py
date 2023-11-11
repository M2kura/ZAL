class Car:
    def __init__(self, identification: int, name: str, brand: str, price: int, active: bool):
        self.identification = identification
        self.name = name
        self.brand = brand
        self.price = price
        self.active = active
    
    def __repr__(self) -> str:
        return f"[ID: {self.identification}, name: {self.name}, brand: {self.brand}, price: {self.price}, active: {self.active}]"

class Node:
    def __init__(self, data):
        self.data = data
        self.nextNode = None
        self.prevNode = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, car: Car):
        new_node = Node(car)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            if current.data.price <= new_node.data.price:
                while current.nextNode:
                    if current.nextNode.data.price <= new_node.data.price:
                        current = current.nextNode
                    else:
                        biggerNode = current.nextNode
                        current.nextNode = biggerNode.prevNode = new_node
                        new_node.prevNode = current
                        new_node.nextNode = biggerNode
                        return self
                else: 
                    current.nextNode = new_node
                    new_node.prevNode = current
                    return self
            else:
                self.head = new_node
                new_node.nextNode = current
                current.prevNode = self.head
        return self

    def updateName(self, identification: int, name: str):
        current = self.head
        while current:
            if current.data.identification == identification:
                current.data.name = name
                return current
            current = current.nextNode
        else:
            return None

    def updateBrand(self, identification, brand):
        current = self.head
        while current:
            if current.data.identification == identification:
                current.data.brand = brand
                return current
            current = current.nextNode
        else:
            return None

    def activateCar(self, identification):
        current = self.head
        while current:
            if current.data.identification == identification:
                current.data.active = True
                return current
            current = current.nextNode
        else:
            return None

    def deactivateCar(self, identification):
        current = self.head
        while current:
            if current.data.identification == identification:
                current.data.active = False
                return current
            current = current.nextNode
        else:
            return None

    def calculateCarPrice(self):
        current = self.head
        total_price = 0
        while current:
            if current.data.active:
                total_price += current.data.price
            current = current.nextNode
        return total_price

    def getDatabaseHead(self):
        return self.head

    def clean(self):
        self.head = None

    def init(self, cars: list[Car]):
        for car in cars:
            self.add(car)
        return self
    
    def getDatabase(self):
        return self

db = LinkedList()