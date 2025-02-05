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

    def front(self):
        return self.q[0]

    def last(self):
        return self.q[-1]

    def pop(self):
        self.q = self.q[:-1]

q = Queue()

x = input("Enter a String : ")

for i in x:
    if q.q:
        if q.last() != i:
            q.enqueue(i)
        else:
            q.pop()
    else:
        q.enqueue(i)

if q.last() == q.front():
    q.pop()
    q.dequeue()

print(q.q)
print(q.last())