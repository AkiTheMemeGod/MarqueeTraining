from collections import deque
class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None


class Tree:
    def __init__(self):
        self.root = None

    def add_child(self, data):
        new_node = Node(data)
        if not self.root:
            self.root = new_node
            return

        ptr = self.root
        while True:
            if data < ptr.data:
                if ptr.left:
                    ptr = ptr.left
                else:
                    ptr.left = new_node
                    break
            else:
                if ptr.right:
                    ptr = ptr.right
                else:
                    ptr.right = new_node
                    break




t = Tree()
t.add_child(10)
t.add_child(3)
t.add_child(2)
t.add_child(4)
t.add_child(11)
t.add_child(5)
t.add_child(124)

print(t)
