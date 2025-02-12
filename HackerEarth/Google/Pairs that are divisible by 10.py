x = int(input())
n = list(map(int, input().split()))
c = 0
for i in range(x):
    for j in range(i+1, x):
        if n[i]*n[j] % 10 == 0:
            c += 1
print(c)