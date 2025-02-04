class Node:
    def __init__(self, data):
        self.prev = None
        self.data = data
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

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

    def rotate(self, n):
        if self.head:
            pivot = self.head
            ptr = self.head
            count = 1
            while ptr.next:
                if count < n:
                    pivot = pivot.next
                    count += 1
                ptr = ptr.next
            # print(pivot.data)
            new_head = pivot.next
            new_head.prev = None
            pivot.next = None
            ptr.next = self.head
            self.head.prev = ptr
            self.head = new_head

    def __str__(self):
        ptr = self.head
        while ptr:
            print(f"|{str(ptr.data)}|", end='<->')

            ptr = ptr.next
        return "End"

dll = DoublyLinkedList()

dll.insert_at_end(1)
dll.insert_at_end(2)
dll.insert_at_end(3)
dll.insert_at_end(4)
dll.insert_at_end(5)

dll.rotate(3)
print(dll)
