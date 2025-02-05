x = list(map(int,input().split(",")))

y = int(input())
count = 0
for i in range(0, len(x)-1):
    for j in range(i+1, len(x)):
        if x[i] + x[j] >= y:
            count += 1
print(count)