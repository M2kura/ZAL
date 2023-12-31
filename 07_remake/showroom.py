class Node:
    def __init__(self, nextNode, prevNode, data):
        self.nextNode = None
        self.prevNode = None
        self.data = data


class LinkedList:
    def __init__(self):
        self.head = None


class Car:
    def __init__(self, identification: int, name: str, brand: str, price: int, active: bool):
        self.identification = identification
        self.name = name
        self.brand = brand
        self.price = price
        self.active = active


db = LinkedList()

def add(car: Car):
    newNode = Node(None, None, car)
    if db.head == None:
        db.head = newNode
        return db
    else:
        current = db.head
        if current.data.price <= newNode.data.price:
            while current.nextNode != None:
                if current.nextNode.data.price <= newNode.data.price:
                    current = current.nextNode
                else:
                    biggerNode = current.nextNode
                    current.nextNode = biggerNode.prevNode = newNode
                    newNode.prevNode = current
                    newNode.nextNode = biggerNode
                    return db
            else: 
                current.nextNode = newNode
                newNode.prevNode = current
                return db
        else:
            db.head = newNode
            newNode.nextNode = current
            current.prevNode = db.head

def init(cars: list[Car]):
    for car in cars:
        add(car)
    return db

# car1 = Car(3, "Alex", "Ford", 31400, True)
# car2 = Car(4, "Max", "Mers", 35400, True)
# car3 = Car(9, "Lolla", "Buggati", 9000, True)
# car4 = Car(4, "Martiza", "Audi", 700, True)
# init([car1, car2, car3, car4])

def updateName(identification: int, name: str):
    current = db.head
    while current:
        if current.data.identification == identification:
            current.data.name = name
            return current
        current = current.nextNode
    else: 
        return None

def updateBrand(identification: int, brand: str):
    current = db.head
    while current:
        if current.data.identification == identification:
            current.data.brand = brand
            return current
        current = current.nextNode
    else: 
        return None

def activateCar(identification: int):
    current = db.head
    while current:
        if current.data.identification == identification:
            current.data.active = True
            return current
        current = current.nextNode
    else: 
        return None

def deactivateCar(identification: int):
    current = db.head
    while current:
        if current.data.identification == identification:
            current.data.active = False
            return current
        current = current.nextNode
    else: 
        return None

def getDatabaseHead():
    return db.head

def getDatabase():
    return db

def calculateCarPrice():
    current = db.head
    total_price = 0
    while current:
        if current.data.active:
            total_price += current.data.price
        current = current.nextNode
    return total_price


def clean():
    db.head = None