x = [10, 100, 1000, 1, 50]
pairs = []
for i in range(0,len(x)):
    if i == 0:
        pairs.append((x[i+1] - x[i]))
    elif i == len(x)-1:
        pairs.append((x[i] - x[i-1]))
    else:
        pairs.append((x[i] - x[i+1], x[i] - x[i-1]))

print(pairs)