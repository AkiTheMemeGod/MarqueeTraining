class Node:
    def __init__(self, data):
        self.prev = None
        self.data = data
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new = Node(data)
        if self.head:
            new.next = self.head
            new.next.prev = new
            self.head = new
        else:
            self.head = new
            new.next = None

        new.prev = None

    def insert_at_end(self, data):
        new = Node(data)
        if self.head:
            ptr = self.head
            while ptr.next:
                ptr = ptr.next
            ptr.next = new
            new.prev = ptr
            new.next = None
        else:
            self.head = new
            new.prev = None
            new.next = None

    def reverse(self):
        if self.head:
            ptr = self.head
            while ptr.next:
                ptr = ptr.next
            while ptr:
                print(f"|{str(ptr.data)}|", end="<->")
                ptr = ptr.prev
            print("end")
    def __str__(self):
        ptr = self.head
        while ptr:
            print(f"|{str(ptr.data)}|", end='<->')

            ptr = ptr.next
        return "End"

dll = DoublyLinkedList()

dll.insert_at_end(4)
dll.insert_at_end(3)
dll.insert_at_end(2)
dll.insert_at_end(1)

dll.reverse()
