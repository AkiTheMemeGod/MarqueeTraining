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

    def isEmpty(self):
        if self.top is None:
            # print("The Stack is Empty")
            return True
        else:
            # print("The Stack is not Empty")
            return False

    def __str__(self):
        ptr = self.top
        while ptr:
            print(f" {str(ptr.data)} ", end='->')
            ptr = ptr.next
        return "End"


stk = Stack()
maps = {
    ']':'[',
    '}' : '{',
    ')' : '('
}
left = ['{', '[', '(']
string = input("Enter a string : ")
count = 0
if string:
    for i in string:
        if i in left:
            stk.push(i)

        else:
            if stk.peek() == maps[i]:
                stk.pop()
                count += 1

else:
    print("Empty")
if stk.isEmpty():
    print("the no of valid brackets are : ", count)
else:
    print("Not a valid bracket string")
print(stk)


