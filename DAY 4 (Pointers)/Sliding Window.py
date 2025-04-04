nums = list(map(int, input("Enter the elements of the array : ").split()))

sub = int(input("Window Size : "))

sums = []
"""
-------------------------------------------
My Slicing Implementation
-------------------------------------------
"""

for i in range(sub):
    if i == len(nums) - sub:
        break
    sums.append(sum(nums[i:sub+i]))
print("Maximum Sum Sub Array : ",max(sums))


"""i = 0
cur = sum(nums[:sub])
maxi = cur
while sub < len(nums):
    cur = cur - nums[i] + nums[sub]
    i += 1
    sub += 1
    maxi = max(cur, maxi)
print(maxi)"""