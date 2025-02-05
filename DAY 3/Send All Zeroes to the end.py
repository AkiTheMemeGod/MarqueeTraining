x = [0, 12, 0, 5, 2, 0, 3, 12, 0]
print("Before : ", x)
for i in x:
    if i == 0:
        x.remove(i)
        x.append(0)

print("After : ",x)