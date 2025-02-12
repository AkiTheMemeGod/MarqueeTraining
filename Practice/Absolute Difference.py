x = list(map(int, input().split()))

slow, fast = 0, 1
l = len(x)
for i in range(len(x)):
    if fast < l:
        x.append(abs(x[slow] - x[fast]))
        slow += 1
        fast += 1
    else:
        break

print(x)