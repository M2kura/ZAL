class Node:
    def __init__(self, value: int):
        self.value = value
        self.left = None
        self.right = None
    



class BinarySearchTree:
    def __init__(self):
        self.head = None
        self.visited = 0

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

    def search(self, value: int):
        count = 0
        current = self.head
        if not self.head:
            return False
        while current:
            if current.value == value:
                count += 1
                self.visited = count
                return True
            elif value > current.value and current.right:
                count += 1
                current = current.right
            elif value < current.value and current.left:
                count += 1
                current = current.left
            else:
                count += 1
                self.visited = count
                return False

    def min(self):
        count = 0
        current = self.head
        if not self.head:
            return None
        while current:
            if not current.left:
                count += 1
                self.visited = count
                return current.value
            current = current.left
            count += 1

    def max(self):
        pass

    def visitedNodes(self):
        return self.visited

bst2 = BinarySearchTree()
bst2.fromArray([5, 3, 5, 1, 4, 7, 6, 8])
print(bst2.min())
print(bst2.visitedNodes())
