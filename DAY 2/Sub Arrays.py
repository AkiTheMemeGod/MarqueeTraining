x = list(map(int,input().split(",")))

y = int(input())
count = []
for i in x:
    if i > y:
        print(1)
for i in range(0, len(x)-1):
    for j in range(i+1, len(x)):
        if sum(x[i:j]) >= y:
            count.append(len(x[i:j]))

if min(count) != len(x) and len(count) > 0:
    print(min(count))
else:
    print(0)