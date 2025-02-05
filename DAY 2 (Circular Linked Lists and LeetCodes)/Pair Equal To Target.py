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

    def find_pair(self, target):
        if self.head:
            ptr = self.head
            count = 0
            while ptr.next:
                forward = ptr.next
                while forward:
                    if (ptr.data + forward.data) == target:
                        print(f"THe pair is ({ptr.data}, {forward.data})")
                        count += 1
                    forward = forward.next
                ptr = ptr.next
            print(f"The number of pairs are : {count}")

    def __str__(self):
        ptr = self.head
        while ptr:
            print(f"|{str(ptr.data)}|", end='->')

            ptr = ptr.next
        return "End"


sll = SinglyLinkedList()

sll.insert_at_end(10)
sll.insert_at_end(20)
sll.insert_at_end(30)
sll.insert_at_end(40)
sll.insert_at_end(50)

sll.find_pair(70)