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

db = LinkedList()

def add(car: Car):
    new_node = Node(car)
    if not db.head:
        db.head = new_node
    else:
        current = db.head
        if current.data.price <= new_node.data.price:
            while current.nextNode:
                if current.nextNode.data.price <= new_node.data.price:
                    current = current.nextNode
                else:
                    biggerNode = current.nextNode
                    current.nextNode = biggerNode.prevNode = new_node
                    new_node.prevNode = current
                    new_node.nextNode = biggerNode
                    return db
            else: 
                current.nextNode = new_node
                new_node.prevNode = current
                return db
        else:
            db.head = new_node
            new_node.nextNode = current
            current.prevNode = db.head
    return db

def updateName(identification: int, name: str):
    current = db.head
    while current:
        if current.data.identification == identification:
            current.data.name = name
            return current
        current = current.nextNode
    else:
        return None

def updateBrand(identification, brand):
    current = db.head
    while current:
        if current.data.identification == identification:
            current.data.brand = brand
            return current
        current = current.nextNode
    else:
        return None

def activateCar(identification):
    current = db.head
    while current:
        if current.data.identification == identification:
            current.data.active = True
            return current
        current = current.nextNode
    else:
        return None

def deactivateCar(identification):
    current = db.head
    while current:
        if current.data.identification == identification:
            current.data.active = False
            return current
        current = current.nextNode
    else:
        return None

def calculateCarPrice():
    current = db.head
    total_price = 0
    while current:
        if current.data.active:
            total_price += current.data.price
        current = current.nextNode
    return total_price

def getDatabaseHead():
    return db.head

def clean():
    db.head = None

def init(cars: list[Car]):
    for car in cars:
        add(car)
    return db

def getDatabase():
    return db

db = LinkedList()

# init([
#     Car(1, "Octavia", "Skoda", 123000, True), 
#     Car(23, "Felica", "Skoda", 5000, True),
#     Car(11, "Superb", "Skoda", 54000, True)
#     ])