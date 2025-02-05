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

    @staticmethod
    def is_prime(num):
        if num <= 1:
            return False
        i = 2
        while i * i <= num:
            if num % i == 0:
                return False
            i += 1
        return True

    def no_of_primes(self):
        if self.head:
            count = 0
            ptr = self.head
            while ptr:
                if self.is_prime(ptr.data):
                    count += 1
                ptr = ptr.next
            print(f"The number of prime numbers are : {count}")


sll = SinglyLinkedList()

sll.insert_at_end(12)
sll.insert_at_end(11)
sll.insert_at_end(7)
sll.insert_at_end(14)
sll.insert_at_end(13)

sll.no_of_primes()


