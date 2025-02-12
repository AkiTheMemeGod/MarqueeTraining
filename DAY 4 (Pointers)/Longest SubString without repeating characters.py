
nums = input("Enter a buzz Word : ")
sub = 0
i = 0
cur = ""
sets = []
while sub <= len(nums):
    cur = nums[i:sub]
    if len(set(cur)) == len(cur):
        sub += 1
        sets.append(cur)
        continue
    i += 1
    sub = 0

o = [len(set(i)) for i in sets]
print(max(o))