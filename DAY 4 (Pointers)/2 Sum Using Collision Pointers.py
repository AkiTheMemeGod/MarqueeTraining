"""class Node:
    def __init__(self, data):
        self.next = None
        self.data = data

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def convert_list_to_ll"""

nums = list(map(int,input("Enter Elements : ").split(' ')))
target = int(input("Enter the target sum pair : "))
print(nums)
"""
f = 0
r = -1
i = 0

while i < len(nums):
    if nums[f] + nums[r] == target:
        print(f"({nums[f]}, {nums[r]})")
        break
    f += 1
    r -= 1
    i += 1"""


left, right = 0 , len(nums)-1
while left < right:
    cur = nums[left] + nums[right]
    if cur == target:
        print(nums[left], nums[right])
        print(True)
        exit()
    elif cur > target:
        right -= 1
    else:
         left += 1

print(False)