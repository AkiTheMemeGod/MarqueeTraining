nums = list(map(int, input("Enter the elements of the array : ").split()))

sub = int(input("Window Size : "))
size = sub
sums = []

i = 0
cur = sum(nums[:sub])
maxi = cur
while sub < len(nums):
    cur = cur - nums[i] + nums[sub]
    i += 1
    sub += 1
    maxi = max(cur, maxi)
print("Maximum Average Sub Array : ",maxi/size)
