# Using Linked Lists


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class FixedStack:
    def __init__(self, size):
        self.top = None
        self.size = size

    def push(self, data):
        new = Node(data)
        if self.size_of_stack() <= self.size:
            if self.top:
                new.next = self.top
                self.top = new
            else:
                self.top = new
                new.next = None

        else:
            print("The Stack has reached the size Limit")

    def pop(self):
        if self.top:
            ptr = self.top
            self.top = ptr.next
            ptr = None

    def peek(self):
        if self.top:

            print("The Topmost Element in the stack is : ",self.top.data)
        else:
            print("Stack Empty")


    def size_of_stack(self):
        count = 0

        if self.top:
            ptr = self.top
            while ptr:
                ptr = ptr.next
                count += 1
        #print("The Current Size of the Stack is : ",count)
        #print("The Remaining Spaces in the stack is : ", self.size - count)
        return count


    def isEmpty(self):
        if self.top is None:
            print("The Stack is Empty")
        else:
            print("The Stack is not Empty")

    def __str__(self):
        ptr = self.top
        while ptr:
            print(f"|{str(ptr.data)}|", end='->')
            ptr = ptr.next
        return "End"


stk = FixedStack(5)

stk.push(1)
stk.push(2)
stk.push(3)
stk.push(4)
stk.push(5)
stk.push(6)
stk.pop()
print(stk)
stk.peek()
#stk.size_of_stack()
stk.isEmpty()
# print(stk)

