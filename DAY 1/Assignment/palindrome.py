class Node:
    def __init__(self, data):
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
            new.prev = ptr
            new.next = None
        else:
            self.head = new
            new.prev = None
            new.next = None

    def is_palindrome(self):
        if self.head:
            s = ""
            ptr = self.head
            while ptr:
                s += ptr.data
                ptr = ptr.next
            if s[::-1] == s:
                print("Palindrome")
            else:
                print("Not a Palindrome")

sll = SinglyLinkedList()

sll.insert_at_end('m')
sll.insert_at_end('a')
sll.insert_at_end('d')
sll.insert_at_end('a')
sll.insert_at_end('m')

sll.is_palindrome()


