class Queue:
    def __init__(self):
        self.q = []

    def enqueue(self, data):
        self.q.append(data)

    def dequeue(self):
        self.q = self.q[1:]

    def size(self):
        return len(self.q)

    def is_empty(self):
        return len(self.q) == 0

    def display(self):
        print(self.q)


q = Queue()

q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)
q.display()
q.dequeue()
q.display()

