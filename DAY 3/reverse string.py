# Using Linked Lists
# without using len function or slicing

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

    def __str__(self):
        ptr = self.top
        while ptr:
            print(f"{str(ptr.data)}", end='')
            ptr = ptr.next
        return ""


stk = Stack()

x = input("Enter a string : ")

for i in x:
    stk.push(i)

print(stk)


"""OR"""

"""
x = input("Enter a String : ")
s = ""
for i in x:
    s = i + s
print(s)
"""