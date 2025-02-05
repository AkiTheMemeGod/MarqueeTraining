class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new = Node(data)
        if self.head:
            ptr = self.head
            while ptr.next != self.head:
                ptr = ptr.next
            ptr.next = new
            new.next = self.head
            self.head = new
        else:
            self.head = new
            new.next = self.head

    def insert_at_end(self, data):
        new = Node(data)
        if self.head:
            ptr = self.head
            while ptr.next != self.head:
                ptr = ptr.next
            ptr.next = new
            new.next = self.head
        else:
            self.head = new
            new.next = self.head

    def find(self):
        if self.head:
            l = []
            ptr = self.head
            while ptr.next != self.head:
                l.append(ptr.data)
                ptr = ptr.next
            l.append(ptr.data)
            print(f"The Maximum in the CLL is {max(l)}")
            print(f"The Minimum in the CLL is {min(l)}")
            print(f"The Maximum Difference of the CLL is {max(l) - min(l)}")



    def __str__(self):
        ptr = self.head
        while ptr.next != self.head:
            print(f"|{str(ptr.data)}|", end='->')

            ptr = ptr.next
        return f"|{ptr.data}|->End"

cll = CircularLinkedList()

cll.insert_at_end(1)
cll.insert_at_end(2)
cll.insert_at_end(3)
cll.insert_at_end(4)
cll.insert_at_end(5)
cll.insert_at_end(6)
cll.find()
print(cll)