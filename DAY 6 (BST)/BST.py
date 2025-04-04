class Node:
    def __init__(self, data):
        self.left = None
        self.data = data
        self.right = None

class BinarySearchTree:

    @staticmethod
    def create(data):
        return Node(data)

    def insert(self, node, data):
        if node is None:
            return self.create(data)
        if data < node.data:
            node.left = self.insert(node.left, data)
        elif data > node.data:
            node.right = self.insert(node.right, data)
        return node

    def in_order(self, node):
        if node:
            self.in_order(node.left)
            print(node.data)
            self.in_order(node.right)

    def pre_order(self, node):
        if node:
            print(node.data)
            self.pre_order(node.left)
            self.pre_order(node.right)

    def post_order(self, node):
        if node:
            self.post_order(node.left)
            self.post_order(node.right)
            print(node.data)



tree = BinarySearchTree()
root = tree.create(8)
for i in range(8):
    tree.insert(root, int(input()))

print("inorder: ")
print(tree.in_order(root))

print("preorder: ")
print(tree.pre_order(root))

print("postorder: ")
print(tree.post_order(root))

print(tree.binaryTreePaths(root.data))

