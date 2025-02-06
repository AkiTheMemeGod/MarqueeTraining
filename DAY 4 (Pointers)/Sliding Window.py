nums = list(map(int, input("Enter the elements of the array : ").split()))

sub = int(input("Window Size : "))

sums = []

for i in range(sub):
    if i == len(nums) - sub:
        break
    sums.append(sum(nums[i:sub+i]))
print("Maximum Sum Sub Array : ",max(sums))