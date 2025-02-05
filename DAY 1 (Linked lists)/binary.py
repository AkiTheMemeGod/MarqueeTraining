class Node:
    def __init__(self, data: int):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new = Node(data)
        if self.head:
            ptr = self.head
            while ptr.next:
                ptr = ptr.next
            ptr.next = new
        else:
            self.head = new

    def binary(self):
        if self.head:
            ptr = self.head
            s = ""
            while ptr:
                s += str(ptr.data)
                ptr = ptr.next
            print(s)
            return int(s,2)
    def binary_of_sum(self):
        if self.head:
            s = 0
            ptr = self.head
            while ptr:
                s += ptr.data
                ptr = ptr.next
            print(s)
            return bin(s)

    def __str__(self):
        ptr = self.head
        while ptr:
            print(str(ptr.data), end='->')
            ptr = ptr.next
        return "End"


sll = SinglyLinkedList()

while True:
    option = int(input(
        " 1 for append\n 2 convert to integer from binary: "))

    if option == 1:
        x = int(input("Enter the Node value to enter at append : "))
        sll.insert_at_end(x)
        print(sll)

    if option == 2:
        x = sll.binary_of_sum()
        print(f"The SLL converted from binary to Integer is : {str(x)[2:]}")