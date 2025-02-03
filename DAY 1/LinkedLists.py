from typing import no_type_check_decorator


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new = Node(data)
        new.next = self.head
        self.head = new

    def insert_at_end(self, data):
        new = Node(data)
        if self.head:
            ptr = self.head
            while ptr.next:
                ptr = ptr.next
            ptr.next = new
        else:
            self.head = new
    def insert_at_position(self, data, position):
        new = Node(data)
        if self.head:
            ptr = self.head
            for i in range(position-2):
                ptr = ptr.next
            new.next = ptr.next
            ptr.next = new

    def search(self, data):
        if self.head:
            ptr = self.head
            while ptr.next:
                if ptr.data == data or ptr.next.data == data:
                    return True
                else:
                    ptr = ptr.next
                    continue
            return False

    def find_middle(self):
        ptr = self.head
        length = 0
        while ptr.next:
            ptr = ptr.next
            length += 1
        ptr = self.head
        for i in range(round(length/2)):
            ptr = ptr.next
        return ptr.data

    def find_mid(self):
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        print(f"The Middle Node is  -> {slow.data}")


    def __str__(self):
        ptr = self.head
        while ptr:
            print(str(ptr.data), end='->')
            ptr = ptr.next
        return "End"


sll = SinglyLinkedList()

while True:
    option = int(input(
        " 1 for append\n 2 for Begining\n 3 for position\n 4 for searching nodes\n 5 find middle node \nEnter your option : "))

    if option == 1:
        x = int(input("Enter the Node value to enter at append : "))
        sll.insert_at_end(x)
        print(sll)
    if option == 2:
        x = int(input("Enter the Node value to enter at beginning : "))
        sll.insert_at_beginning(x)
        print(sll)
    if option == 3:
        x = int(input("Enter the Node value to enter at position : "))
        pos = int(input("Enter the position : "))
        sll.insert_at_position(x, pos)
        print(sll)
    if option == 4:
        x = int(input("Node to search : "))
        result = sll.search(x)
        if result:
            print("The node is present in the linked list ")
        else:
            print("The node is not present in the linked list")
    if option == 5:
        sll.find_mid()


