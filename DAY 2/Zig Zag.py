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

    def convert_to_list(self):
        if self.head:
            l = []
            ptr = self.head
            while ptr.next:
                l.append(ptr.data)
                ptr = ptr.next
            l.append(ptr.data)
        return l

    def find_mid(self):
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow.data

    def zigzag(self):

        sll = self.convert_to_list()
        length = len(sll)
        ops = []
        for i in range(1, length):
            if i % 2 == 0:
                ops.append(i)
            else:
                ops.append(i*-1)
        mid = self.find_mid()
        index = sll.index(mid)
        # print(ops)
        print(sll[index], end=" ")
        for i in ops:
            index = index + i
            print(sll[index] , end=" ")



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
sll.insert_at_end(60)
sll.insert_at_end(60)
sll.insert_at_end(70)


print(sll)
sll.zigzag()

