n, k = map(int, input().split())

nums = list(map(int, input().split()))
nums.sort()
subs = []
l = len(nums)
for i in range(l):
    for j in range(i, l):
        sub = nums[i:j+1]
        if all(abs(sub[x] - sub[x+1]) == 1 for x in range(len(sub) - 1)):
            subs.append(sub)
c = 0
for u in subs:
    if sum(u) == k:
        print(u)
        c += 1
print(c)