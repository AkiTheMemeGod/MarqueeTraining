"""x = [0, 12, 0, 5, 2, 0, 3, 12, 0]
print("Before : ", x)
for i in x:
    if i == 0:
        x.remove(i)
        x.append(0)

print("After : ",x)"""

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
            return ptr.data

    def peek(self):
        if self.top:
            return self.top.data
            # print("The Topmost Element in the stack is : ",self.top.data)
        else:
            print("Stack Empty")
            return None

    def size(self):
        count = 0

        if self.top:
            ptr = self.top
            while ptr:
                ptr = ptr.next
                count += 1
        print("The Size of the Stack is : ",count)

    def isEmpty(self):
        if self.top is None:
            print("The Stack is Empty")
            return True
        else:
            print("The Stack is not Empty")
            return False

    def __str__(self):
        ptr = self.top
        while ptr:
            print(f" {str(ptr.data)} ", end='->')
            ptr = ptr.next
        return "End"


stk = Stack()

stk.push(1)
stk.push(0)
stk.push(3)
stk.push(4)
stk.push(0)
stk.push(12)
print(stk)
final = []
zero = 0
for _ in range(6):
    if stk.peek() != 0:
        final.append(stk.pop())
    else:
        stk.pop()
        zero += 1
    print(stk)
for i in range(zero):
    final.append(0)

print(final)