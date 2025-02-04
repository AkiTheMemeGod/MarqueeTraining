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
    def is_ps(num):
        if num < 0:
            return False
        root = num ** 0.5
        if root.is_integer():
            return True
        else:
            return False

    def find_num_of_ps(self):
        if self.head:
            count = 0
            ptr = self.head
            while ptr:
                if self.is_ps(ptr.data):
                    count += 1
                ptr = ptr.next
            print(f"The number of perfect Squares : {count}")
    def __str__(self):
        ptr = self.head
        while ptr:
            print(f"|{str(ptr.data)}|", end='->')

            ptr = ptr.next
        return "End"


sll = SinglyLinkedList()

sll.insert_at_end(4)
sll.insert_at_end(6)
sll.insert_at_end(8)
sll.insert_at_end(10)
sll.insert_at_end(9)
print(sll)
sll.find_num_of_ps()