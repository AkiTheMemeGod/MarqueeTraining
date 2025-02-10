
nums = input("Enter a buzz Word : ")
sub = 3
i = 0
cur = ""
sets = []
while sub <= len(nums):
    cur = nums[i:sub]
    i += 1
    sub += 1
    if len(set(cur)) == 3:
        sets.append(cur)

print(sets)

