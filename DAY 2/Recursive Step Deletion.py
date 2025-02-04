class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None


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

    def convert_to_list(self):
        if self.head:
            l = []
            ptr = self.head
            while ptr.next != self.head:
                l.append(ptr.data)
                ptr = ptr.next
            l.append(ptr.data)
        return l

    def recursive_delete(self, step):
        if not self.head or self.head.next == self.head:
            return

        ptr = self.head
        preptr = None
        count = 1

        while ptr.next != ptr:
            if count % step == 0:
                if preptr:
                    preptr.next = ptr.next
                if ptr == self.head:
                    self.head = ptr.next
                ptr = ptr.next
            else:
                preptr = ptr
                ptr = ptr.next
            count += 1

        self.head = ptr





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
cll.recursive_delete(2)
print(cll)