# Using Linked Lists

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        new = Node(data)
        if self.top:
            new.next = self.top
            self.top = new
        else:
            self.top = new
            new.next = None

    def pop(self):
        if self.top:
            ptr = self.top
            self.top = ptr.next
            ptr = None

    def peek(self):
        if self.top:
            return self.top.data
            # print("The Topmost Element in the stack is : ",self.top.data)
        else:
            print("Stack Empty")

    def size(self):
        count = 0

        if self.top:
            ptr = self.top
            while ptr:
                ptr = ptr.next
                count += 1
        print("The Size of the Stack is : ",count)

    def is_empty(self):
        return self.top is None

    def __str__(self):
        ptr = self.top
        while ptr:
            print(f" {str(ptr.data)} ", end='->')
            ptr = ptr.next
        return "End"


stk = Stack()

stk.push(1)
stk.push(2)
stk.push(3)
stk.push(4)
stk.push(5)
stk.pop()
print(stk)
stk.peek()  
stk.size()
stk.is_empty()
