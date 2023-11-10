class Car:
    def __init__(self, identification:int, name:str, brand:str, price:int, active:bool):
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
    all = []
    def __init__(self):
        self.head = None

    def add(self, car):
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
            # while current.nextNode:
            #     current = current.nextNode
            # current.nextNode = new_node
            # new_node.prevNode = current

    def sort_by_price(self):
        if self.head:
            sorted_list = []
            current = self.head
            while current:
                sorted_list.append(current)
                current = current.nextNode
            sorted_list.sort(key=lambda x: x.data.price)
            self.head = sorted_list[0]
            for i in range(len(sorted_list) - 1):
                sorted_list[i].nextNode = sorted_list[i + 1]
                sorted_list[i + 1].prevNode = sorted_list[i]
            sorted_list[-1].nextNode = None

    def updateName(self, identification, name):
        current = self.head
        while current:
            if current.data.identification == identification:
                current.data.name = name
                return
            current = current.nextNode

    def updateBrand(self, identification, brand):
        current = self.head
        while current:
            if current.data.identification == identification:
                current.data.brand = brand
                return
            current = current.nextNode

    def activateCar(self, identification):
        current = self.head
        while current:
            if current.data.identification == identification:
                current.data.active = True
                return
            current = current.nextNode

    def deactivateCar(self, identification):
        current = self.head
        while current:
            if current.data.identification == identification:
                current.data.active = False
                return
            current = current.nextNode

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

    def init(self, cars):
        for car in cars:
            self.add(car)
        return self
    
    def getDatabase(self):
        return self

# Příklad použití:
db = LinkedList()
# Seznam aut
cars_list = [
    Car(1, "Car A", "Brand X", 10000, True),
    Car(2, "Car B", "Brand Y", 15000, True),
    Car(3, "Car C", "Brand Z", 12000, False),
    Car(4, "Car D", "Brand U", 7000, True)
]

# Inicializace databáze
db.init(cars_list)

# Aktualizace názvu a značky vozu s identifikátorem 2
# db.updateName(2, "Car D")
# db.updateBrand(2, "Brand Z")

# Deaktivace vozu s identifikátorem 1
# db.deactivateCar(1)

# Výpočet celkové ceny aktivních vozů
# total_price = db.calculateCarPrice()
# print(f"Celková cena aktivních aut: {total_price}")
# print(db.head)
# print(db.head.nextNode.nextNode.nextNode)
# print(db.head.nextNode.nextNode)
# print(db.head.nextNode)
# print(db.head.nextNode.data.brand)
# print(db.head.nextNode.nextNode.data.brand)
print("Hello World")
# print(db.head.data.__repr__)
# print(db.head.nextNode.data.__repr__)
# print(db.head.nextNode.nextNode.data.__repr__)
print(db)
