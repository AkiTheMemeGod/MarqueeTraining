m = []
import numpy as np

for i in range(3):
    y = list(map(int, input().split()))
    m.append(y)
c = []
for i in m:
    for j in i:
        c.append(j)
z = set(c)
if len(z) != len(c):
    exit("Duplicate elements detected")
diag = 0
rows = 0
cols = 0
arr = np.array(m)
trans = arr.transpose()

for i in arr:
    print(f"{i} ==> {sum(i)}")
    if sum(i) == 15:
        rows += 1
print("|  |  |")
for i in trans:
    print(sum(i), end=' ')
    # print(i+" ==> "+sum(i))
    cols += 1
print()
x = 0
for i in arr:
    # print(i+" ==> "+sum(i))
    diag += i[x]
    x += 1


if cols == 3 and rows == 3 and diag == 15:
    print("Each Rows Sum up to 15\nEach Columns Sum up to 15\nThe diagonal sums up to 15")

else:
    print("Either the rows or the Columns are not up to the standards i.e not sum of 15")
    print(rows)
    print(cols)
    print(diag)

