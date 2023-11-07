from cars import Car

class Stack:
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
my_stack = Stack()
my_stack.push(car1)
my_stack.push(car2)
my_stack.push(car3)
print(my_stack.data)
my_stack.pop()
