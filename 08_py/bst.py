class Node:
    def __init__(self, value: int):
        self.value = value
        self.left = None
        self.right = None
    



class BinarySearchTree:
    def __init__(self):
        self.head = None

    def insert(self, value):
        new_node = Node(value)
        current = self.head
        if not self.head:
            self.head = new_node
            return
        while current:
            if value > current.value:
                if not current.right:
                    current.right = new_node
                    return
                current = current.right
            elif value < current.value:
                if not current.left:
                    current.left = new_node
                    return
                current = current.left
            else:
                return

    def fromArray(self, array: list[int]):
        for i in array:
            self.insert(i)
        return 

    def search(self, value):
        pass

    def min(self):
        pass

    def max(self):
        pass

    def visitedNodes(self):
        pass

bst2 = BinarySearchTree()
bst2.fromArray([5, 3, 5, 1, 4, 7, 6, 8])