class Node:
    def __init__(self, data):
        self.next = None
        self.data = data

class Queue:
    def __init__(self):
        self.front = None

    def enqueue(self, data):
        new = Node(data)
        if self.front:
            ptr = self.front
            while ptr.next:
                ptr = ptr.next
            ptr.next = new
            new.next = None
        else:
            self.front = new
            new.next = None
    def dequeue(self):
        if self.front:
            ptr = self.front
            self.front = ptr.next
            ptr = None

        else:
            print("The Queue is Empty")

    def size(self):
        if self.front:
            c = 0
            ptr = self.front
            while ptr.next:
                c += 1
                ptr = ptr.next
        print("The Size of the Queue is : ", c)
        return c

    def is_empty(self):
        return self.front is None

    def __str__(self):
        ptr = self.front
        print("| ", end="")

        while ptr:
            print(f" {str(ptr.data)} ", end=' | ')
            ptr = ptr.next
        return ""
q = Queue()

q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)
print(q)
print()
q.size()
print()
q.dequeue()
print(q)
print()
print(q.is_empty())