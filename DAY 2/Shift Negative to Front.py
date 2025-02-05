nums = [10 , 20 , -1, -2 , 50, 30]
x = nums
for i in range(0, len(nums)-1):
    for j in range(i+1,len(nums)):
        if nums[j] < 0:
            nums[j], nums[i] = nums[i], nums[j]
            break

print(nums)