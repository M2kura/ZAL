from cars import Car

class Queue:
    def __init__(self) -> None:
        self.data: list[Car] = []
        pass

    def push(self, item):
        self.data.append(item)
    
    def pop(self) -> Car:
        return self.data.pop()
    
    def size(self):
        return len(self.data)

    def is_empty(self):
        return self.size(0) == 0

    def print_items(self):
        for item in self.data:
            print(item)

car1 = Car("BMW", 900000)
car2 = Car("Merc", 4)
car3 = Car("Makura", 2005)
my_queue = Queue()
my_queue.push(car1)
my_queue.push(car2)
my_queue.push(car3)
print("..........")
print(my_queue.size())
