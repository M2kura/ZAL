from cars import Car
class Node:
    def __init__(self, car: Car, next: Node, prev: Node) -> None:
        self.data = car
        self.next = next
        self.prev = prev

class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def push(self, car: Car):
        new_node = Node(car, None, None)
        if self.head == None:
            self.head = new_node
        else:
            tmp_node = self.head
            while tmp_node.next != None:
                tmp_node = tmp_node.next
            tmp_node.next = new_node
            new_node.prev = tmp_node