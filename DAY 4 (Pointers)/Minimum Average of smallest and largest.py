nums = list(map(int, input("Enter the elements of the array : ").split()))
averages = []
nums.sort()
avg ,f = 0, 0
r = len(nums)- 1
while r > f:
    averages.append((nums[f] + nums[r])/2)
    f += 1
    r -= 1
print(min(averages))