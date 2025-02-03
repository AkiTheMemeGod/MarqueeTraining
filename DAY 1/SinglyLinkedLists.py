class Node:
    def __init__(self, data: int):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new = Node(data)
        new.next = self.head
        self.head = new

    def insert_at_end(self, data):
        new = Node(data)
        if self.head:
            ptr = self.head
            while ptr.next:
                ptr = ptr.next
            ptr.next = new
        else:
            self.head = new
    def insert_at_position(self, data, position):
        new = Node(data)
        if self.head:
            ptr = self.head
            for i in range(position-2):
                ptr = ptr.next
            new.next = ptr.next
            ptr.next = new

    def search(self, data):
        if self.head:
            ptr = self.head
            while ptr.next:
                if ptr.data == data or ptr.next.data == data:
                    return True
                else:
                    ptr = ptr.next
                    continue
            return False

    def find_middle(self):
        ptr = self.head
        length = 0
        while ptr.next:
            ptr = ptr.next
            length += 1
        ptr = self.head
        for i in range(round(length/2)):
            ptr = ptr.next
        return ptr.data

    def find_mid(self):
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # print(f"The Middle Node is  -> {slow.data}")
        return slow.data

    """def frommid(self):
        if self.head:
            slow = fast = self.head
            while fast and fast.next:
                slow = slow.next
            self.head = slow"""


    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def tomid(self):
        mid = self.find_mid()
        if self.head:
            ptr = self.head
            while ptr:
                print(ptr.data, end="->")
                if ptr.data == mid:
                    break
                ptr = ptr.next
            print("\n")

    def bubble_sort(self):
        if self.head:
            ptr = self.head
            while ptr.next:
                forward = ptr.next
                while forward:
                    if ptr.data > forward.data:
                        ptr.data , forward.data = forward.data, ptr.data
                    forward = forward.next
                ptr = ptr.next



    def deletion_at_beginning(self):
        if self.head:
            ptr = self.head
            self.head = ptr.next

    def deletion_at_end(self):
        if self.head:
            ptr = self.head
            pre = ptr
            while ptr.next:
                pre = ptr
                ptr = ptr.next
            pre.next = None

    def __str__(self):
        ptr = self.head
        while ptr:
            print(f"|{str(ptr.data)}|", end='->')

            ptr = ptr.next
        return "End"


sll = SinglyLinkedList()

while True:
    print("\nOptions:")
    print("1. Append a node at the end")
    print("2. Delete a node from the end")
    print("3. Insert a node at a specific position")
    print("4. Search for a node")
    print("5. Find the middle node")
    print("6. Reverse the linked list")
    print("7. Print nodes up to the middle node")
    print("8. Sort the linked list using bubble sort")
    print("9. Exit")

    option = int(input("Enter your option: "))

    if option == 1:
        x = int(input("Enter the node value to append: "))
        sll.insert_at_end(x)
        print(sll)
    elif option == 2:
        sll.deletion_at_end()
        print(sll)
    elif option == 3:
        x = int(input("Enter the node value to insert: "))
        pos = int(input("Enter the position: "))
        sll.insert_at_position(x, pos)
        print(sll)
    elif option == 4:
        x = int(input("Enter the node value to search: "))
        result = sll.search(x)
        if result:
            print("The node is present in the linked list.")
        else:
            print("The node is not present in the linked list.")
    elif option == 5:
        print(f"The middle node value is: {sll.find_mid()}")
    elif option == 6:
        sll.reverse()
        print(sll)
    elif option == 7:
        sll.tomid()
    elif option == 8:
        sll.bubble_sort()
        print(sll)
    elif option == 9:
        print("Exiting...")
        break
    else:
        print("Invalid option. Please try again.")