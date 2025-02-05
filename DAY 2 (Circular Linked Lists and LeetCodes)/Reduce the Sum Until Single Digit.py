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
    @staticmethod
    def reduce(num):
        if num < 9:
            return num
        elif num % 9 == 0:
            return 9
        else:
            return num % 9

    def reduce_to_single(self):
        if self.head:
            ptr = self.head
            while ptr:
                ptr.data = self.reduce(ptr.data)
                ptr = ptr.next

    def __str__(self):
        ptr = self.head
        while ptr:
            print(f"|{str(ptr.data)}|", end='->')

            ptr = ptr.next
        return "End"


sll = SinglyLinkedList()

sll.insert_at_end(105)
sll.insert_at_end(150)
sll.insert_at_end(144)
sll.insert_at_end(2020)
sll.insert_at_end(89)
sll.insert_at_end(2)
print(sll)
sll.reduce_to_single()
print(sll)
