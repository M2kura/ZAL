from cars import Car

class Queue:
    def __init__(self) -> None:
        self.data: list[Car] = []

    def push(self, item: Car) -> None:
        self.data.append(item)
        
    def pop(self) -> Car:
        return self.data.pop(0)
        
    def size(self):
        return len(self.data)
        
    def is_empty(self):
        return self.size() == 0 
    
    def print_items(self):
        for item in self.data:
            print()

# TEST

car1 = Car("BMW", 750000)
car2 = Car("Skoda", 350000)
car3 = Car("Kia", 520000)
my_queue = Queue()
my_queue.push(car1)
my_queue.push(car2)
my_queue.push(car3)
print("--------------")
print(my_queue.size())
print(my_queue.is_empty())
my_queue.print_items()
print("--------------")
# print(my_queue.pop())
# print(my_queue.pop())
# print(my_queue.pop())

